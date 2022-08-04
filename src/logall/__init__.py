import logging
import os

from .logclasses import Logger
from .logclasses import MLFlowLogger
from .logclasses import PolyaxonLogger
from .logclasses import PyLogger
from .logclasses import TensorboardLogger

__version__ = "0.0.2"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = [
    module[:-3]
    for module in os.listdir(os.path.dirname(__file__))
    if module != "__init__.py" and module[-3:] == ".py"
]

__all__ += ["Logger", "TensorboardLogger", "PyLogger", "MLFlowLogger", "PolyaxonLogger"]
