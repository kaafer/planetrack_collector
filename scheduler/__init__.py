import atexit
from typing import Any

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.base import BaseScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from scheduler.jobs import register_radar_jobs


class Scheduler:
    def __init__(self, *args, **kwargs) -> None:
        actual_class = BackgroundScheduler if kwargs.pop('background', True) else BlockingScheduler
        self._scheduler: BaseScheduler = actual_class(*args, **kwargs)
        register_radar_jobs(self._scheduler)

    def start(self, *args, **kwargs):
        if isinstance(self._scheduler, BlockingScheduler):
            try:
                self._scheduler.start(*args, **kwargs)
            except (KeyboardInterrupt, SystemExit):
                raise RuntimeError('Unexpected Scheduler implementation')
        elif isinstance(self._scheduler, BackgroundScheduler):
            self._scheduler.start(*args, **kwargs)
            atexit.register(self._scheduler.shutdown)


def __getattr__(self, name: str) -> Any:
    return self._scheduler.__getattribute__(name)
