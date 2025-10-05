8-Puzzle Solver (Iterative Deepening Search & Bidirectional Search)
📌 Project Overview

This project is an implementation of the classic 8-puzzle problem solver in Python.
It demonstrates the use of search algorithms in Artificial Intelligence, namely:

Iterative Deepening Search (IDS)

Bidirectional Search

The program can either generate a random solvable puzzle or accept a custom puzzle from the user.
It then applies search strategies to find the optimal sequence of moves from the start state to the goal state.

🛠️ Tech Stack & Skills Used
🔹 Programming Language

Python 3: Core language used for implementing the solver.

Reason: Python provides clean syntax, built-in data structures, and powerful libraries for handling search problems.

🔹 Python Standard Libraries

random:

Used for shuffling tiles and generating random puzzle configurations.

Ensures only solvable puzzles are considered using inversion parity check.

collections.deque:

Provides an efficient queue structure.

Used in Bidirectional Search for BFS-like expansion from both directions.

🔹 Algorithms & AI Concepts

Inversion Parity Check:

Determines if a given puzzle configuration is solvable.

Depth-Limited Search (DLS):

A DFS-based recursive search that stops when the depth limit is reached.

Iterative Deepening Search (IDS):

Combines DFS and BFS principles.

Runs multiple depth-limited searches with increasing limits until the goal is found.

Guarantees optimal solution while using less memory than BFS.

Bidirectional Search:

Runs search simultaneously from the start and goal states.

When the two frontiers meet, a solution path is constructed.

Much more efficient in terms of nodes expanded.

🔹 Data Structures

Tuples:

Used to represent puzzle states in a hashable format for fast lookup.

Sets & Dictionaries:

Used for storing visited states to avoid repeated exploration.

Lists:

Used for storing sequences of moves (solution path).

🔹 Problem-Solving & Software Skills

Algorithm Design & Analysis: Applied different AI search algorithms and compared performance.

Optimization: Reduced redundant state exploration by using hashing & pruning.

Clean Coding Practices: Modular functions (state management, solvability check, printing, searching).

Debugging & Testing: Verified correctness with both random and custom puzzles.
