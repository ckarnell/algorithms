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


if __name__ == "__main__":
    array = [1, 2, [3, 4, [5, 6], 7, 8], [9, 10]]
    print flattener(array)
