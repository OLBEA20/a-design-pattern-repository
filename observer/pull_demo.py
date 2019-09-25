import time
from random import randint, random

from pull.health_status.graphical_health_status import GraphicalHealthStatus
from pull.health_status.text_health_status import TextHealthStatus
from pull.player import Player


def destined_to_happen(probability: float = 0.5):
    return random() < probability

def play(player: Player, duration: int):
    for _ in range(duration):
        if destined_to_happen():
            player.take_damage(randint(1, 3))
        if destined_to_happen(1/3):
            player.recover(randint(1, 2))

        time.sleep(1)

if __name__ == "__main__":
    player_health = 10
    player = Player(player_health)
    health_status = TextHealthStatus(player)
    health_bar = GraphicalHealthStatus(player)

    player.subscribe(health_status)
    player.subscribe(health_bar)

    play(player, 20)
