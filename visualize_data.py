import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("agent_moves.csv")

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for action, ax in zip(df["action"].unique(), axs.flat):
    curr_df = df[df["action"] == action]
    other_df = df[df["action"] != action]
    ax.scatter(curr_df["dir_col"], -curr_df["dir_row"], color="orange", alpha=0.6)
    ax.scatter(other_df["dir_col"], -other_df["dir_row"], color="gray", alpha=0.2)
    ax.set_title(f"Action: {action}")
    ax.set_xlabel("dir_col")
    ax.set_ylabel("dir_row")

plt.tight_layout()
plt.savefig("action_scatter_plots.png")
plt.show()