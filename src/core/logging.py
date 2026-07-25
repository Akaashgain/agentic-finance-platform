import logging
import sys


def setup_logging(level: str = "INFO") -> None:
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )