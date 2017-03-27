def _get_change_making_matrix(set_of_coins, r):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(r + 1):
      m[0][i] = i
    return m

def change_making(coins, n):
    """This function assumes that all coins are available infinitely.
    n is the number that we need to obtain with the fewest number of coins.
    coins is a list or tuple with the available denominations."""
    m = _get_change_making_matrix(coins, n)
    for c in range(1, len(coins) + 1):

        for r in range(1, n + 1):

            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = [coins[c - 1]]

            # coins[c - 1] cannot be included.
            # We use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]

            # We can use coins[c - 1].
            # We need to decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without using coins[c - 1]) plus this 1 extra coin.
            else:
                first = m[c - 1][r]
                if isinstance(first, int):
                    # first = [1 for _ in range(first)]
                    if first % coins[c - 1] == 0:
                        first = [coins[c - 1] for _ in range(first / coins[c - 1])]
                    else:
                        m[c][r] = first
                        continue
                second = m[c][r - coins[c - 1]] + [coins[c - 1]]
                if len(first) <= len(second):
                    m[c][r] = first
                else:
                    m[c][r] = second

    # return m
    if isinstance(m[-1][-1], list):
        return m[-1][-1]
    else:
        return False

if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    import unittest
    class DynamicProgrammingTest(unittest.TestCase):
        def test_get_change(self):
            inputs = ((([1, 5, 10, 25], 39), [1, 1, 1, 1, 10, 25]),
                      (([5, 10, 25], 40), [5, 10, 25]),
                      (([5, 10, 25], 39), False))
            self.assertTrue(all(change_making(i[0][0], i[0][1]) == i[1] for i in inputs))

    unittest.main()
