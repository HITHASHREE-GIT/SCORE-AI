from pathlib import Path
from loguru import logger

# Create logs directory if it doesn't exist
Path("logs").mkdir(exist_ok=True)

# Configure logger
logger.remove()

logger.add(
    "logs/score.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)