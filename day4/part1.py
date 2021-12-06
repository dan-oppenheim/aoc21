class Board:
    def __init__(self, lines):
        self.board = []
        for line in lines:
            self.board += [int(x) for x in line.split()]
    
    def __str__(self):
        s = ""
        for i in range(0, 25, 5):
            s += ', '.join([f"{x:>2}" for x in self.board[i:i+5]]) + '\n'

        return s

    def _to_index(self, x, y):
        return y * 5 + x

    def _from_index(self, index):
        return (index % 5, index // 5)

    def _check_row(self, y):
        for x in range(5):
            i = self._to_index(x, y)
            if self.board[i] != 'x':
                return False
        return True

    def _check_column(self, x):
        for y in range(5):
            i = self._to_index(x, y)
            if self.board[i] != 'x':
                return False
        return True

    def check_number(self, number):
        try:
            index = self.board.index(number)
            self.board[index] = 'x'
            x, y = self._from_index(index)
            return self._check_row(y) or self._check_column(x)
        except ValueError:
            pass

    def sum_unmarked(self):
        sum = 0
        for num in self.board:
            if num == 'x':
                continue
            sum += num
        return sum


def check_boards(num, boards):
    complete_boards = []
    for board in boards:
        if board.check_number(num):
            complete_boards.append(board)
    return complete_boards

def day1(draw_stream, boards):
    for num in draw_stream:
        completed_boards = check_boards(num, boards)
        if len(completed_boards) > 0:
            print(f"Day one result is: {completed_boards[0].sum_unmarked() * num}")
            break

def day2(draw_stream, boards):
    last_board = None
    last_num = 0
    for num in draw_stream:
        completed_boards = check_boards(num, boards)
        for completed in completed_boards:
            boards.remove(completed)
            last_board = completed
            last_num = num

    print(f"Day two result is {last_board.sum_unmarked() * last_num}")

        

with open('input.txt') as input_file:
    draw_stream = [int(x) for x in input_file.readline().split(',')]

    # data assumptions! the rest of the file consists of an empty line and
    # five board lines.
    lines = input_file.readlines()
    assert(len(lines) % 6 == 0)
    boards = []
    for board_index in range(0, len(lines), 6):
        board = Board(lines[board_index+1:board_index+6])
        boards.append(board)
    
    day1(draw_stream, boards)
    day2(draw_stream, boards)
            
