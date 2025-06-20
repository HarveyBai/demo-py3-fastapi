import os
import sys
import time
from loguru import logger

log_path = os.path.join(os.getcwd(), "logs")
if not os.path.exists(log_path):
    os.mkdir(log_path)

# log_error = logger.bind(type="error")
# log_error_path = os.path.join(
#     log_path, f'{time.strftime("%Y-%m-%d")}_error.log', serialize=True
# )
# log_error.add(log_error_path, filter=lambda x: x["extra"].get("type") == "error")

log_path_all = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_all.log')

logger.add(sys.stderr, format="{time:YYYY-MM-DD} | {level} | {message}")
logger.add(
    log_path_all,
    rotation="50MB",
    level="DEBUG",
    encoding="utf-8",
    enqueue=True,
    compression="zip",
)
