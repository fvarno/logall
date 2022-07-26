import logging
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import mlflow
import polyaxon
from torch.utils.tensorboard import SummaryWriter

from .utils import apply_on_dict


class Logger(object):
    def __init__(self, path: str = None, ignore_patterns: List[str] = None) -> None:
        self._path = path
        if ignore_patterns is None:
            self._ignore_patterns = []
        else:
            self._ignore_patterns = ignore_patterns
        self._logger_obj = self.register_logger_object()

    #  The following are the abstract methods to be implemented by children classes
    def register_logger_object(self) -> Any:
        """This abstract method should be implemented by child class.

        Returns:
            object: the logger object to return when get_logger_object is called.
        """
        pass

    def log_scalar(key: str, value: float, step: Optional[int] = None) -> None:
        r"""log a single scalar.

        Args:
            key (str): scalar name
            value (float): scalar value
            step (Optional[int], optional): scalar step. Defaults to zero if
                unspecified.

        .. code-block:: python
        :caption: Example

            my_logger.log_scalar('loss', 2.3)
        """
        pass

    # the following methods are already implemented

    def log_scalars(
        self, scalars: Dict[str, float], step: Optional[int] = None
    ) -> None:
        """log multiple metrics.

        Args:
            scalars (Dict[str, float]): Dict of scalar names.
            step (Optional[int], optional): step at which log is desired.
                Defaults to zero if
                unspecified.
            my_logger.log_scalar({'loss': 2.3, 'norm': 4.2})
        """
        apply_on_dict(scalars, self.log_scalar, step=step)

    def get_logger_object(self) -> Any:
        return self._logger_obj

    def get_path(self):
        return self._path

    def get_ignore_patterns(self):
        return self._ignore_patterns

    def get_dir(self) -> str:
        raise NotImplementedError


class TensorboardLogger(Logger):
    def __init__(self, path: str, ignore_patterns: List[str] = None) -> None:
        super().__init__(path, ignore_patterns=ignore_patterns)

    def register_logger_object(self) -> Any:
        return SummaryWriter(log_dir=self.get_path())

    def log_scalar(self, key: str, value: float, step: Optional[int] = None) -> None:
        r"""log a single scalar.

        Args:
            key (str): scalar name
            value (float): scalar value
            step (Optional[int], optional): scalar step. Defaults to zero if
                unspecified.

        .. code-block:: python
        :caption: Example


        from logall import TensorboardLogger
        logger = TensorboardLogger('runs')
        logger.log_scalar('loss', 2.3)
        """
        # check for ignore pattern
        for pattern in self.get_ignore_patterns():
            if key in pattern:
                return

        logger_ob = self.get_logger_object()
        logger_ob.add_scalar(key, value, step)

    def get_dir(self):
        return self._logger_obj.get_logdir()


class PyLogger(Logger):
    def __init__(
        self, path: str, ignore_patterns: List[str] = None, filemode="w"
    ) -> None:
        self.filemode = filemode
        super().__init__(path, ignore_patterns=ignore_patterns)

    def register_logger_object(self) -> Any:
        print(self.get_path())
        logging.basicConfig(filename=self.get_path(), level=0, filemode=self.filemode)
        handle = logging.getLogger()
        return handle

    def log_scalar(self, key: str, value: float, step: Optional[int] = None) -> None:
        # check for ignore pattern
        for pattern in self.get_ignore_patterns():
            if key in pattern:
                return

        logger_ob = self.get_logger_object()
        logger_ob.info(f"{key},{value},{step}")

    # TODO: implement get_dir for pylogger
    def get_dir(self) -> str:
        raise not NotImplementedError


class MLFlowLogger(Logger):
    def __init__(self, path: str, ignore_patterns: List[str] = None, **kwargs) -> None:
        self.kwargs = kwargs
        super().__init__(path, ignore_patterns=ignore_patterns)

    def register_logger_object(self) -> Any:
        # the following gets the active run (if any) otherwise makes new
        mlflow.start_run(**self.kwargs)
        return mlflow

    def log_scalar(self, key: str, value: float, step: Optional[int] = None) -> None:
        # check for ignore pattern
        for pattern in self.get_ignore_patterns():
            if key in pattern:
                return
        logger_ob = self.get_logger_object()
        logger_ob.log_metric(key, value, step)

    def get_dir(self) -> str:
        return mlflow.get_artifact_uri()


class PolyaxonLogger(MLFlowLogger):
    def __init__(self, path: str, ignore_patterns: List[str] = None, **kwargs) -> None:
        super().__init__(path, ignore_patterns=ignore_patterns, **kwargs)

    def register_logger_object(self) -> Any:
        # the following gets the active run (if any) otherwise makes new
        handle = polyaxon.tracking.init(**self.kwargs)
        return handle

    # TODO: implement get_dir for polyaxon
    def get_dir(self) -> str:
        raise not NotImplementedError
