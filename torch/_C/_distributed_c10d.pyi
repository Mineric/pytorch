from typing import Optional
from datetime import timedelta

class FileStore:
    def __init__(
        self,
        path: str,
        numWorkers: int
    ): ...
class TCPStore:
    def __init__(
        self,
        masterAddr: Optional[str],
        masterPort: int,
        numWorkers: int,
        isServer: bool,
        timeout: timedelta
    ): ...