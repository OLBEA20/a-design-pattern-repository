from push.observer import Observer


class TextHealthStatus(Observer):
    def notify(self, player_health: int) -> None:
        print(f"Health: {player_health}")
