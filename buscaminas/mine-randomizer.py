# Package import
import random


mine_spawn = ([0, 1, 0], [0, 1, 1], [0, 0, 1]) # Saves mine spawn (static)
difficulty = 1  # Set default difficulty to 1


def getMineSpawn(difficulty):
    spawn_limit = difficulty * 20 + random.randint(1,10)
    return spawn_limit

def iteration(mine_spawn):
    for spawn_list in mine_spawn:
        for spawn_point in spawn_list:
            print(spawn_point)
        print()


print(iteration(mine_spawn))
print(getMineSpawn(1))