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

# This was a functional question asked for a job interview at Enigma.io
# Write a function such that func("Hello ")("world!") returns "Hello world!".
def func(str1):
    final_str = str1

    def return_func(str2):
        return final_str + str2

    return return_func

# Simple fibionacci series solver. This is a common problem
# for demonstrating recursion
def fib(num):
    if num in [1, 0]:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

# Simple function that takes two sequences and returns a sequence
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
    brack_d = {')': '(', '}': '{', ']': '['}
    stack = []
    for c in brack:
        if c in brack_d.values():
            stack.append(c)
        elif c in brack_d.keys():
            try:
                char = stack.pop(-1)
                if brack_d[char] != c:
                    return False
            except IndexError:
                return False
    if stack:
        return False
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
# the bisection method.
def total_perfect_squares(A, B):
    def bisection_method(num):
        # Uses the bisection method to find out if the root of 
        # the given number is an integer
        if num in [0, 1]:
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
        if bisection_method(x):
            tot += 1
    return tot

# This was for a coding test for Blue Mountain Capital.
# Algorithm that takes in a list of comma seperated triplets, that represent
# the value, left leaf, and right leaf of a node, respectively. This
# algorithm should return the minimum level of the tree such that a node
# on that level is missing either a left or right leaf. The first triplet is the
# root node and following lines are branches/leaves of previous lines.
def minimum_level(graph_list):
    graph_list = [triple.split(',') for triple in graph_list]

    def add_node(triple, graph):
        node_name = triple[0]
        left, right = triple[1], triple[2]
        if node_name not in graph:
            graph[node_name] = {'left': '', 'right': ''}
        if not graph[node_name]['left']:
            graph[node_name]['left'] = left
        if not graph[node_name]['right']:
            graph[node_name]['right'] = right
        # Add the left/right nodes to the graph if they're not
        # already in the graph
        if left and left not in graph:
            graph[left] = {'left': '', 'right': ''}
        if right and right not in graph:
            graph[right] = {'left': '', 'right': ''}

        return graph

    def get_next_level(graph, nodes):
        '''
        Returns the next level of the graph, or False if one of the
        current nodes lacks either a right or left branch
        '''
        next_level = []
        for node in nodes:
            if not (graph[node]['left'] and graph[node]['right']):
                return False
            next_level.append(graph[node]['left'])
            next_level.append(graph[node]['right'])
        return next_level

    graph = {}
    # Get ahold of root for later
    root = graph_list[0]
    graph = add_node(root, graph)
    for triple in graph_list[1:]:
        graph = add_node(triple, graph)
    level = -1
    next_level = [root[0]]
    while next_level:
        next_level = get_next_level(graph, next_level)
        level += 1
    return level

# Given a string made of only 1's, 0's, and X's, return a list of 
# every combination of the string if the X's were replaced with either 0's or 1's.
def binary_string_replace(inpt):
    d = {}
    cur_key = 0
    last_ind = 0

    # Separate into chunks, each containing an X except the last
    for ind in range(len(inpt)):
        if inpt[ind].upper() == 'X':
            cur_str = inpt[last_ind:ind]
            d[cur_key] = [cur_str+'0', cur_str+'1']
            last_ind = ind + 1
            cur_key += 1
    d[cur_key] = [inpt[last_ind:]]

    # Compile every combination of the ordered chunks
    result = []
    for key in d:
        if not result:
            result.extend(d[key])
            continue
        result = [head + tail for head in result for tail in d[key]]
    return result

# Longest increasing sequence problem - Given a sequence of n real numbers A(1) ... A(n),
# determine a slice of maximum length in which the values in the slice form a strictly 
# increasing sequence.
def longest_increasing_slice(arr):
    try:
        el = arr[0]
        curr_slice = max_slice = [el]
        last = el
    except IndexError:
        return []
    for el in arr: # O(n)
        if el > last:
            curr_slice.append(el)
        else:
            if len(max_slice) < len(curr_slice):
                max_slice = curr_slice
            curr_slice = [el]
        last = el
    if len(max_slice) < len(curr_slice):
        max_slice = curr_slice
    return max_slice

# Check if two strings are a rotation of eachother.
def rotation_check(str1, str2):
    if len(str1) != len(str2):
        return False
    str_double = str1*2
    if str_double.count(str2):
        return True
    return False
