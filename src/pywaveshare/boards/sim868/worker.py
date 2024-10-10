import enum
import threading
import typing

import serial

from . import config, exceptions, itc, protocols


class WorkerState(enum.Enum):
    START = 0x0000
    LISTEN_TO_CLIENT = 0x0001
    LISTEN_TO_SERIAL = 0x0002


class Worker(threading.Thread):
    logger = config.get_logger("worker")

    def __init__(self, config: config.Config) -> None:
        super().__init__()

        self.config = config
        self.protocols = protocols.SupportedProtocolFactory()

    def run(self) -> None:
        if not itc.IS_WORKER_RUNNING.is_set():
            raise exceptions.WaveshareException("Event 'IS_WORKER_RUNNING' is not set.")

        # TODO: initialize serial object and SIM868
        self.comm_port = serial.Serial(self.config.serial_port, self.config.baud_rate)
        self.comm_port.open()

        WORKER_STATE_MAPPING: typing.Dict[
            WorkerState, typing.Callable[..., typing.Any]
        ] = {
            WorkerState.START: self.on_start,
            WorkerState.LISTEN_TO_CLIENT: self.on_listen_to_client,
            WorkerState.LISTEN_TO_SERIAL: self.on_listen_to_serial,
        }

        curr_state: typing.Optional[WorkerState] = WorkerState.START
        next_state: typing.Optional[WorkerState] = None

        while itc.IS_WORKER_RUNNING.is_set():
            self.logger.debug(f"Current State: {curr_state}")
            if curr_state is None:
                break
            next_state = WORKER_STATE_MAPPING[curr_state]()
            curr_state = next_state

    def on_start(self) -> WorkerState:
        # TODO: initialize all enabled protocols

        with itc.ACQUIRE_CLIENT_TX_DATA:
            if itc.CLIENT_TX_Q.qsize() > 0:
                self.logger.debug("Client TX data available!")
                return WorkerState.LISTEN_TO_CLIENT

        with itc.ACQUIRE_SERIAL_RX_DATA:
            if itc.SERIAL_RX_Q.qsize() > 0:
                self.logger.debug("Serial RX data available!")
                return WorkerState.LISTEN_TO_SERIAL

        self.logger.debug("No data available :(")
        return WorkerState.START

    def on_listen_to_client(self) -> WorkerState:
        return WorkerState.START

    def on_listen_to_serial(self) -> WorkerState:
        return WorkerState.START
