from bingo_board import BingoBoard

def main_part_1():
    draw_numbers, boards = read_input_file()
    answer = play_bingo(draw_numbers, boards)
    print(f'The answer to part 1 is: {answer}')

def main_part_2():
    draw_numbers, boards = read_input_file()
    answer = lose_bingo(draw_numbers, boards)
    print(f'The answer to part 2 is: {answer}')

def read_input_file():
    f = open('input.txt', 'r')

    draw_numbers = list()
    boards = list()
    current_board = []
    i = 0

    for line in f:
        line = trim_newline_char_if_exists(line)
        
        if i == 0:
            draw_numbers = [int(numeric_str) for numeric_str in line.split(',')]
        else:
            current_board = current_board + [int(numeric_str) for numeric_str in line.split()]

        if len(current_board) == 25:
            boards.append(BingoBoard(current_board)) 
            current_board = []
        i += 1 

    return draw_numbers, boards

def play_bingo(draw_numbers, boards):
    for num in draw_numbers:
        for board in boards:
            board.mark_cell(num)
            if board.winner:
                return board.calculate_score(int(num))

def lose_bingo(draw_numbers, boards):
        num_of_winners = 0;
        total_boards = len(boards)

        for num in draw_numbers:
            for board in boards:
                if not board.winner:
                    board.mark_cell(num)
                    if board.winner and num_of_winners == total_boards - 1:
                        return board.calculate_score(num)
                    elif board.winner:
                        num_of_winners += 1

def trim_newline_char_if_exists(line):
    if len(line) > 1 and line[-1] == '\n':
        return line[:-1]
    return line

if __name__ == "__main__":
    main_part_1()
    main_part_2()
