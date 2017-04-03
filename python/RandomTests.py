import unittest
from RandomAlgorithms import *

class TestRandom(unittest.TestCase):
    def test_flattener(self):
        inputs = (([1, 2, [3, 4, [5, 6], 7, 8], [9, 10]], range(11)[1:]),)
        self.assertTrue(all(flattener(t[0]) == t[1] for t in inputs))

    def test_func(self):
        inputs = (("Hello ", "world!", "Hello world!"),)
        self.assertTrue(all(func(t[0])(t[1]) == t[2] for t in inputs))

    def test_fib(self):
        inputs = ((1, 1), (0, 1), (3, 2), (5, 8))
        self.assertTrue(all(fib(i[0]) == i[1]) for i in inputs)

    def test_alternator(self):
        inputs = ((([], []), []),
                  (([1, 2, 3], [4, 5, 6]), [1, 4, 2, 5, 3, 6]),
                  (([1, 2, 3], ['4', '5', '6', '7']), [1, '4', 2, '5', 3, '6']))
        self.assertTrue(all(alternator(t[0][0], t[0][1]) == t[1] for t in inputs))

    def test_anagram_checker_valid(self):
        inputs = (['heyhey', 'yehyeh'],
                  ['', ''],
                  ['ddbbee', 'ebdbde'])
        self.assertTrue(all(anagram_checker(*i) for i in inputs))

    def test_anagram_checker_invalid(self):
        inputs = (['heyhey', 'ehyeh'],
                  ['', 'h'],
                  ['ddbbee', ''])
        self.assertFalse(any(anagram_checker(*i) for i in inputs))

    def test_smallest_ascending_k(self):
        inputs = (([5,1,3], 3),
                  ([1,2,6,0,10], 4),)
        self.assertTrue(all(smallest_ascending_k(i[0]) == i[1] for i in inputs))

    def test_total_perfect_squares(self):
        inputs = (([1, 100], 10),
                  ([1, 200], 14),
                  ([1, 1], 1),
                  ([49, 100], 4))
        self.assertTrue(all(total_perfect_squares(i[0][0], i[0][1]) == i[1] for i in inputs))

    def test_minimum_level(self):
        inputs = ((['a,b,c', 'b,d,e'], 1),
                  (['a,b,c', 'b,d,e', 'c,f,g', 'd,h,i', 'e,j,k', 'g,l,m'], 2),
                  (['a,b,c', 'b,d,e', 'c,f,g', 'd,h,i', 'e,j,k', 'f,l,m', 'g,n,o'], 3),
                  (['a,b,c', 'b,,e', 'c,f,g', 'e,j,k', 'f,l,m', 'g,n,o'], 1))
        self.assertTrue(all(minimum_level(i[0]) == i[1] for i in inputs))

    def test_binary_string_replace(self):
        inputs = (['01X', ['010', '011']], ['0X1', ['001', '011']], ['', ['']],
                  ['XXX', ['000', '001', '010', '011', '100', '101', '110', '111']])
        self.assertTrue(all(binary_string_replace(i[0]) == i[1] for i in inputs))

    def test_longest_increasing_slice(self):
        inputs = ([[1, 2, 3, 2, 1], [1, 2, 3]], [[10, 4, 5, 6, 3, 10, 11, 12, 13], [3, 10, 11, 12, 13]],
                  [[], []], [[0], [0]])
        self.assertTrue(all(longest_increasing_slice(i[0]) == i[1] for i in inputs))

    def test_rotation_check(self):
        inputs = ([['abda', 'aabd'], True], [['racecar', 'carrace'], True], [['', ''], True],
                  [['heythere', 'heothere'], False], [['hi', 'hihi'], False])
        self.assertTrue(all(rotation_check(*i[0]) == i[1] for i in inputs))

if __name__ == '__main__':
    unittest.main()
