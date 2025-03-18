from random import randint, choice, random, shuffle
from math import ceil

class Maze:
  start, goal, maze, rows, cols = None, None, None, None, None
  def __init__(self, position):
    self.state = position
  
  @classmethod
  def generate_problem(cls):
    cls.rows = randint(5,10)
    cls.cols = randint(5, 7) if cls.rows < 8 else randint(8, 10)
    Maze._initialize_maze()
    Maze._create_path()
    Maze._finalize_maze()
    return cls.start, cls.goal, cls.maze
    
  @classmethod
  def _initialize_maze(cls):
    start_position_randomizer = randint(0,1)
    starti = randint(0, ceil(cls.rows/2)-2) * start_position_randomizer
    startj = randint(0, ceil(cls.cols/2)-2) * (1 - start_position_randomizer)
  
    goal_position_randomizer = randint(0,1)
    goali = cls.rows-1 if goal_position_randomizer == 0 else randint(cls.rows - (ceil(cls.rows/2)-1), cls.rows-1)
    goalj = cls.cols-1 if goal_position_randomizer == 1 else randint(cls.cols - (ceil(cls.cols/2)-1), cls.cols-1)
  
    cls.start = Maze((starti, startj))
    cls.goal = Maze((goali, goalj))
    cls.maze = [[0 if (i,j) == cls.start.state or (i,j) == cls.goal.state else "" for j in range(cls.cols)] for i in range(cls.rows)]
  
  @classmethod
  def _create_path(cls):
    prev_middles = []
    first, second = None, cls.start
    for _ in range(ceil(min(cls.rows, cls.cols)/2)-1):
      first = second
      second = Maze(choice([(i,j) for i in range(cls.rows) for j in range(cls.cols) if (i,j) not in [cls.start.state, cls.goal.state] + prev_middles]))
      prev_middles.append(second.state)
      Maze._create_middle_path(first, second, first.manhattan_distance(second))
    first = second
    second = cls.goal
    Maze._create_middle_path(first, second, first.manhattan_distance(second))
  
  @classmethod
  def _create_middle_path(cls, first, second, current_distance):
    if first.state == second.state:
      return
    moves = []
    for neighbour in first.generate_neighbours(randomize=True):
      temp = neighbour.manhattan_distance(second)
      if temp < current_distance:
        current_distance = temp
        moves.append(neighbour)
    if moves:
      next_move = choice(moves)
      i,j = next_move.state
      cls.maze[i][j] = 0
      Maze._create_middle_path(next_move, second, current_distance)
  
  @classmethod
  def _finalize_maze(cls):
    for i in range(cls.rows):
      for j in range(cls.cols):
        if cls.maze[i][j] == "":
          cls.maze[i][j] = 1 if random() < 0.7 else 0
  
  def generate_neighbours(self, randomize=False):
    i, j = self.state
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if randomize:
      shuffle(directions)
    for di, dj in directions:
      ni, nj = i + di, j + dj
      if 0 <= ni < Maze.rows and 0 <= nj < Maze.cols:
        if (not randomize and Maze.maze[ni][nj] == 0) or randomize:
          yield Maze((ni, nj))
  
  def manhattan_distance(self, other):
      return abs(self.state[0] - other.state[0]) + abs(self.state[1] - other.state[1])
  
  def __lt__(self, other):
    if isinstance(other, Maze):
      return self.manhattan_distance(Maze.goal) < other.manhattan_distance(Maze.goal)
    
  def get_state(self):
    return self.state
  
  def get_state_tuple(self):
    return self.state