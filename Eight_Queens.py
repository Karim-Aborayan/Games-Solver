from random import shuffle

class EightQueens:
    start, goal = None, None
    
    def __init__(self, board):
        self.state = board

    @classmethod
    def generate_problem(cls):
        board = list(range(8))
        while not EightQueens.is_valid(board):
            shuffle(board)
        cls.start = EightQueens(list(range(8)))
        cls.goal = EightQueens(board)
        return cls.start, cls.goal

    def generate_neighbours(self):
        for i in range(8):
            for j in range(i + 1, 8):
                new_board = self.state.copy()
                new_board[i], new_board[j] = new_board[j], new_board[i]
                yield EightQueens(new_board)

    def manhattan_distance(self, other):
        return sum(abs(self.state[i] - other.state[i]) for i in range(8))

    @staticmethod
    def is_valid(board):
        positions = []
        for i1, j1 in enumerate(board):
            for i2, j2 in positions:
                if j1 == j2 or abs(i1 - i2) == abs(j1 - j2):
                    return False
            positions.append((i1, j1))
        return True

    def __repr__(self):
        board_repr = []
        for row in range(8):
            line = [EightQueens.queen if self.state[row] == col else EightQueens.empty for col in range(8)]
            board_repr.append(" ".join(line))
        return "\n".join(board_repr)
    
    def __lt__(self, other):
        if EightQueens.goal:
            return self.manhattan_distance(EightQueens.goal) < other.manhattan_distance(EightQueens.goal)
        return False

    def __eq__(self, other):
        return self.state == other.state
    
    def get_state(self):
        return self.state
    
    def get_state_tuple(self):
        return tuple(self.state)