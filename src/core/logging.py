import logging
import sys


def setup_logging(log_level: str = "INFO") -> None:
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )