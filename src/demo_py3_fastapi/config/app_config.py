from pydantic_settings import BaseSettings
from typing import Literal, Dict, Any, Optional


class AppSettings(BaseSettings):
    """
    应用配置
    """

    app_name: str = "demo-py3-fas Ftapi"
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
