from classes import *
from sklearn.linear_model import LogisticRegression

def main():
    agent = Agent("MyAgent", model=LogisticRegression())
    map = Map(seed=42, agent=agent)
    print(map.display())
    print(agent.observe(map))
    print(agent.act("user"))
    print(agent.location)

    # agent.save_log("agent_moves.csv")

if __name__ == "__main__":
    main()