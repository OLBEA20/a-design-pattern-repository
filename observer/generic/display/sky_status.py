from generic.observer import Observer


class SkyStatus(Observer[str]):
    def notify(self, status: str):
        print(25*"-")
        print(f"Sky status: {status}")
        print(25*"-")