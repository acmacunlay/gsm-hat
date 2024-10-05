class Config:
    def __init__(self, serial_port: str, baud_rate: int, encoding: str) -> None:
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.encoding = encoding
