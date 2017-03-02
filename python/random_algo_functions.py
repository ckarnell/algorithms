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
                absolute_max = max(absolute_max, saved_max)

            absolute_max = max(absolute_max, local_max)
            local_max = num
        else:
            if local_max < 0:
                local_max = num
                absolute_max = max(absolute_max, local_max)
            else:
                local_max += num
                absolute_max = max(absolute_max, local_max)
            if saved_max < 0:
                saved_max = num
            else:
                saved_max += num

    return max(absolute_max, local_max, saved_max)


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

    unittest.main()

