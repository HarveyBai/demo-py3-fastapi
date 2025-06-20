from pathlib import Path
from my_utils.path_util import PathUtil, hello
from my_utils import path_util

from my_log.app_log import logger


class TestPathUtil:
    """测试PathUtil类"""

    def test_hello(self):
        """测试hello方法"""
        # assert hello() == "hello"
        assert path_util.hello() == "hello"

    def test_get_project_root(self):
        """测试获取项目根路径"""
        root_path = PathUtil.get_project_root()
        logger.info(f"root_path: {root_path}")
        assert root_path is not None
        assert isinstance(root_path, Path)
        assert root_path.exists()
        assert root_path.is_dir()
