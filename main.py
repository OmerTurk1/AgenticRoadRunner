from classes import *
import joblib
import time

def main(player):
    agent = Agent("MyAgent", model=joblib.load("agent_model.pkl"))
    map = Map(seed=42, agent=agent, map_size=17)
    while not map.is_reached_goal():
        map.display()
        agent.observe(map)
        candidate_actions = agent.take_action(player) # from big probability to small probability
        selected_action = None
        for idx, action in enumerate(candidate_actions):
            print(f"{idx}: {action}")
            if map.is_appropriate_action(action):
                selected_action = action
                break
        map.update_agent_position(selected_action)
        if player=="ai":
            print("-----------------------------")
            time.sleep(1)

    if player=="user":
        agent.save_log("agent_moves.csv")
    print("finished")

if __name__ == "__main__":
    main("ai")