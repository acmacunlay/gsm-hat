import queue
import threading

IS_WORKER_RUNNING = threading.Event()

ACQUIRE_SERIAL_OBJECT = threading.Lock()

ON_SERIAL_RX: queue.Queue[bytes] = queue.Queue()
ON_SERIAL_TX: queue.Queue[bytes] = queue.Queue()
