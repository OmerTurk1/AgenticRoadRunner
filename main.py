from classes import *
import joblib
import time

def main(player):
    agent = Agent("MyAgent", model=joblib.load("agent_model.pkl"))
    map = Map(seed=42, agent=agent, map_size=17)
    while not map.is_reached_goal():
        map.display()
        agent.observe(map)
        candidate_action = agent.new_action(player)
        map.update_agent_position(candidate_action)
        if player=="ai":
            print("-----------------------------")
            time.sleep(1)

    if player=="user":
        agent.save_log("agent_moves.csv")
    print("finished")

if __name__ == "__main__":
    main("user")