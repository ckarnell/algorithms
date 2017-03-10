# For a list of integers that also contains nested
# lists of integers, return a flattened list.
# e.g. [1, [2, 3], [4, [5, 6], 7], 8, [9, [10]]]
# would return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def flattener(l):
    flattened = []
    def flattener_recurse(sub_list):
        for element in sub_list:
            if isinstance(element, int):
                flattened.append(element)
            elif isinstance(element, list):
                flattener_recurse(element)

    flattener_recurse(l)
    return flattened

# func("Hello ")("world!") returns "Hello world!".
# This is a functional question asked for a job interview.
def func(str1):
    final_str = str1

    def return_func(str2):
        return final_str + str2

    return return_func

# Given a list of numbers, return a number equal to the
# greatest sum of consecutive elements of the list.
def max_slice_finder(l):
    assert l, 'List must have at least one element'
    local_max = l[0]
    saved_max = l[0]
    absolute_max = l[0]

    if len(l) == 1:
        return local_max

    for num in l[1:]:
        if num < 0:
            if saved_max < 0:
                saved_max = max(saved_max, num)
            elif saved_max + num > 0:
                absolute_max = max(absolute_max, saved_max)
                saved_max += num
            else:
                saved_max += num

            absolute_max = max(absolute_max, local_max, saved_max)
            local_max = num
        else:
            if local_max < 0:
                local_max = num
            else:
                local_max += num
                absolute_max = max(absolute_max, local_max)
            if saved_max < 0:
                saved_max = num
            else:
                saved_max += num

            absolute_max = max(absolute_max, local_max, saved_max)

    return absolute_max 

# Simple fibionacci series solver.
def fib(num):
    if num in [1, 0]:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

# Simple function that takes who sequences and returns a sequence
# with alternating elements.
def alternator(seq1, seq2):
    result = zip(seq1, seq2)
    if result:
        return list(reduce(lambda x, y: x + y, result))
    else:
        return []

# Returns True if the two input strings are anagrams,
# or False if they are not
def anagram_checker(str1, str2):
    lstr2 = list(str2)
    for c in str1:
        try: 
            lstr2.remove(c)
        except ValueError:
            return False
    if not lstr2:
        return True
    return False

# Validates strings with different combinations of brackets
def bracket_validator(brack):
    openers, closers = ['{', '[', '('], ['}', ']', ')']
    stack = []
    for c in brack:
        if c in openers:
            stack.append(c)
        elif c in closers:
            try:
                char = stack.pop(-1)
                if char != c:
                    return False
            except IndexError:
                return False
    if not stack:
        return True

# You have an array of numbers. You want this array of numbers to be in ascending order. 
# Consider a number d. You can add/subtract any number in your array by any number <= d. 
# What is the smallest d you could use to make the array ascending?
def smallest_ascending_k(arr):
    prev = arr[0]
    current_k = 0
    for el in arr[1:]:
        if el + current_k <= prev - current_k:
            current_k = ((prev - el) / 2) + 1
        prev = el
    return current_k

# Given a starting point A and an ending point B (both integers), this algorithm
# will find the total number of perfect squares between A and B inclusive using
# Neuton's method
def total_perfect_squares(A, B):
    def neutons_method(num):
        if num == 1:
            return True
        left = 0
        right = num
        old_middle = 0
        middle = (right - left) / 2
        while old_middle != middle:
            res = middle * middle
            if res == num:
                return True
            elif res > num:
                right = middle
            else:
                left = middle
            old_middle = middle
            if left + ((right - float(left)) / 2) == left + ((right - left) / 2):
                middle = left + ((right - left) / 2)
            else:
                middle = left + ((right - left) / 2) + 1
        res = middle * middle
        if res == num:
            return True
        return False

    tot = 0
    for x in range(A, B+1):
        if neutons_method(x):
            tot += 1
    return tot

if __name__ == "__main__":
    import unittest

    class AlgorithmTest(unittest.TestCase):
        def test_flattener(self):
            inputs = (([1, 2, [3, 4, [5, 6], 7, 8], [9, 10]], range(11)[1:]),)
            self.assertTrue(all(flattener(t[0]) == t[1] for t in inputs))

        def test_func(self):
            inputs = (("Hello ", "world!", "Hello world!"),)
            self.assertTrue(all(func(t[0])(t[1]) == t[2] for t in inputs))

        def test_max_slice_finder(self):
            inputs = (([-1], -1), ([-1, 5, 6, -20, 10, 11, -2, 20, -5], sum([10, 11, -2, 20])),
                      ([-20, -30, -40, -10, -100], -10), ([-5, 10, -20, -30, 5, 6, -50], 11))
            self.assertTrue(all(max_slice_finder(t[0]) == t[1] for t in inputs))

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

    unittest.main()

