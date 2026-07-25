# main.py
import logging
from src.core.logging import setup_logging

# 1. Initialize your configuration
setup_logging(log_level="DEBUG")

# 2. Get a logger instance for the current module
logger = logging.getLogger(__name__)

# 3. Emit test messages across different severity levels
logger.debug("This is a debug message (visible because level is DEBUG)")
logger.info("Application starting...")
logger.warning("Something looks slightly off!")
logger.error("An error occurred!")