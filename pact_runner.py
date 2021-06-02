import json
import sys, os
from factory.base_context import BaseContext as Bctx
from factory.handling.base_logging import BaseLogging as Log

from settings.cli_impl import Cli
from settings.environment_data_provider import EnvSettings as Conf
from factory.handling.allure_report_impl import AllureReport


allure_results_dir = "allure-results"


def main():
    args = Cli.parse_external_args()
    Cli.set_arguments(args)
    try:
        execute_commands()
    except:
        return 1


def execute_commands():
    try:
        AllureReport.set_screenshot_path(Conf.get_screenshot_path())
        AllureReport.cleanup_reports(Conf.get_generate_report())
        run_unittest_with_allure_command()
    finally:
        AllureReport.generate_report_command(
            Conf.get_generate_report(), Conf.get_report_library_path()
        )
        AllureReport.open_report_command_locally(
            Conf.get_generate_report(), Conf.get_report_library_path()
        )


def run_unittest_with_allure_command():
    suite_name = Cli.parse_tags()
    env_selected = Bctx.flag_environment.get()
    environment_suites = f"tests{os.sep}feature_domains{os.sep}{env_selected}{os.sep}{suite_name}"
    Log.info(f"Running API tests in {env_selected}...")
    allure_results_env = os.path.abspath(f"{allure_results_dir}-{env_selected}")
    result = os.system(
        f"python3 -m pytest --capture=tee-sys --log-cli-level=ERROR {environment_suites} --alluredir {allure_results_env}"
    )
    if result == 1:
        raise BaseException


class PactRunner:
    if __name__ == "__main__":
        sys.exit(main())
