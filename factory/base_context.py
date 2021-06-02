import contextvars


class BaseContext:

    """ General Context """

    cur_tag = contextvars.ContextVar("cur_tag")
    random_data = contextvars.ContextVar("random_data")
    screenshot_path = contextvars.ContextVar("screenshot_path")

    """ ConfigCat Context """
    configcat_sdk_key_ff_dev = contextvars.ContextVar("configcat_sdk_key_ff_dev")
    configcat_sdk_key_ff_staging = contextvars.ContextVar("configcat_sdk_key_ff_staging")
    configcat_sdk_key_ff_production = contextvars.ContextVar("configcat_sdk_key_ff_production")

    """ CLI Context """
    flag_mode = contextvars.ContextVar("flag_mode")
    flag_os = contextvars.ContextVar("flag_os")
    flag_os_version = contextvars.ContextVar("flag_os_version")
    flag_scenario = contextvars.ContextVar("flag_scenario")
    flag_tags = contextvars.ContextVar("flag_tags")
    flag_target = contextvars.ContextVar("flag_target")
    flag_environment = contextvars.ContextVar("flag_environment")
    flag_skip_tests = contextvars.ContextVar("flag_skip_tests")

    """ URL Context """
    app_url = contextvars.ContextVar("app_url")
    admin_url = contextvars.ContextVar("admin_url")
    email_url = contextvars.ContextVar("email_url")
