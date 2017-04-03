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

# Given a list of numbers and a number k, find the subarray 
# of length k with the greatest min/max difference
def min_max_finder(arr, k):
    length = len(arr)
    assert length > k, "Array must have a length greater than k"
    loc_max = max(arr[:k])
    loc_min = min(arr[:k])
    max_diff = loc_max - loc_min
    ind = k+1
    while ind < length-1:
        # We only have to check for new max/mins when we find
        # a number greater or lower than our current max/min
        if arr[ind] > loc_max:
            high = k+ind if k+ind < length-1 else length-1
            min_in_area_around_ind = min(arr[ind-k:high])
            if arr[ind] - min_in_area_around_ind > max_diff:
                loc_max = arr[ind]
                loc_min = min_in_area_around_ind
                max_diff = loc_max - loc_min
        elif arr[ind] < loc_min:
            high = k+ind if k+ind < length-1 else length-1
            max_in_area_around_ind = max(arr[ind-k:high])
            if max_in_area_around_ind  - arr[ind] > max_diff:
                loc_max = max_in_area_around_ind
                loc_min = arr[ind]
                max_diff = loc_max - loc_min
        ind += 1
    return max_diff

# Given two lists and a target number, return one member of
# each list who's sum is the target number in O(2*n) time.
# If no such pair exists return False.
def target_number(A, B, target_num):
    b_dict = {target_num - b: b for b in B}
    for a in A:
        try:
            return [a, b_dict[a]]
        except KeyError:
            continue
    return False

# Given an array of numbers and a target number, this function
# finds the two values in the array who's sum is the closest
# to the target number without going over.
def find_inds_closest_to_sum(arr, trgt_num):
    import sys
    min_diff = sys.maxint
    left = 0
    right = len(arr) - 1
    results = []
    if arr:
        left_val, right_val = arr[left], arr[right]
    else:
        return False
    while left != right:
        curr_diff = left_val + right_val - trgt_num
        # If the value is positive the numbers were too high
        if curr_diff > 0:
            right -= 1 # Since the number too high, make the right number smaller
            right_val = arr[right]
        else:
            # Check for a new minimum and update values accordingly
            curr_diff = abs(curr_diff)
            if curr_diff < min_diff:
                results = [left_val, right_val]
                # Return if we found an optimal result
                if curr_diff == 0:
                    return results
                min_diff = curr_diff
            left += 1 # Since the number was negative, make the left number larger
            left_val = arr[left]
    if results:
        return results
    else:
        return False

# Returns length of the longest increasing subsequence
# in arr of size n
def longest_increasing_subseq(arr):
    if arr:
        track_increase = [1]*len(arr)
    else:
        return 0

    for i in range(len(arr)):
        for j in range(i): # O(n*((n+1)/2))
            if arr[j] < arr[i]:
                if track_increase[i] < track_increase[j] + 1:
                    track_increase[i] = track_increase[j] + 1
    return max(track_increase)

# Get the minimum "edit distance" between two strings - that is to say
# the minimum number of operations between replacing a character, removing
# a character, and adding a character that you have to do in order to make
# string 1 into a copy of string 2. O(3^n)
def min_edit_distance(str1, str2, count=0):
    if not (str1 and str2): # If either string is empty
        return count + len(str1) + len(str2)
    if str1[0] == str2[0]:
        return min_edit_distance(str1[1:], str2[1:], count)
    else:
        rep = min_edit_distance(str1[1:], str2[1:], count+1)
        rem = min_edit_distance(str1[1:], str2, count+1)
        add = min_edit_distance(str1, str2[1:], count+1)
        return min(rep, rem, add)

# More optimized dynamic version of the last solution for minimum edit
# distance, using subproblem storage. O(n*m)
def min_edit_distance_optimized(str1, str2):
    m, n = len(str1), len(str2)
    saved = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if not i: # If str1 is empty, add the rest of str2 to it
                saved[i][j] = j
            elif not j: # If str2 is empty, remove the rest of str1
                saved[i][j] = i
            elif str1[i-1] == str2[j-1]:
                saved[i][j] = saved[i-1][j-1]
            else:
                rem = saved[i-1][j]
                add = saved[i][j-1]
                rep = saved[i-1][j-1]
                saved[i][j] = 1 + min(rem, add, rep)
    return saved[m][n]

# Given an array of a stock's prices over time, return the optimal
# buy and sell prices to maximize profit.
def get_best_buy_sell_price(arr):
    min_buy = arr[0]
    max_prof = arr[1] - min_buy
    for curr_sell in arr[2:]:
        curr_prof = curr_sell - min_buy 
        if curr_prof > max_prof:
            max_prof = curr_prof
        if curr_sell < min_buy:
            min_buy = curr_sell
    return max_prof
