import pandas as pd

df = pd.read_csv("agent_moves.csv")

print("Data Shape:")
print(df.shape,"\n")

print("Agent Move Log:")
print(df.head(),"\n")

print("Counts of Unique Actions:")
print(df["action"].value_counts(),"\n")

for action in df["action"].unique():
    action_df = df[df["action"] == action]
    print(f"{action} move averages:")
    print(action_df.drop(columns="action").mean())