import threading

from . import config, itc


class Worker(threading.Thread):
    def __init__(self, config: config.Config) -> None:
        super().__init__()

        self.config = config

    def run(self) -> None:
        itc.IS_WORKER_RUNNING.set()
        while itc.IS_WORKER_RUNNING.is_set():
            pass
