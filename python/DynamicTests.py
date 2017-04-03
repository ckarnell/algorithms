from DynamicAlgorithms import *
import unittest

class DynamicTest(unittest.TestCase):
    def test_min_edit_distance(self):
        inputs = ([['', 'hi'], 2], [['hey', ''], 3], [['geek', 'gesek'], 1],
                  [['sunday', 'saturday'], 3])
        self.assertTrue(all(min_edit_distance(*i[0]) == i[1] for i in inputs))

    def test_min_edit_distance_optimized(self):
        inputs = ([['', 'hi'], 2], [['hey', ''], 3], [['geek', 'gesek'], 1],
                  [['sunday', 'saturday'], 3])
        self.assertTrue(all(min_edit_distance_optimized(*i[0]) == i[1] for i in inputs))

    def test_target_number(self):
        inputs = ((([1, 3, 5], [10, 50, 100], 103), [3, 100]), 
                  (([5, 5, 5], [10, 10, 20], 62), False))
        self.assertTrue(all(target_number(*i[0]) == i[1] for i in inputs))

    def test_min_max_finder(self):
        inputs = ((([5, 5, 5, 2, 5, 5, 5], 2), 3),)
        self.assertTrue(all(min_max_finder(i[0][0], i[0][1]) == i[1] for i in inputs))

    def test_max_slice_finder(self):
        inputs = (([-1], -1), ([-1, 5, 6, -20, 10, 11, -2, 20, -5], sum([10, 11, -2, 20])),
                  ([-20, -30, -40, -10, -100], -10), ([-5, 10, -20, -30, 5, 6, -50], 11))
        self.assertTrue(all(max_slice_finder(t[0]) == t[1] for t in inputs))

    def test_longest_increasing_subseq(self):
        inputs = ([[1, 2, 3, 2, 1], len([1, 2, 3])], [[10, 4, 5, 6, 3, 10, 11, 12, 13], len([4, 5, 6, 10, 11, 12, 13])],
                  [[10, 22, 9, 33, 21, 50, 41, 60, 80], len([10, 22, 33, 50, 60, 80])],
                  [[], 0], [[0], 1])
        self.assertTrue(all(longest_increasing_subseq(i[0]) == i[1] for i in inputs))

    def test_find_inds_closest_to_sum(self):
        inputs = ([[[], 0], False], [[[1], 1], False], [[[3, 4, 5, 6, 20], 10], [4, 6]])
        self.assertTrue(all(find_inds_closest_to_sum(*i[0]) == i[1] for i in inputs))

    def test_get_best_buy_sell_price(self):
        inputs = ([[5, 4, 3, 2, 1], -1], [[5, 12, 1, 6, 7, 13, 6], 12])
        self.assertTrue(all(get_best_buy_sell_price(i[0]) == i[1] for i in inputs))

if __name__ == '__main__':
    unittest.main()
