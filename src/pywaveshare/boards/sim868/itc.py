from __future__ import annotations

import queue
import threading

IS_WORKER_RUNNING = threading.Event()

SERIAL_LOCK = threading.Lock()
C2W_Q_LOCK = threading.Lock()
"""
If acquired, then the acquirer can to safely work on `CLIENT_TO_WORKER_Q` queue.
"""

CLIENT_TO_WORKER_Q: queue.Queue[bytes] = queue.Queue()
WORKER_TO_SERIAL_Q: queue.Queue[bytes] = queue.Queue()
SERIAL_TO_WORKER_Q: queue.Queue[bytes] = queue.Queue()
