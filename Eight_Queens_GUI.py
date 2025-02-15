import tkinter as tk
from tkinter import messagebox

class EightQueensGUI:
    def __init__(self, root, EightQueens, positions):
        self.root = root
        self.EightQueens = EightQueens
        self.positions = positions
        self.current_position_index = 0
        self.cells = [[None for _ in range(8)] for _ in range(8)]

        self.start = self.positions[0]
        self.goal = self.positions[-1]
        self.showing_goal = False  # Track if the goal is currently being shown

        self.root.title("Eight Queens Problem")
        self.create_widgets()

    def create_widgets(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(padx=10, pady=10)

        # Initialize the chessboard grid (8x8)
        self.initialize_board()

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        self.prev_button = tk.Button(self.control_frame, text="Previous State", command=self.previous_state)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(self.control_frame, text="Next State", command=self.next_state)
        self.next_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.show_goal_button = tk.Button(self.control_frame, text="Show Goal", command=self.show_goal)
        self.show_goal_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.hide_goal_button = tk.Button(self.control_frame, text="Hide Goal", command=self.hide_goal, state=tk.DISABLED)
        self.hide_goal_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.update_board(self.start)

        # Set the window size
        self.root.geometry("500x500")

    def initialize_board(self):
        """Initialize the 8x8 grid of cells."""
        for row in range(8):
            for col in range(8):
                cell = tk.Label(
                    self.grid_frame,
                    text="",
                    width=4,
                    height=2,
                    bg="white" if (row + col) % 2 == 0 else "gray",
                    relief=tk.RAISED,
                    borderwidth=2
                )
                cell.grid(row=row, column=col)
                self.cells[row][col] = cell

    def update_board(self, state):
        """Update the board to reflect the current state of queens."""
        for row in range(8):
            for col in range(8):
                if state[row] == col:
                    self.cells[row][col]["text"] = "Q"
                else:
                    self.cells[row][col]["text"] = ""

    def previous_state(self):
        """Move to the previous state and update the board."""
        if not self.showing_goal:  # Allow navigation only if not showing the goal
            if self.current_position_index > 0:
                self.current_position_index -= 1
                self.update_board(self.positions[self.current_position_index])
            else:
                messagebox.showinfo("Info", "This is the first state!")
        else:
            messagebox.showinfo("Info", "Hide the goal to navigate states.")

    def next_state(self):
        """Move to the next state and update the board."""
        if not self.showing_goal:  # Allow navigation only if not showing the goal
            if self.current_position_index < len(self.positions) - 1:
                self.current_position_index += 1
                self.update_board(self.positions[self.current_position_index])
            else:
                messagebox.showinfo("Info", "No more states!")
        else:
            messagebox.showinfo("Info", "Hide the goal to navigate states.")

    def show_goal(self):
        """Display the goal state on the board."""
        self.update_board(self.goal)
        self.showing_goal = True
        self.show_goal_button.config(state=tk.DISABLED)
        self.hide_goal_button.config(state=tk.NORMAL)

    def hide_goal(self):
        """Return to the current state from the goal."""
        self.update_board(self.positions[self.current_position_index])
        self.showing_goal = False
        self.show_goal_button.config(state=tk.NORMAL)
        self.hide_goal_button.config(state=tk.DISABLED)

def GUI(EightQueens, positions, extra_text=""):
    if positions:
        root = tk.Tk()
        app = EightQueensGUI(root, EightQueens, positions)
        root.mainloop()
    else:
        print("No path found")