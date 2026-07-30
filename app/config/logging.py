import logging
import sys


def configure_logging() -> None:
    """
    Configure application-wide logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger instance.
    """

    return logging.getLogger(name)