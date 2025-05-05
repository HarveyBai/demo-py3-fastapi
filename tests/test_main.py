import io
import sys
from unittest.mock import patch

import pytest

from src.demo_py3_fastapi.main import main


def test_main_output():
    # 捕获标准输出
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # 执行main函数
    main()

    # 恢复标准输出
    sys.stdout = sys.__stdout__

    # 验证输出
    assert captured_output.getvalue().strip() == "Hello from a!"


# 使用mock测试
def test_main_with_mock():
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with("Hello from a!")


# 参数化测试示例（虽然当前函数不需要参数，但这是一个示例）
@pytest.mark.parametrize(
    "expected_output",
    [
        ("Hello from a!"),
    ],
)
def test_main_parametrize(expected_output):
    with patch("builtins.print") as mock_print:
        main()
        mock_print.assert_called_once_with(expected_output)


# 测试入口点
def test_main_entry_point():
    with patch("src.demo_py3_fastapi.main.main") as mock_main:
        import src.demo_py3_fastapi.main as main

        # 模拟从命令行运行
        with patch.object(main, "__name__", "__main__"):
            main.main()
        mock_main.assert_called_once()
