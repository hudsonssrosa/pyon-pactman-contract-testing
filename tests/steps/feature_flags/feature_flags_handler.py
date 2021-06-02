from factory.base_context import BaseContext as Bctx
from factory.api.request_wrapper import BaseRequests
from factory.handling.configcat_impl import ConfigCat
from factory.utils.StringsUtil import StringUtil as String
from settings.secrets_data_provider import SecretsSettings as SecFile
from factory.utils.DataEncryptedUtil import DataEncrypted as RandomData


is_production_environment = Bctx.flag_environment.get() == "production"
is_staging_environment = Bctx.flag_environment.get() == "staging"
is_dev_environment = Bctx.flag_environment.get() == "dev"


def is_the_flag_enabled(flag, context_data):

    """
    Use this method in the scenario steps to check feature flags from application reducing the complexity
    in use a same scenario to recognise when a feature flag from ConfigCat should be activated or deactivated
    for a specific user or not. To see further information about ConfigCat client implementation,
    get this link:

        https://configcat.com/docs/sdk-reference/python/

    Call this method considering

        from features.steps.feature_flags.feature_flag_handler import *

        @given("that a feature flag example is set")
        def step_given_that_a_feature_flag_is_set(context):
            if is_the_flag_enabled(flag=FFlag.ff_my_flag_to_be_on, context_data=context.user_email):
                # [IMPLEMENT THE LOGIC FOR NEW FF HERE]
            else:
                # [IMPLEMENT OTHER LOGIC IF THE FLAG IS SKIPPED]

    :return:
    """
    return ConfigCat.get_feature_flag(flag, fflag_state=True, email_address=context_data)


class FeatureFlagHandler(BaseRequests):
    """[summary]

    Args:
        BaseRequests (object): If your app is using ConfigCat to handle feature flags for the environments, just provide the existing flag name here
    """

    ff_my_flag_to_be_on_1 = "configcat_flag_name_1_here"
    ff_my_flag_to_be_on_2 = "configcat_flag_name_2_here"
    ff_my_flag_to_be_on_3 = "configcat_flag_name_3_here"
