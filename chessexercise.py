import sys
import argparse


def read_arguments():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-piece",
                            help="Name of the pawn, Accepted values: Knight,Rook,Queen")
        parser.add_argument("-position", help="Position of pawn on Chessboard, "
                                              "It has 2 characters first should lie between a-h & second between 1-8")
        args = parser.parse_args()

        # print("argument list: ", len(sys.argv))

        if len(sys.argv) != 5:
            print("Piece and Position values should be provided ")
            print("Format: chessexercise.py -piece <<piece name>> -position <<position>>")
            sys.exit(1)

        if args.piece is None:
            print("Error: Piece is mandatory argument to the program. Accepts: Knight or Rook or Queen ")
            sys.exit(1)
        elif args.piece.upper() not in ['KNIGHT', 'ROOK', 'QUEEN']:
            print("Error: Piece  doesn't match pieces in accepted piece list: 'KNIGHT','ROOK','QUEEN'")
            sys.exit(1)

        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        digits = [1, 2, 3, 4, 5, 6, 7, 8]

        if args.position is None or len(args.position) != 2:
            print("Error: Position is mandatory argument to the program."
                  "It has 2 characters first should lie between a-h & second between 1-8")
            sys.exit(1)
        elif args.position[0].lower not in alpha and int(args.position[1]) not in digits:
            print("Error: Position argument is not in correct format."
                  "It has 2 characters first should lie between a-h & second between 1-8")
            sys.exit(1)

        return args.piece, args.position

    except Exception as excep:
        print("Error : ", str(excep))
        sys.exit(1)


def decode_pos(pos):
    a, b = pos[0], pos[1]
    a = ord(a) - 96
    return int(a), int(b)


def encode_pos(row, column):
    char1 = chr(int(row) + 96)
    return char1 + str(column)


def validate_position(p, q):
    if (1 <= p <= 8) and (1 <= q <= 8):
        return True

    return False


def get_knight_moves(l_position):
    x, y = decode_pos(l_position)
    possible_positions = [(x + 2, y + 1), (x - 2, y + 1), (x + 2, y - 1), (x - 2, y - 1), (x + 1, y + 2),
                          (x - 1, y + 2), (x + 1, y - 2), (x - 1, y - 2)]

    final_position_list = [encode_pos(pos[0], pos[1]) for pos in possible_positions if validate_position(pos[0], pos[1])]
    return final_position_list


def get_queen_moves(l_position):
    x, y = decode_pos(l_position)
    possible_positions = []
    for i in range(1, 8):
        if i != x:
            possible_positions.append((x, i))
        if i != y:
            possible_positions.append((i, y))

    while validate_position(x + 1, y + 1):
        possible_positions.append((x + 1, y + 1))
        x += 1
        y += 1

    while validate_position(x - 1, y + 1):
        possible_positions.append((x - 1, y + 1))
        x -= 1
        y += 1

    # print("possible pos: ", possible_positions)

    while validate_position(x + 1, y - 1):
        possible_positions.append((x + 1, y - 1))
        x -= 1
        y += 1

    # print("possible pos: ", possible_positions)

    while validate_position(x - 1, y - 1):
        possible_positions.append((x - 1, y - 1))
        x -= 1
        y -= 1

    # print("possible pos: ", possible_positions)

    final_position_list = [encode_pos(pos[0], pos[1]) for pos in possible_positions]

    return final_position_list


def get_rook_moves(l_position):
    x, y = decode_pos(l_position)
    possible_positions = []
    for i in range(1, 8):
        if i != x:
            possible_positions.append((x, i))
        if i != y:
            possible_positions.append((i, y))

    final_position_list = [encode_pos(pos[0], pos[1]) for pos in possible_positions]
    return final_position_list


if __name__ == '__main__':

    piece, position = read_arguments()
    l_piece = piece.lower()
    l_position = position.lower()

    if l_piece == 'knight':
        position_list = get_knight_moves(l_position)
    elif l_piece == 'queen':
        position_list = get_queen_moves(l_position)
    elif l_piece == 'rook':
        position_list = get_rook_moves(l_position)

    # print("Possible moves for {}: ".format(piece.upper()), position_list)
    print(*position_list)
