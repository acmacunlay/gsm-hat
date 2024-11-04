import enum
import threading
import typing

import serial

from . import config, exceptions, itc, protocols


class WorkerState(enum.Enum):
    STARTUP = 0x00
    RESTART = 0x01
    SHUTDOWN = 0x02
    LISTEN_TO_SOURCES = 0x03
    LISTEN_TO_CLIENT = 0x04
    LISTEN_TO_SERIAL = 0x05


class Worker(threading.Thread):
    logger = config.get_logger("worker")

    def __init__(self, config: config.Config) -> None:
        super().__init__(daemon=True)

        self.config = config
        self.protocols = protocols.get_enabled_protocols(self.config)
        self.comm_port = serial.Serial(self.config.serial_port, self.config.baud_rate)

    def run(self) -> None:
        if not itc.IS_WORKER_RUNNING.is_set():
            raise exceptions.WaveshareException("Event 'IS_WORKER_RUNNING' is not set.")

        WORKER_STATE_MAPPING: typing.Dict[
            WorkerState, typing.Callable[..., typing.Union[WorkerState, None]]
        ] = {
            WorkerState.STARTUP: self.on_startup,
            WorkerState.RESTART: self.on_restart,
            WorkerState.SHUTDOWN: self.on_shutdown,
            WorkerState.LISTEN_TO_SOURCES: self.on_listen_to_sources,
            WorkerState.LISTEN_TO_CLIENT: self.on_listen_to_client,
            WorkerState.LISTEN_TO_SERIAL: self.on_listen_to_serial,
        }

        curr_state: typing.Optional[WorkerState] = WorkerState.STARTUP
        next_state: typing.Optional[WorkerState] = None

        while itc.IS_WORKER_RUNNING.is_set():
            self.logger.debug(f"Current State: {curr_state}")
            if curr_state is None:
                break
            next_state = WORKER_STATE_MAPPING[curr_state]()
            curr_state = next_state

    def on_startup(self) -> WorkerState:
        self.comm_port.open()
        # TODO: initialize all enabled protocols
        return WorkerState.LISTEN_TO_SOURCES

    def on_restart(self) -> WorkerState:
        return WorkerState.STARTUP

    def on_shutdown(self) -> None:
        return None

    def on_listen_to_sources(self) -> WorkerState:
        with itc.ACQUIRE_CLIENT_TX_DATA:
            if self.is_client_data_available():
                self.logger.debug("Client TX data available!")
                return WorkerState.LISTEN_TO_CLIENT

        with itc.ACQUIRE_SERIAL_RX_DATA:
            if self.is_serial_data_available():
                self.logger.debug("Serial RX data available!")
                return WorkerState.LISTEN_TO_SERIAL

        self.logger.debug("No data available :( Rechecking sources...")
        return WorkerState.LISTEN_TO_SOURCES

    def is_client_data_available(self) -> bool:
        return itc.CLIENT_TX_Q.qsize() > 0

    def on_listen_to_client(self) -> WorkerState:
        return WorkerState.LISTEN_TO_SOURCES

    def is_serial_data_available(self) -> bool:
        return itc.SERIAL_RX_Q.qsize() > 0

    def on_listen_to_serial(self) -> WorkerState:
        return WorkerState.LISTEN_TO_SOURCES
