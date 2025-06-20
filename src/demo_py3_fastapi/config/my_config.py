import argparse
import os
import sys
from dotenv import load_dotenv
from functools import lru_cache
from pydantic import computed_field
from pydantic_settings import BaseSettings
from typing import Literal, Dict, Any, Optional


class AppSettings(BaseSettings):
    """
    应用配置
    """

    app_name: str = "demo-py3-fastapi"
    app_env: str = "dev"
    app_work_dir: str = os.getcwd()
    app_host: str = "0.0.0.0"
    app_port: int = 9099
    app_version: str = "1.0.0"
    app_reload: bool = True
    app_ip_location_query: bool = True
    app_same_time_login: bool = True


class DataBaseSettings(BaseSettings):
    """
    数据库配置
    """

    db_type: Literal["mysql", "postgresql"] = "mysql"
    db_host: str = "127.0.0.1"
    db_port: int = 3306
    db_username: str = "root"
    db_password: str = "mysqlroot"
    db_database: str = "ruoyi-fastapi"
    db_echo: bool = True
    db_max_overflow: int = 10
    db_pool_size: int = 50
    db_pool_recycle: int = 3600
    db_pool_timeout: int = 30

    @computed_field
    @property
    def sqlglot_parse_dialect(self) -> str:
        if self.db_type == "postgresql":
            return "postgres"
        return self.db_type


class MyConfig:
    """
    自定义配置类
    """

    def __init__(self):
        self._config = {}
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
            parser.add_argument("--env", type=str, default="", help="运行环境")
            # 解析命令行参数
            args = parser.parse_args()
            # 设置环境变量，如果未设置命令行参数，默认APP_ENV为dev
            os.environ["APP_ENV"] = args.env if args.env else "dev"
        # 读取运行环境
        run_env = os.environ.get("APP_ENV", "")
        # 运行环境未指定时默认加载.env.dev
        env_file = ".env.dev"
        # 运行环境不为空时按命令行参数加载对应.env文件
        if run_env != "":
            env_file = f".env.{run_env}"
        # 加载配置
        load_dotenv(env_file, verbose=True, override=True)

    def reload_config(self):
        """
        重新加载配置
        """
        # 清空缓存
        self.get_app_config.cache_clear()
        self.get_database_config.cache_clear()
        # 重新加载配置
        self.parse_cli_args()

    def get(self, key: str, default: Any = None) -> Any:
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

    @lru_cache()
    def get_app_config(self):
        """
        获取应用配置
        """
        # 实例化应用配置模型
        return AppSettings()

    @lru_cache()
    def get_database_config(self):
        """
        获取数据库配置
        """
        # 实例化数据库配置模型
        return DataBaseSettings()


# 实例化获取配置类
my_config = MyConfig()
# # 应用配置
# AppConfig = my_config.get_app_config()
# # 数据库配置
# DataBaseConfig = my_config.get_database_config()
