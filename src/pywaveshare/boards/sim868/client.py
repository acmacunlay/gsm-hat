from . import config, worker


class Client:
    logger = config.get_logger("client")

    def __init__(self, config: config.Config) -> None:
        self.config = config
        self.worker = worker.Worker(self.config)
        self.worker.start()
