import os
import pytest
from typing import Generic, TypeVar, Mapping, Iterator, Dict

from factory.base_context import BaseContext as Bctx
from factory.handling.base_logging import BaseLogging as Log
from factory.handling.running_exception import RunningException as Rexc
from factory.utils.DataEncryptedUtil import DataEncrypted as RandData
from settings.cli_impl import Cli
from settings.secrets_data_provider import SecretsSettings as SecFile


@pytest.fixture
def before_all():
    Bctx.random_data.set(RandData.generate_random_data(length=7))
    Log.info(f"Hash available for test scope: {Bctx.random_data.get()}")
    Bctx.configcat_sdk_key_ff_dev.set(SecFile.get_secret_configcat_sdk_key_ff_dev())
    Bctx.configcat_sdk_key_ff_staging.set(SecFile.get_secret_configcat_sdk_key_ff_staging())
    Bctx.configcat_sdk_key_ff_production.set(SecFile.get_secret_configcat_sdk_key_ff_production())
    Log.info(f"ConfigCat SDK Keys are ready!")


def get_flag_value(environment=False, skipped_tests=False):
    try:
        if environment:
            return str(Cli.get_arguments()["environment"])
        if skipped_tests:
            return str(Cli.get_arguments()["skipped_tests"])
    except LookupError as le:
        Rexc.raise_exception_error("Unreachable context", le)


@pytest.fixture
def afer_all():
    Log.info("module %s" % __name__)
