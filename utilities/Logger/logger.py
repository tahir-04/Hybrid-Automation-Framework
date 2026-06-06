from loguru import logger
import os

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    f"{LOG_DIR}/framework.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

def get_logger():
    return logger