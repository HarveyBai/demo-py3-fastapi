import os
from pathlib import Path
import sys


class PathUtil:
    """
    路径工具类
    """

    @staticmethod
    def get_project_root() -> Path:
        """
        获取项目根路径
        :return:
        """
        return Path(__file__).parent.parent.parent.parent

    @staticmethod
    def show_all_path():
        """
        打印出所有的相关路径
        :return:
        """
        # print("sys.path:", sys.path)
        # print("*" * 66)

        _cwd = os.getcwd()
        print(f"_cwd: {_cwd}")

        _exePath = sys.executable
        print(f"_exePath: {_exePath}")

        _exeDir = os.path.dirname(_exePath)

        script_path = os.path.abspath(__file__)  # 包含文件名，如 '/project/src/main.py'
        real_path = os.path.realpath(__file__)
        print(f"script_path: {script_path}, real_path: {real_path}")
        script_dir = os.path.dirname(script_path)
        print(f"script_dir: {script_dir}")

        _userHome = os.path.expanduser("~")
        print(f"_userHome: {_userHome}")

        return os.getcwd()

    @staticmethod
    def get_log_path() -> Path:
        """
        获取日志文件路径
        :return:
        """
        script_path = os.path.abspath(__file__)  # 包含文件名，如 '/project/src/main.py'
        script_dir = os.path.dirname(script_path)
        print(f"script_path: {script_path}, script_dir: {script_dir}")
        return PathUtil.get_project_root() / "logs"

    @staticmethod
    def get_config_path() -> Path:
        """
        获取配置文件路径
        :return:
        """
        return PathUtil.get_project_root() / "config"


def hello():
    return "hello"


if __name__ == "__main__":
    PathUtil.show_all_path()
