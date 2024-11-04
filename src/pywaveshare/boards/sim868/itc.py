from __future__ import annotations

import queue
import threading

IS_WORKER_RUNNING = threading.Event()

ACQUIRE_CLIENT_TX_DATA = threading.Lock()
ACQUIRE_SERIAL_RX_DATA = threading.Lock()

CLIENT_TX_Q: queue.Queue[bytes] = queue.Queue()
SERIAL_RX_Q: queue.Queue[bytes] = queue.Queue()
SERIAL_TX_Q: queue.Queue[bytes] = queue.Queue()
