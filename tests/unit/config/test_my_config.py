# -*- coding: utf-8 -*-
import os
from demo_py3_fastapi.config.my_config import my_config, MyConfig
import tempfile
import json

from my_utils.string_util import parse_boolean

# src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
# print("src_path:", src_path)
# sys.path.append(src_path)


class TestMyConfig:
    """测试MyConfig类"""

    def test_init_config(self):
        """测试配置初始化"""
        ''.boolean()
        config = MyConfig()
        assert config is not None
        assert isinstance(config, MyConfig)

    def test_get_config(self):
        """测试获取配置项"""
        config = MyConfig()

        # 测试获取默认配置
        assert config.get("app_name") == "My-FastAPI-2"
        assert config.get("app_host") == "0.0.0.0"
        assert config.get("APP_PORT") == "9099"
        # assert config.get("APP_WORK_DIR") == os.getcwd()
        assert config.get_app_config().app_work_dir == os.getcwd()
        assert config.get("app_version") == "1.0.0"
        assert parse_boolean(config.get("app_reload")) is True
        assert config.get("debug") in (False, None)

        # 测试获取不存在的配置项
        assert config.get("non_existent_key") is None
        assert config.get("non_existent_key", "default") == "default"

    # def test_set_config(self):
    #     """测试设置配置项"""
    #     config = MyConfig()

    #     # 测试设置新配置项
    #     config.set("new_key", "new_value")
    #     assert config.get("new_key") == "new_value"

    #     # 测试更新已存在的配置项
    #     config.set("app_name", "new_app_name")
    #     assert config.get("app_name") == "new_app_name"

    # def test_load_from_env(self):
    #     """测试从环境变量加载配置"""
    #     # 设置测试环境变量
    #     os.environ["APP_NAME"] = "env_app_name"
    #     os.environ["PORT"] = "9000"

    #     config = MyConfig()
    #     config.load_from_env()

    #     assert config.get("app_name") == "env_app_name"
    #     assert config.get("port") == 9000

    #     # 清理环境变量
    #     del os.environ["APP_NAME"]
    #     del os.environ["PORT"]

    # def test_load_from_file(self):
    #     """测试从配置文件加载配置"""

    #     # 创建临时配置文件
    #     config_data = {"app_name": "file_app_name", "port": 9000}

    #     with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
    #         json.dump(config_data, temp_file)
    #         temp_file_path = temp_file.name

    #     config = MyConfig()
    #     config.load_from_file(temp_file_path)

    #     assert config.get("app_name") == "file_app_name"
    #     assert config.get("port") == 9000

    #     # 清理临时文件
    #     os.unlink(temp_file_path)

    # def test_to_dict(self):
    #     """测试转换配置为字典"""
    #     config = MyConfig()
    #     config_dict = config.to_dict()

    #     assert isinstance(config_dict, dict)
    #     assert config_dict["app_name"] == "demo-py3-fastapi"
    #     assert config_dict["host"] == "127.0.0.1"
    #     assert config_dict["port"] == 8000
    #     assert config_dict["debug"] is True
