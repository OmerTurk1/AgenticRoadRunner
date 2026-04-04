# Agentic Road Runner

This project explores an interactive route-finding agent that moves toward a goal on a generated grid map while logging state-action data for later analysis.

## Overview

The codebase includes:
- a generated map with random obstacles,
- an agent that observes nearby tiles and goal direction,
- an interactive loop for choosing moves,
- logging of move states and actions to `agent_moves.csv`,
- analysis and visualization scripts for the collected data.

## Scripts

### `classes.py`
- Defines the `Agent` and `Map` classes.
- `Agent` builds a state from the 8 surrounding tiles plus the normalized goal direction vector.
- The agent tracks location, current observation, and move history.
- `Map` generates a square board, places obstacles, and validates each move.
- Valid moves update the board and agent position; invalid moves are blocked and penalized.

### `main.py`
- Creates a reproducible map using a fixed seed.
- Runs an interactive loop until the agent reaches the goal.
- Displays the map, observes the current state, receives user actions, updates position, and logs each move.
- Saves the collected move data to `agent_moves.csv` at the end.

### `read_data.py`
- Loads `agent_moves.csv` with `pandas`.
- Prints dataset shape, sample rows, and counts of each action.
- Shows average feature values for each action to help understand how moves relate to goal direction and nearby tiles.

### `visualize_data.py`
- Loads `agent_moves.csv` and creates scatter plots of goal direction for each move.
- Saves the result as `action_scatter_plots.png`.
- Helps visualize which direction patterns correspond to each action.

## Data

`agent_moves.csv` contains:
- `tile_0` through `tile_7`: surrounding tile values,
- `dir_row`, `dir_col`: normalized direction to the goal,
- `action`: the chosen move (`w`, `a`, `s`, `d`).

## How to run

1. Install dependencies:
   - `pandas`
   - `numpy`
   - `scikit-learn`
   - `matplotlib`
   - `seaborn`
2. Run the interactive script:
   - `python main.py`
3. Analyze collected data:
   - `python read_data.py`
4. Generate visualizations:
   - `python visualize_data.py`

## Goal

The main aim is to collect human-controlled move data and use it to understand or train an autonomous route-finding agent.