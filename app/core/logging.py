import logging


def configure_logging(log_level:str) -> None:
    numeric_level=getattr(
        logging,
        log_level.upper()
    )

    logging.basicConfig(
        level=numeric_level,
        format=(
            "%(asctime)s | "
            "%(asclevelname)s | "
            "%(ascname)s | "
            "%(message)s"
        ),
        force=True
    )