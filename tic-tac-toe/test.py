# class TestTerminate(unittest.TestCase):

#     def setUp(self):
#         global board, played
#         board = [' '] * 9
#         played = set()
#         self.held, sys.stdout = sys.stdout, StringIO()

#     def tearDown(self):
#         sys.stdout = self.held

#     def test_empty_board(self):
#         self.assertFalse(terminate('X'))
#         self.assertFalse(terminate('O'))
#         self.assertEqual(sys.stdout.getvalue(), '')

#     def test_x_wins_horizontal(self):
#         global board, played
#         board = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
#         played = {0, 1, 2, 3, 4}
#         self.assertTrue(terminate('X'))
#         self.assertEqual(sys.stdout.getvalue().strip(),
#                          "You won! Thanks for playing.")

#     def test_o_wins_vertical(self):
#         global board, played
#         board = ['X', 'O', 'X', ' ', 'O', ' ', 'X', 'O', ' ']
#         played = {0, 1, 2, 4, 6, 7}
#         self.assertTrue(terminate('O'))
#         self.assertEqual(sys.stdout.getvalue().strip(),
#                          "You lost! Thanks for playing.")

#     def test_x_wins_diagonal(self):
#         global board, played
#         board = ['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'X']
#         played = {0, 1, 4, 5, 8}
#         self.assertTrue(terminate('X'))
#         self.assertEqual(sys.stdout.getvalue().strip(),
#                          "You won! Thanks for playing.")

#     def test_draw_full_board(self):
#         global board, played
#         board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
#         played = {0, 1, 2, 3, 4, 5, 6, 7, 8}
#         self.assertTrue(terminate('X'))
#         self.assertEqual(sys.stdout.getvalue().strip(),
#                          "A draw! Thanks for playing.")

#     def test_draw_blocked_board(self):
#         global board, played
#         board = ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
#         played = {0, 1, 2, 3, 4, 5, 6, 7, 8}
#         self.assertTrue(terminate('X'))
#         self.assertEqual(sys.stdout.getvalue().strip(),
#                          "A draw! Thanks for playing.")

#     def test_game_not_over(self):
#         global board, played
#         board = ['X', ' ', ' ', 'O', 'X', ' ', ' ', ' ', ' ']
#         played = {0, 3, 4}
#         self.assertFalse(terminate('X'))
#         self.assertEqual(sys.stdout.getvalue(), '')

#     def test_near_win_not_over(self):
#         global board, played
#         board = ['X', 'X', ' ', 'O', 'O', ' ', ' ', ' ', ' ']
#         played = {0, 1, 3, 4}
#         self.assertFalse(terminate('X'))
#         self.assertEqual(sys.stdout.getvalue(), '')

#     def test_near_loss_not_over(self):
#         global board, played
#         board = ['X', 'O', 'O', ' ', 'X', ' ', ' ', ' ', ' ']
#         played = {0, 1, 2, 4}
#         self.assertFalse(terminate('X'))
#         self.assertEqual(sys.stdout.getvalue(), '')

# if __name__ == '__main__':
#     unittest.main()