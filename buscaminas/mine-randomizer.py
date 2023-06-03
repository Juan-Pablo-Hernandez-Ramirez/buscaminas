# Package import
import random

columns = 3
map_row = [[]]*columns # Saves mine spawn (static)
difficulty = 1  # Set default difficulty to 1


def get_mine_cap(difficulty):
    spawn_limit = difficulty * 20 + random.randint(1,10)
    return spawn_limit

def mine_mapping(map_row):
    global columns
    for i in range(int(len(map_row)/columns)):
        for inner_list in range(len(map_row)):
            map_row[inner_list].append(1)
        print(map_row)

for i in range(columns):
    print(mine_mapping(map_row))

# map_row[0].append(1)
# print(map_row)