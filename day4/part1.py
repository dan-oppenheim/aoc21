class Board:
    def __init__(self, lines):
        self.board = []
        for line in lines:
            self.board.append([int(x) for x in line.split()])
    
    def __str__(self):
        s = ""
        for line in self.board:
            s += str(line) + '\n'
        return s

with open('input.txt') as input_file:
    draw_stream = input_file.readline().split(',')

    # data assumptions! the rest of the file consists of an empty line and
    # five board lines. so we know how many boards there are
    lines = input_file.readlines()
    num_boards = len(lines) // 6

    boards = []
    for board_index in range(0, 600, 6):
        board = Board(lines[board_index+1:board_index+6])
        boards.append(board)
        print(board)
            
