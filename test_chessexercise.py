import unittest
import chessexercise


class TestChessExercise(unittest.TestCase):
    def test_decode_pos(self):
        self.assertEqual(chessexercise.decode_pos('d2'), (4, 2))
        self.assertEqual(chessexercise.decode_pos('a3'), (1, 3))
        with self.assertRaises(TypeError):
            chessexercise.decode_pos(3)

    def test_encode_pos(self):
        self.assertEqual(chessexercise.encode_pos(4, 2), 'd2')

    def test_validate_position(self):
        self.assertEqual(chessexercise.validate_position(4, 2), True)
        self.assertEqual(chessexercise.validate_position(4, -2), False)
        self.assertEqual(chessexercise.validate_position(4, 0), False)
        self.assertEqual(chessexercise.validate_position(1, 1), True)

    def test_get_knight_moves(self):
        result = ['f3', 'b3', 'f1', 'b1', 'e4', 'c4']
        self.assertEqual(chessexercise.get_knight_moves('d2'), result)

        result = ['c2', 'b3']
        self.assertEqual(chessexercise.get_knight_moves('a1'), result)

        result = ['f7', 'g6']
        self.assertEqual(chessexercise.get_knight_moves('h8'), result)

        with self.assertRaises(TypeError):
            chessexercise.get_knight_moves(3)

        with self.assertRaises(IndexError):
            chessexercise.get_knight_moves('a')

    def test_get_rook_moves(self):
        result = ['h1', 'a8', 'h2', 'b8', 'h3', 'c8', 'h4', 'd8', 'h5', 'e8', 'h6', 'f8', 'h7', 'g8']
        self.assertEqual(chessexercise.get_rook_moves('h8'), result)

        with self.assertRaises(TypeError):
            chessexercise.get_rook_moves(3)

        with self.assertRaises(IndexError):
            chessexercise.get_rook_moves('a')

    def test_get_queen_moves(self):
        result = ['h1', 'a8', 'h2', 'b8', 'h3', 'c8', 'h4', 'd8', 'h5', 'e8', 'h6', 'f8', 'h7', 'g8', 'g7', 'f6', 'e5',
                  'd4', 'c3', 'b2', 'a1']
        self.assertEqual(chessexercise.get_queen_moves('h8'), result)

        with self.assertRaises(TypeError):
            chessexercise.get_queen_moves(3)

        with self.assertRaises(IndexError):
            chessexercise.get_queen_moves('a')


if __name__ == '__main__':
    unittest.main()
