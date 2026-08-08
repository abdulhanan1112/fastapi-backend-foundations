import logging
from collections.abc import Iterator
from contextlib import contextmanager
from time import perf_counter


logger = logging.getLogger(__name__)


@contextmanager
def measure_time( operation : str) -> Iterator[None]:
    started_at=perf_counter()

    try:
        yield
    
    finally:
        total_time=perf_counter() - started_at
        logger.info(
            "operation_completed operation=%s total_time=%.3f",
            operation,
            total_time

        )


