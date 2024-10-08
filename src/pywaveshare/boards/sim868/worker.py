import threading

from . import config, itc, protocols


class Worker(threading.Thread):
    logger = config.get_logger("worker")

    def __init__(self, config: config.Config) -> None:
        super().__init__()

        self.config = config
        self.protocols = protocols.SupportedProtocolFactory()

    def run(self) -> None:
        itc.IS_WORKER_RUNNING.set()
        while itc.IS_WORKER_RUNNING.is_set():
            pass
