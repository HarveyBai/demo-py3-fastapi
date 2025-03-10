# 尝试导入loguru，如果失败则提示安装
try:
    from loguru import logger
except ImportError:
    raise ImportError("请先安装loguru包: pip install loguru")
import sys
from pathlib import Path
from .config import get_settings

settings = get_settings()

# 创建日志目录
log_path = Path("logs")
log_path.mkdir(exist_ok=True)

# 移除默认的处理器
logger.remove()

# 添加控制台输出处理器
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    enqueue=True
)

# 添加文件输出处理器
logger.add(
    str(log_path / "app_{time}.log"),
    rotation="00:00",  # 每天零点创建新文件
    retention="30 days",  # 保留30天的日志
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    encoding="utf-8",
    enqueue=True
)

# 导出logger实例
app_logger = logger