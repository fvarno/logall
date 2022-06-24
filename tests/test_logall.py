r"""
Pytest environment cannot write to file. T
"""

import logging

from logall import PyLogger

data_points = [
    ["loss", 10.1, 0],
    ["loss", 12.3, 1],
    ["accuracy", 0.9, 15],
]


def test_pylogger(caplog):
    logger = PyLogger("log.log")
    with caplog.at_level(logging.INFO):
        for point in data_points:
            logger.log_scalar(*point)
        for i, point in enumerate(data_points):
            assert caplog.records[i].message == ",".join(map(str, point))
