# 全局配置管理对象


import argparse
import os
import pprint
import sys
from typing import override

from dotenv import load_dotenv

# import tomllib

# Define a generic type for configuration values


class GlobalConfig:
    """
    全局配置管理类
    """

    def __init__(self) -> None:
        print("GlobalConfig.__init__...")
        # self._config = {}
        self.parse_cli_args()

    @staticmethod
    def parse_cli_args():
        """
        解析命令行参数
        """
        if "uvicorn" in sys.argv[0]:
            # 使用uvicorn启动时，命令行参数需要按照uvicorn的文档进行配置，无法自定义参数
            pass
        else:
            # 使用argparse定义命令行参数
            parser = argparse.ArgumentParser(description="命令行参数")
            _ = parser.add_argument("--env", type=str, default="", help="运行环境")
            # 解析命令行参数
            args = parser.parse_args()
            # 使用 getattr 获取环境参数并确保类型安全
            env_value: str = getattr(args, "env", "")
            # 设置环境变量，如果未设置命令行参数，默认APP_ENV为dev
            os.environ["APP_ENV"] = env_value if env_value else "dev"
        # 读取运行环境
        run_env = os.environ.get("APP_ENV", "")
        # 运行环境未指定时默认加载.env.dev
        env_file = ".env.dev"
        # 运行环境不为空时按命令行参数加载对应.env文件
        if run_env != "":
            env_file = f".env.{run_env}"
        # 加载配置
        _ = load_dotenv(env_file, verbose=True, override=True)
        _ = load_dotenv(".env.private", verbose=True, override=True)
        # 加载toml格式配置
        # with open(f"config/{run_env}.toml", "rb") as f:
        #     _data = tomllib.load(f, parse_float=decimal.Decimal)
        # _DB_HOST = os.getenv("DATABASE_HOST", getattr(getattr(_data, "database", {}), "host", ""))
        # print(_DB_HOST)

    def reload_config(self):
        """
        重新加载配置
        """
        # 清空缓存
        # self.get_app_config.cache_clear()
        # self.get_database_config.cache_clear()
        # 重新加载配置
        self.parse_cli_args()

    def get(self, key: str, default: str | None = None) -> str | None:
        """
        获取配置项

        Args:
            key: 配置项键名
            default: 默认值，当配置项不存在时返回

        Returns:
            配置项值
        """
        return os.environ.get(key, default)
        # return self._config.get(key, default)

    def print_data(self) -> None:
        # pprint.pprint(dict(os.environ))
        for key, value in os.environ.items():
            print(f"{key}={value}")

    # @lru_cache()
    # def get_app_config(self):
    #     """
    #     获取应用配置
    #     """
    #     # 实例化应用配置模型
    #     return AppSettings()

    # @lru_cache()
    # def get_database_config(self):
    #     """
    #     获取数据库配置
    #     """
    #     # 实例化数据库配置模型
    #     return DataBaseSettings()


# 实例化获取配置类
_config = GlobalConfig()
print("_config: ", _config)
# # 应用配置
# AppConfig = _config.get_app_config()
# # 数据库配置
# DataBaseConfig = _config.get_database_config()

if __name__ == "__main__":
    print("global_config main....")
    _config.print_data()
