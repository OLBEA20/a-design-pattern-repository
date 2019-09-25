from random import randint, random
import time

from generic.display.graphical_health_status import GraphicalHealthStatus
from generic.display.health_alert import HealthAlert
from generic.display.sky_status import SkyStatus
from generic.player import Player
from generic.sky import Sky


def destined_to_happen(probability: float = 0.5):
    return random() < probability

def play(player: Player, sky: Sky,duration: int):
    for _ in range(duration):
        if destined_to_happen():
            player.take_damage(randint(1, 3))
        if destined_to_happen(1/3):
            player.recover(randint(1, 2))
        
        sky.update_status(randint(0, 100))

        time.sleep(1)

if __name__ == "__main__":
    health_status = HealthAlert(6)
    player_health = 10
    health_bar = GraphicalHealthStatus(10)
    player = Player(player_health)

    player.subscribe(health_status)
    player.subscribe(health_bar)

    sky_status = SkyStatus()
    sky = Sky(randint(0,100))
    sky.subscribe(sky_status)

    """
    Uncomment and run a type-checker against this file to test Generics mechanism.
    """
    # sky.subscribe(health_bar)
    # player.subscribe(sky_status)

    play(player, sky, 20)
