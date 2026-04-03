import random
import pandas as pd
import numpy as np

moves={
    "w": (-1, 0), # up
    "a": (0, -1), # left
    "s": (1, 0), # down
    "d": (0, 1) # right
}

class Agent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.state = None
        self.location = []
        self.move_list = []

    def train(self, X, y):
        self.model.fit(X, y)

    def new_action(self, mode="ai"):
        while True:
            if mode == "ai":
                action = self.model.predict(self.state)[0]
            else:
                action = input("Enter your action: ")

            if action in moves: # control for user
                self.log(action)
                break
        return action

    def get_direction(self, goal_location):
        row_diff = goal_location[0] - self.location[0]
        col_diff = goal_location[1] - self.location[1]
        direction = np.array([row_diff, col_diff])
        unit_dir = np.round(direction / np.linalg.norm(direction), decimals=4)
        return unit_dir

    def observe(self,map):
        tiles = map.tiles
        counter = 0
        observation = []
        for i in (-1,0,1):
            for j in (-1,0,1):
                if i == 0 and j == 0:
                    continue
                row = self.location[0] + i
                col = self.location[1] + j
                if 0 <= row < map.map_size and 0 <= col < map.map_size:
                    observation.append(tiles[row][col]) # 0 for empty, 1 for wall, 2 for agent, 3 for goal
                else:
                    observation.append(1) # outside the map is considered wall
                counter += 1
        dir_vec = self.get_direction(map.goal_location)
        observation.extend([dir_vec[0], dir_vec[1]])
        cols = [f"tile_{i}" for i in range(counter)] + ["dir_row", "dir_col"]
        self.state = pd.DataFrame([observation], columns=cols)
        return self.state

    def log(self, action):
        new_entry = self.state.copy()
        new_entry["action"] = action
        self.move_list.append(new_entry)

    def save_log(self, filename):
        if self.move_list:
            final_df = pd.concat([pd.read_csv(filename)] + self.move_list, ignore_index=True)
            final_df.to_csv(filename, index=False)
            print(f"Log Saved: {filename}")

class Map:
    def __init__(self, seed, agent, map_size=15):
        """0: empty tile, 1:wall, 2:agent, 3:goal"""
        self.agent = agent
        self.seed = seed
        self.name = f"Map_{seed}"
        self.map_size = map_size
        self.goal_location = [random.randint(0, self.map_size - 1), random.randint(0, self.map_size - 1)]
        self.agent.location = [random.randint(0, self.map_size - 1), random.randint(0, self.map_size - 1)] # start location
        self.tiles = []
        self.generate()

    def generate(self):
        print(f"Generating {self.name} with seed: {self.seed}")
        random.seed(self.seed)

        # Zemin oluştur
        self.tiles = [[0 for _ in range(self.map_size)] for _ in range(self.map_size)]

        # Duvar oranı
        obstacle_density = 0.2
        obstacle_count = int(self.map_size * self.map_size * obstacle_density)

        placed = 0
        while placed < obstacle_count:
            row = random.randint(0, self.map_size - 1)
            col = random.randint(0, self.map_size - 1)
            if (row, col) == self.goal_location or (row, col) == self.agent.location:
                continue
            if self.tiles[row][col] == 0:
                self.tiles[row][col] = 1
                placed += 1

        # Agent ve hedefi yerleştir
        ax, ay = self.agent.location
        gx, gy = self.goal_location
        self.tiles[ax][ay] = 2
        self.tiles[gx][gy] = 3

    def update_agent_position(self, action_taken):
        old_x, old_y = self.agent.location
        move_x, move_y = moves[action_taken]
        new_x = old_x + move_x
        new_y = old_y + move_y

        if 0 <= new_x < self.map_size and 0 <= new_y < self.map_size and self.tiles[new_x][new_y] != 1:
            self.tiles[old_x][old_y] = 0
            self.tiles[new_x][new_y] = 2
            self.agent.location = [new_x, new_y]
            print("Reward: -1")
        else:
            print("Invalid move. Reward: -20")

    def display(self):
        symbol_map = {0: '.', 1: '#', 2: 'A', 3: 'G'}
        for row_id in range(self.map_size):
            print(' '.join(symbol_map[self.tiles[row_id][col_id]] for col_id in range(self.map_size)))
        return self.tiles

    def is_reached_goal(self):
        return self.agent.location == self.goal_location