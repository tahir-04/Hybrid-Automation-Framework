from loguru import logger
import sys
import os

os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    format="{time} | {level} | {message}"
)

logger.add(
    "logs/framework.log",
    rotation="5 MB",
    retention="10 days",
    level="INFO"
)

def get_logger():
    return logger