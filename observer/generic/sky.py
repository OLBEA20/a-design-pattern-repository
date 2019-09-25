from generic.obersvable import Observable


class Sky(Observable[str]):
    def __init__(self, humidity_level: int):
        super().__init__()
        self._status = "VALVE_OPEN"
        self.update_status(humidity_level)

    def update_status(self, water_level: int) -> None:
        status = "CLOUDY" if water_level > 50 else "SUNNY"
        if status != self.status:
            self.status = status
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status: str) -> None:
        self._status = status
        self.notify_observers(self._status)