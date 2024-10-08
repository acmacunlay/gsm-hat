from . import config, itc, worker


class Client:
    logger = config.get_logger("client")

    def __init__(self, config: config.Config) -> None:
        self.config = config
        self.worker = worker.Worker(self.config)

    def start(self) -> None:
        itc.IS_WORKER_RUNNING.set()
        self.worker.start()

    def send_at_command(self, command: str):
        pass
