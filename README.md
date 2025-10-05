# 8-Puzzle Solver 🧩

This repository contains a **Python-based implementation of the classic 8-Puzzle Problem**.  
The project demonstrates the application of **Artificial Intelligence (AI) search algorithms** to solve puzzles optimally, comparing efficiency and performance across different techniques.

---

## 📌 What this project does
- Solves the **8-puzzle sliding tile problem** by moving tiles into the correct order.  
- Supports **two AI search algorithms**:
  - **Iterative Deepening Search (IDS)** → explores nodes layer by layer with depth-limited DFS, guaranteeing optimal solutions.  
  - **Bidirectional Search** → searches simultaneously from start and goal, meeting in the middle to reduce search space.  
- Provides:
  - **Custom puzzle input** (user enters tiles manually).  
  - **Random solvable puzzle generator** using inversion parity check.  
  - **Step-by-step move sequence** from start state to goal state.  
  - **Performance metrics** such as number of nodes expanded.  

---

## 🛠️ Tech Stack & Tools Used
- **Language:** Python 3 (core language of the implementation).  
- **Python Standard Libraries:**
  - `random` → for generating and shuffling random puzzle states.  
  - `collections.deque` → for implementing efficient BFS queues in Bidirectional Search.  
- **Data Structures:**
  - **Tuples** → represent puzzle states in a hashable form for fast lookup.  
  - **Lists** → store states and move sequences.  
  - **Sets & Dictionaries** → track visited states and avoid duplicate exploration.  
- **Algorithms Implemented:**
  - *Inversion Parity Check* → ensures only solvable puzzles are considered.  
  - *Depth-Limited Search (DLS)* → recursive DFS restricted by depth.  
  - *Iterative Deepening Search (IDS)* → combination of DFS and BFS principles.  
  - *Bidirectional Search* → parallel search from start and goal states.  

---

## 🧑‍💻 Skills Demonstrated
- **Artificial Intelligence Concepts:** Search strategies, state space representation, solvability conditions.  
- **Algorithm Design & Analysis:** Implemented and compared different search algorithms.  
- **Problem-Solving & Optimization:** Reduced redundant exploration with hashing and pruning.  
- **Software Development Practices:** Modular functions, structured code, clear separation of concerns.  
- **Python Proficiency:** Efficient use of built-in libraries (`random`, `collections`) and data structures.  
- **Debugging & Testing:** Verified with both random and user-input puzzles for correctness.  

---

## 🚀 Why this project is useful
- Shows **practical application of AI search algorithms** on a classic problem.  
- Demonstrates **trade-offs between IDS and Bidirectional Search** (time vs memory).  
- Provides a clean, easy-to-understand Python implementation with **no external dependencies**.  
- Can be extended for research, teaching, or learning purposes in AI and search algorithms.  
