import tkinter as tk
from tkinter import messagebox

class MazeGUI:
    def __init__(self, root, Maze, positions):
        self.root = root
        self.maze = Maze.maze
        self.positions = positions
        self.current_position_index = 0
        self.text_ids = {}
        self.start = Maze.start
        self.goal = Maze.goal

        self.root.title("Maze Solver")
        self.create_widgets()

    def create_widgets(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(padx=10, pady=10)

        grid_rows, grid_cols = len(self.maze), len(self.maze[0])
        cell_size_x, cell_size_y = 53, 53
        window_width, window_height = cell_size_x * grid_cols, cell_size_y * grid_rows
        cell_size = min(cell_size_x, cell_size_y)

        self.canvas = tk.Canvas(self.grid_frame, width=window_width, height=window_height)
        self.canvas.pack()

        self.cell_rectangles = {}
        for i in range(grid_rows):
            for j in range(grid_cols):
                x1, y1, x2, y2 = j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray", fill="white")
                self.cell_rectangles[(i, j)] = rect

        self.prev_button = tk.Button(self.root, text="Previous Move", command=self.previous_move)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(self.root, text="Next Move", command=self.next_move)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.update_grid(self.maze)

        window_width = grid_cols * cell_size + 50
        window_height = grid_rows * cell_size + 150
        self.root.geometry(f"{window_width}x{window_height}")

    def update_grid(self, state):
        for (x, y), text_id in list(self.text_ids.items()):
            if self.text_ids.get((x, y)) and (x, y) != self.positions[self.current_position_index]:
                self.canvas.delete(text_id)
                del self.text_ids[(x, y)]

        for i in range(len(state)):
            for j in range(len(state[0])):
                rect = self.cell_rectangles[(i, j)]
                self.canvas.itemconfig(rect, fill="black" if state[i][j] == 1 else "white")

        start_x, start_y = self.start.get_state()
        goal_x, goal_y = self.goal.get_state()
        self.mark_position(start_x, start_y, "green", "S")
        self.mark_position(goal_x, goal_y, "red", "G")

        for i in range(self.current_position_index + 1):
            path_x, path_y = self.positions[i]
            if (path_x, path_y) != (start_x, start_y) and (path_x, path_y) != (goal_x, goal_y):
                self.mark_position(path_x, path_y, "blue", "")

        current_x, current_y = self.positions[self.current_position_index]
        if (current_x, current_y) != (start_x, start_y) and (current_x, current_y) != (goal_x, goal_y):
            self.mark_position(current_x, current_y, "blue", "P")

    def mark_position(self, x, y, color, text):
        rect = self.cell_rectangles[(x, y)]
        self.canvas.itemconfig(rect, fill=color)
        text_id = self.canvas.create_text((y * 53) + 26, (x * 53) + 26, text=text, fill="white", font=("Helvetica", 12))
        self.text_ids[(x, y)] = text_id

    def next_move(self):
        if self.current_position_index < len(self.positions) - 1:
            self.current_position_index += 1
            self.update_grid(self.maze)
        else:
            messagebox.showinfo("Info", "No more moves!")

    def previous_move(self):
        if self.current_position_index > 0:
            self.current_position_index -= 1
            self.update_grid(self.maze)
        else:
            messagebox.showinfo("Info", "This is the first move!")

def GUI(Maze, positions, extra_text=""):
    if positions:
        root = tk.Tk()
        app = MazeGUI(root, Maze, positions)
        root.mainloop()
    else:
        print("No path found")