r"""
Pytest environment cannot write to file. T
"""

import logging

from logall import MLFlowLogger
from logall import PolyaxonLogger
from logall import PyLogger
from logall import TensorboardLogger
from logall.utils import apply_on_dict

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


def test_tblogger():
    tb_logger = TensorboardLogger(None)
    assert tb_logger.get_dir() is not None


def test_plxlogger():
    plx_logger = PolyaxonLogger(None, is_offline=True)
    assert plx_logger.get_dir() is not None


def test_mlflogger():
    mlf_logger = MLFlowLogger(None)
    assert mlf_logger.get_dir() is not None


def test_apply_on_dict():
    sample_dict = dict(a_1=2, b_3=5)

    def fn(key, val):
        _, factor = key.split("_")
        return int(factor) * val

    res = apply_on_dict(sample_dict, fn, return_as_dict=True)
    assert res["a_1"] == 2
    assert res["b_3"] == 15
