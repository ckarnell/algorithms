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

if __name__ == "__main__":
    array = [1, 2, [3, 4, [5, 6], 7, 8], [9, 10]]
    print flattener(array)

    print func("Hello ")("world!")
