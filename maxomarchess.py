
import re


def print_board():
    print()
    print('   A B C D E F G H')
    print()

    for i, line in enumerate(board[1:]):
        line_number = str(8 - i)
        print(line_number + '  ' + " ".join(line[1:]) + '  ' + line_number)

    print()
    print('   A B C D E F G H')
    print()


def input_check(inp):
    return len(inp) == 2 and inp[0] in letter_to_number and inp[1] in '12345678'


def square_to_indices(square):
    return [len(board) - int(square[1]), letter_to_number[square[0]]]


def indices_to_square(x, y):
    return number_to_letter[y] + str(9-x)


def square_is_empty(x, y):
    piece = board[x][y]

    return piece == '.'


def piece_is_white(x, y):
    piece = board[x][y]

    return piece == piece.upper()


def move_is_valid(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8


def valid_moves_for_rook(x, y):
    moves = []

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x + 1, new_y

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x - 1, new_y

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x, new_y + 1

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x, new_y - 1

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    return moves


def valid_moves_for_bishop(x, y):
    moves = []

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x + 1, new_y + 1

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x - 1, new_y + 1

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x + 1, new_y - 1

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    new_x, new_y = x, y
    for i in range(1, 8):
        new_x, new_y = new_x - 1, new_y - 1

        if move_is_valid(new_x, new_y) and square_is_empty(new_x, new_y):
            moves.append([new_x, new_y])
        elif move_is_valid(new_x, new_y) and not square_is_empty(new_x, new_y) and white_moves != piece_is_white(new_x, new_y):
            moves.append([new_x, new_y])
            break
        else:
            break

    return moves


def valid_moves_for_queen(x, y):
    return valid_moves_for_rook(x, y) + valid_moves_for_bishop(x, y)


def valid_moves_for_king(x, y):
    moves = [[x + 1, y], [x + 1, y + 1], [x + 1, y - 1], [x - 1, y + 1],
             [x - 1, y - 1], [x - 1, y], [x, y - 1], [x, y + 1]]

    return [x for x in moves if move_is_valid(x[0], x[1])]


def valid_moves_for_knight(x, y):
    moves = [[x + 1, y + 2], [x + 2, y + 1], [x - 1, y + 2], [x - 2, y + 1],
             [x + 1, y - 2], [x + 2, y - 1], [x - 1, y - 2], [x - 2, y - 1]]

    return [x for x in moves if move_is_valid(x[0], x[1])]


def valid_moves_for_pawn(x, y):
    moves = []
    if piece_is_white(x, y):

        candidates = [[x - 1, y]]
        if x == 7:
            candidates.append([x - 2, y])

        for candidate in candidates:
            if move_is_valid(candidate[0], candidate[1]) and square_is_empty(candidate[0], candidate[1]):
                moves.append(candidate)

        candidates = [[x - 1, y + 1], [x - 1, y - 1]]
        for candidate in candidates:
            if move_is_valid(candidate[0], candidate[1]) and not square_is_empty(candidate[0], candidate[1]):
                moves.append(candidate)

    else:

        candidates = [[x + 1, y]]
        if x == 2:
            candidates.append([x + 2, y])

        for candidate in candidates:
            if move_is_valid(candidate[0], candidate[1]) and square_is_empty(candidate[0], candidate[1]):
                moves.append(candidate)

        candidates = [[x + 1, y + 1], [x + 1, y - 1]]
        for candidate in candidates:
            if move_is_valid(candidate[0], candidate[1]) and not square_is_empty(candidate[0], candidate[1]):
                moves.append(candidate)

    return moves


def valid_moves(x, y):
    piece = board[x][y]
    return valid_moves_by_pieces[board[x][y].lower()](x, y)


valid_moves_by_pieces = {
    'p': valid_moves_for_pawn,
    'r': valid_moves_for_rook,
    'n': valid_moves_for_knight,
    'b': valid_moves_for_bishop,
    'q': valid_moves_for_queen,
    'k': valid_moves_for_king
}


def short_castle(is_white):
    if is_white:
        if white_castled or white_king_moved or r_white_rook_moved:
            return False

        if square_is_empty(8, 7) and square_is_empty(8, 6):
            board[8][8] = '.'
            board[8][7] = 'K'
            board[8][6] = 'R'
            board[8][5] = '.'
            return True

    else:
        if black_castled or black_king_moved or r_black_rook_moved:
            return False

        if square_is_empty(1, 7) and square_is_empty(1, 6):
            board[1][8] = '.'
            board[1][7] = 'k'
            board[1][6] = 'r'
            board[1][5] = '.'
            return True

    return False


def long_castle(is_white):
    if is_white:
        if white_castled or white_king_moved or l_white_rook_moved:
            return False

        if square_is_empty(8, 2) and square_is_empty(8, 3) and square_is_empty(8, 4):
            board[8][1] = '.'
            board[8][3] = 'K'
            board[8][4] = 'R'
            board[8][5] = '.'
            return True

    else:
        if black_castled or black_king_moved or l_black_rook_moved:
            return False

        if square_is_empty(1, 2) and square_is_empty(1, 3) and square_is_empty(1, 4):
            board[1][1] = '.'
            board[1][3] = 'k'
            board[1][4] = 'r'
            board[1][5] = '.'
            return True

    return False


def is_previous_move_command(command):
    pattern = r'^previous_move( \d+)?$'
    return re.match(pattern, command) is not None


def is_next_move_command(command):
    pattern = r'^next_move( \d+)?$'
    return re.match(pattern, command) is not None


def is_find_moves_command(command):
    pattern = r'^[a-h][1-8]-$'
    return re.match(pattern, command) is not None


def is_find_opposing_pieces_command(command):
    pattern = r'^[a-h][1-8]$'
    return re.match(pattern, command) is not None


letter_to_number = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

number_to_letter = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h'
}

board = [
    [None, None, None, None, None, None, None, None],
    [None, 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    [None, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [None, '.', '.', '.', '.', '.', '.', '.', '.'],
    [None, '.', '.', '.', '.', '.', '.', '.', '.'],
    [None, '.', '.', '.', '.', '.', '.', '.', '.'],
    [None, '.', '.', '.', '.', '.', '.', '.', '.'],
    [None, 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [None, 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

white_moves = True
move_number = 1
white_castled = False
black_castled = False
l_white_rook_moved = False
r_white_rook_moved = False
l_black_rook_moved = False
r_black_rook_moved = False
white_king_moved = False
black_king_moved = False
moves_done = 0
history = []

while True:

    if white_moves:
        print(f'white {move_number}:')
    else:
        print(f'black {move_number}:')

    move = input()

    if move == 'exit':
        break

    if move == 'draw':
        print_board()
        continue

    if move == '0-0':
        castled_successfully = short_castle(white_moves)

        if not castled_successfully:
            print('Error. Type: The piece cannot make the specified move.')
        else:
            white_moves = not (white_moves)
            if white_moves:
                move_number += 1

        continue

    if move == '0-0-0':
        castled_successfully = long_castle(white_moves)

        if not castled_successfully:
            print('Error. Type: The piece cannot make the specified move.')
        else:
            white_moves = not (white_moves)
            if white_moves:
                move_number += 1

        continue

    if is_previous_move_command(move):
        try:
            length = int(move.split(" ")[1]) if len(move.split(" ")) > 1 else 1
        except:
            print('Error. Type: Wrong input format.')
            continue

        if length > len(history):
            print('Error. Type: History out of bounds')
            continue

        for i in range(length):
            moves_done -= 1
            start, destination, piece, eaten = history[moves_done]
            x1, y1 = square_to_indices(start)
            x2, y2 = square_to_indices(destination)
            board[x1][y1], board[x2][y2] = piece, eaten
            white_moves = not (white_moves)
            if not white_moves:
                move_number -= 1

        continue

    if is_next_move_command(move):

        try:
            length = int(move.split(" ")[1]) if len(move.split(" ")) > 1 else 1
        except:
            print('Error. Type: Wrong input format.')
            continue

        if length > len(history) - moves_done:
            print('Error. Type: History out of bounds')
            continue

        for i in range(length):
            start, destination, piece, _ = history[moves_done]
            x1, y1 = square_to_indices(start)
            x2, y2 = square_to_indices(destination)
            board[x1][y1], board[x2][y2] = '.', piece
            moves_done += 1
            white_moves = not (white_moves)
            if white_moves:
                move_number += 1e2-e4

        continue

    if is_find_moves_command(move):
        x, y = square_to_indices(move[:2])
        moves = valid_moves(x ,y)
        squares = sorted([indices_to_square(a, b) for a, b in moves])
        print(f'possible moves: {", ".join(squares) if squares else "none"}')
        continue

    if is_find_opposing_pieces_command(move):
        x, y = square_to_indices(move[:2])
        moves = valid_moves(x, y)
        squares = sorted([indices_to_square(a, b) for a, b in moves if not square_is_empty(a, b)])
        print(f'enemy figures under attack: {", ".join(squares) if squares else "none"}')
        continue

    try:
        start, destination = move.split('-')
        x1, y1 = square_to_indices(start)
        x2, y2 = square_to_indices(destination)
    except:
        print('Error. Type: Wrong input format.')
        continue

    if not (input_check(start) and input_check(destination)):
        print('Error. Type: Wrong input format.')
        continue

    if square_is_empty(x1, y1) or piece_is_white(x1, y1) != white_moves or start == destination:
        print('Error. Type: The piece cannot make the specified move.')
        continue

    moves = valid_moves(x1, y1)

    if [x2, y2] in moves:

        if moves_done <= len(history):
            history = history[:moves_done]
        moves_done += 1

        history.append([start, destination, board[x1][y1], board[x2][y2]])
        board[x1][y1], board[x2][y2] = '.', board[x1][y1]

        if start == 'a8': l_black_rook_moved = True
        if start == 'h8': r_black_rook_moved = True
        if start == 'a1': l_white_rook_moved = True
        if start == 'h1': r_white_rook_moved = True
        if start == 'e8': black_king_moved = True
        if start == 'e1': white_king_moved = True

        white_moves = not(white_moves)
        if white_moves:
            move_number += 1
    else:
        print('Error. Type: The piece cannot make the specified move.')
        continue