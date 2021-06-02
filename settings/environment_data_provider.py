import os
from sys import platform as _platform
from factory.utils.OsUtil import OsUtil
from factory.utils.FileUtil import FileUtil
from factory.utils.TextColorUtil import TextColor as Color


ENV_SETTINGS = "env_settings"
LINUX_OR_IOS = _platform == "linux" or _platform == "linux2" or _platform == "darwin"
WINDOWS = _platform == "win32" or "win64"
UTF8_UPPER = "UTF-8"
UTF8 = "utf-8"
SEP = os.sep


def read_env_conf_properties_to_os_platform(file_name):
    if LINUX_OR_IOS:
        return FileUtil.read_properties(
            [OsUtil.search_file_in_root_dir(OsUtil.get_current_dir_name(), file_name)]
        )
    elif WINDOWS:
        return FileUtil.read_properties(
            [OsUtil.search_file_in_root_dir(OsUtil.get_current_dir(), file_name)]
        )


CONFIG = read_env_conf_properties_to_os_platform(ENV_SETTINGS + ".properties")


class EnvSettings:
    @staticmethod
    def get_screenshot_path():
        from factory.handling.allure_report_impl import allure_report_dir

        return str(f"{allure_report_dir}{SEP}screenshots")

    # ---- REPORT PARAMETERS ----
    @staticmethod
    def get_report_library_path():
        report_lib_path = os.path.abspath(CONFIG.get("report", "report_library_path"))
        return report_lib_path.replace("\\", SEP).strip()

    @staticmethod
    def get_generate_report():
        report_enabled = CONFIG.get("report", "generate_report", fallback=None)
        return str(report_enabled).strip() == "true"

    # ---- API PARAMETERS ----
    @staticmethod
    def get_api_request_timeout():
        return CONFIG.get("api", "api_request_timeout")

    # ---- DEBUG PARAMETERS ----
    @staticmethod
    def get_dev_mode():
        return CONFIG.get("cli-args-debug", "development_mode", fallback=None)

    @staticmethod
    def get_debug_flag_environment(default_env):
        env_config = CONFIG.get("cli-args-debug", "debug_flag_environment", fallback=None)
        environment_set = default_env if env_config is None else env_config
        return environment_set

    @staticmethod
    def get_debug_flag_target():
        return str(CONFIG.get("cli-args-debug", "debug_flag_target", fallback=None).strip())

    @staticmethod
    def get_debug_flag_mode():
        return str(CONFIG.get("cli-args-debug", "debug_flag_mode", fallback=None).strip())

    @staticmethod
    def get_debug_tags():
        return CONFIG.get("cli-args-debug", "debug_tags", fallback=None)

    @staticmethod
    def get_debug_skip_tests():
        return CONFIG.get("cli-args-debug", "debug_skip_tests", fallback=None)

    @staticmethod
    def get_debug_flag_os():
        return str(CONFIG.get("cli-args-debug", "debug_flag_os", fallback=None).strip())

    @staticmethod
    def get_debug_flag_os_version():
        return str(CONFIG.get("cli-args-debug", "debug_flag_os_version", fallback=None).strip())

    # ---- BROWSERSTACK PARAMETERS ----
    @staticmethod
    def get_bs_user_key():
        return CONFIG.get("browserstack", "bs_user_key")

    @staticmethod
    def get_bs_access_key():
        return CONFIG.get("browserstack", "bs_access_key", fallback=None)

    @staticmethod
    def get_bs_record_video():
        return CONFIG.get("browserstack", "bs_record_video").strip()

    # ---- LAMBDATEST PARAMETERS ----
    @staticmethod
    def get_lt_email():
        return CONFIG.get("lambdatest", "lt_email")

    @staticmethod
    def get_lt_username():
        return CONFIG.get("lambdatest", "lt_username")

    @staticmethod
    def get_lt_app_key():
        return CONFIG.get("lambdatest", "lt_key", fallback=None)

    @staticmethod
    def get_lt_video():
        return CONFIG.get("lambdatest", "lt_video")

    @staticmethod
    def get_lt_console():
        return CONFIG.get("lambdatest", "lt_console")

    @staticmethod
    def get_lt_visual():
        return CONFIG.get("lambdatest", "lt_visual")

    @staticmethod
    def get_lt_network():
        return CONFIG.get("lambdatest", "lt_network")

    @staticmethod
    def get_lt_tunnel():
        return CONFIG.get("lambdatest", "lt_tunnel", fallback=None)

    @staticmethod
    def get_lt_tunnel_name():
        tunnel_name = CONFIG.get("lambdatest", "lt_tunnel_name")
        if tunnel_name is not None:
            return f"--tunnelName {tunnel_name}"
        else:
            return ""

    @staticmethod
    def show_logo():
        logo = Color.red(
            """
                                              █                                                             
                            █████████.     :██                                                             
                         █████      ███    ███                                                              
                       ███           ██   ██                 .█.                                            
                     ███             ██  ██               █████████                ,█:                      
                   ███              :█: ██               ██       :██           :███████                    
                  ██               ███  ██        ████  ██     ███  ███       ███,    ,█:   ,████:          
                :██              ███:   ██      ███ ,█  ██       ██   ██    ███        ██ ████::█████:      
               ███         :██████      ███ :████   ██   ██     :█:    ██:███          ,███          ███:   
              ███                        :████     ██     ████████      ███                            :██: 
             ██:                                  ██        `█´                                          : 
            ██:                                  ██                                                         
           :██                                  ██        ██████     ,████     .█████    .████████
           ██                                 ,██         █     █   █    `█   █     █   █    █    █
          ██                                 ███         █     █       .██   █              █
         ██                                 ███         ██████´   ███████   █              █
         ██                                ██          █         █      █  █              █
        ██                               :██          █         █,    ██  █     ,█       █
        █                                +█         .██          ██████  `██████´      ███
            
                     PYON-PACTMAN | Pact-based Contract Testing | Created by: Hudson S. S. Rosa 
            """
        )
        """ Generated with http://manytools.org/hacker-tools/convert-images-to-ascii-art/go/ """
        return print(logo)
