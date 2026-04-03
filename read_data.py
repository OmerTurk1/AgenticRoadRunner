import pandas as pd

df = pd.read_csv("agent_moves.csv")

print("Data Shape:")
print(df.shape,"\n")

print("Agent Move Log:")
print(df.head(),"\n")

print("Counts of Actions Taken:")
print(df["action"].value_counts(),"\n")

