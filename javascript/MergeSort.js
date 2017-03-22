Merge = function(array) {
    if (array.length <= 1) {
        return array
    }

    half = parseInt(array.length / 2);
    lefthalf = array.slice(0, half);
    righthalf = array.slice(half, array.length);
    return MergeSort(Merge(lefthalf), Merge(righthalf));
}

MergeSort = function(left_arr, right_arr) {
    result = [];
    while ((left_arr.length > 0) && (right_arr.length > 0)) {
        if (left_arr[0] < right_arr[0]) {
            result.push(left_arr.shift());
        } else {
            result.push(right_arr.shift());
        }
    }

    while (left_arr.length > 0) {
        result.push(left_arr.shift());
    }

    while (right_arr.length > 0) {
        result.push(right_arr.shift());
    }

    console.log("SORT RESULT: " + result); // Debug
    return result;
}

// Function for checking equality of arrays that
// don't contain nested arrays
Array.prototype.equals = function(array) {
    if (!array) { return false; }
    if (array.length !== this.length) { return false; }

    // Check for equality
    for (x = 0; x < array.length; x++) {
        if (this[x] !== array[x]) { return false; }
    }
    return true;
}

// Tests
var results = {successes: 0, failures: 0};
testMergeSort = function(input) {
    output = Merge(input.concat());
    if (output.equals(input.sort())) {
        results.successes++;
        console.log(`Success: ${output}`);
    } else {
        results.failures++;
        console.log(`Failure: ${output}`);
    }
}

inputs = [[], [2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [100, 1000, 10], [-1, -10, 4, 0], [1]];
for (x = 0; x < inputs.length; x++) {
    testMergeSort(inputs[x]);
}
console.log(`${results.successes} successes, ${results.failures} failures.`);
