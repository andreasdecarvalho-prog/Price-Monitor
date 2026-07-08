import logging
from logging.handlers import TimedRotatingFileHandler

# Create a timed rotating file handler
file_handler = TimedRotatingFileHandler(
    "logs/pipeline.log",
    when="midnight",      # rotate at midnight
    interval=1,           # every 1 day
    backupCount=7,        # keep 7 days of logs
    encoding="utf-8"
)

# Define format
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
file_handler.setFormatter(formatter)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        file_handler,
        logging.StreamHandler()
    ]
)