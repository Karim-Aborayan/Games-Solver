# Game Solver

## Overview
**Game Solver** is a Python-based project that implements various search algorithms to solve two distinct problems:

1️⃣ **Maze Pathfinding** - Find the optimal path from the start to the goal in a randomly generated maze.
2️⃣ **Eight Queens Puzzle** - Arrange 8 queens on a chessboard so that no two queens threaten each other.

The project supports **multiple search algorithms** and allows users to choose between **CLI (Command Line Interface) and GUI (Graphical User Interface).**

---

## 📂 Project Structure
```
game-solver/
│── Algorithms/
│   ├── Alpha_Beta.py
│   ├── BestFirstSearch.py
│   ├── BidirectionalSearch.py
│   ├── DLS.py
│   ├── HillClimbing.py
│   ├── IDS.py
│   ├── Minimax.py
│
│── Interfaces/
│   ├── Maze_CLI.py
│   ├── Maze_GUI.py
│   ├── Eight_Queens_CLI.py
│   ├── Eight_Queens_GUI.py
│
│── Problems/
│   ├── Maze.py
│   ├── Eight_Queens.py
│
│── main.py  # Main entry point of the project
│── README.md  # Documentation
```

---

## How It Works
The program starts by running `main.py`, which asks the user for input to:

1️⃣ **Choose an Interface:**
   - `1` → CLI (Command Line Interface)
   - `2` → GUI (Graphical User Interface)

2️⃣ **Select a Problem:**
   - `1` → Maze Pathfinding
   - `2` → Eight Queens Puzzle

3️⃣ **Pick an Algorithm:**
   - `1` → Depth Limited Search (DLS)
   - `2` → Iterative Deepening Search (IDS)
   - `3` → Best-First Search
   - `4` → Hill Climbing
   - `5` → Bidirectional Search
   - `6` → Minimax (for game-based problems)
   - `7` → Alpha-Beta Pruning (optimized Minimax)

Once the choices are made, the corresponding problem, interface, and algorithm are loaded dynamically, and the solution process begins.

---

## 🛠 Installation & Requirements
This project **does not require any external dependencies**—it runs using Python’s built-in modules. Just make sure you have **Python 3.x** installed.

### To Run the Project:
1. Clone the repository:
   ```sh
   git clone https://github.com/Karim-Aborayan/game-solver.git
   ```
2. Navigate to the project directory:
   ```sh
   cd game-solver
   ```
3. Run the program:
   ```sh
   python main.py
   ```
4. Follow the on-screen prompts to select a problem, algorithm, and interface.

---

## Algorithms Implemented
| Algorithm | Type | Description |
|-----------|------|-------------|
| **Depth Limited Search (DLS)** | Uninformed | Searches to a fixed depth limit. |
| **Iterative Deepening Search (IDS)** | Uninformed | Combines DFS & BFS for optimal solutions. |
| **Best-First Search** | Informed | Uses heuristics to expand the most promising node. |
| **Hill Climbing** | Informed | A greedy approach that moves toward the best state. |
| **Bidirectional Search** | Informed | Searches forward from the start and backward from the goal. |
| **Minimax** | Game AI | Evaluates optimal moves for adversarial games. |
| **Alpha-Beta Pruning** | Game AI | Optimized Minimax that reduces unnecessary evaluations. |

---

## Interfaces (CLI & GUI)
The project offers two interfaces for user interaction:
- **CLI (Command Line Interface)** → Displays textual outputs.
- **GUI (Graphical User Interface)** → Uses Tkinter to visualize solutions.

The Maze problem is visualized in a **grid format**, while the Eight Queens puzzle is displayed as a **chessboard layout**.

---

## Example Runs
### **Maze Pathfinding (GUI Example)**
```
Interfaces:
1) CLI
2) GUI
Choose Interface: 2

Problems:
1) Maze
2) 8 Queens
Choose Problem: 1

Algorithms:
1) Depth Limited Search
2) Iterative Deepening Search
3) Best First Search
4) Hill Climbing
5) Bidirectional Search
6) MinMax
7) Alpha-Beta
Choose Algorithm: 3
```
- The program generates a **random maze** and solves it using Best-First Search.
- Since GUI is selected, it will **visualize the maze** with next move and previous move buttons to go through the solution path.

### **Eight Queens (CLI Example)**
```
Interfaces:
1) CLI
2) GUI
Choose Interface: 1

Problems:
1) Maze
2) 8 Queens
Choose Problem: 2

Algorithms:
1) Depth Limited Search
2) Iterative Deepening Search
3) Best First Search
4) Hill Climbing
5) Bidirectional Search
6) MinMax
7) Alpha-Beta
Choose Algorithm: 4
```
- The program initializes a random chessboard and solves it using **Hill Climbing**.
- If CLI is selected, it **prints the board state** step by step.

---

## Future Improvements
- Support for additional games (e.g., **Sudoku Solver, N-Queens**)  
- More advanced AI algorithms (e.g., **Genetic Algorithms**)
- Enhanced GUI with better **animations & interactivity**
