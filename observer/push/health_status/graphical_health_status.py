from push.observer import Observer

class GraphicalHealthStatus(Observer):
    def __init__(self, inital_health: int):
        self.inital_health = inital_health

    def notify(self, player_health: int) -> None:
        print(f"[{player_health * 'x'}{(self.inital_health - player_health) * ' '}]")
