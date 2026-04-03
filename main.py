from classes import *
from sklearn.naive_bayes import GaussianNB

def main():
    agent = Agent("MyAgent", model=GaussianNB())
    map = Map(seed=42, agent=agent, map_size=17)
    while not map.is_reached_goal():
        map.display()
        agent.observe(map)
        candidate_action = agent.new_action("user")
        map.update_agent_position(candidate_action)
        print(agent.location)

    agent.save_log("agent_moves.csv")
    print("finished")

if __name__ == "__main__":
    main()