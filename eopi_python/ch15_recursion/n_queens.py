class Solution:
    def __init__(self):
        self.results = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.compute_n_queens()
        return self.construct_answer()
        
    def compute_n_queens(self, positions=None, curr_row=0):
        if positions is None:
            positions = []

        if curr_row > self.n:
            return None

        for y in range(0, self.n):
            curr_position = (curr_row, y)
            if self.is_in_attacking_position(curr_position, positions) == False:
                copy_of_positions = positions + [curr_position]
                if len(copy_of_positions) == self.n:
                    self.results.append(copy_of_positions)
                else:
                    self.compute_n_queens(copy_of_positions, curr_row + 1)

    def is_in_attacking_position(self, curr_position, positions):
        for pos in positions:
            if abs(curr_position[1] - pos[1]) == 0 or (abs(curr_position[1] - pos[1])/abs(curr_position[0] - pos[0]) == 1):
                return True
        return False
    
    def construct_row(self, position):
        append_num = self.n - position[1] - 1
        return (position[1] * ".") + "Q" + (append_num * ".")
    
    def construct_board(self, board_positions):
        board = []
        for pos in board_positions:
            board.append(self.construct_row(pos))
        return board
    
    def construct_answer(self):
        return [self.construct_board(board_positions) for board_positions in self.results]
