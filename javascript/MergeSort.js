Merge = function(array) {
    if (array.length < 2) {
        return array
    }

    half = array.length / 2;
    lefthalf = array.slice(0, half);
    righthalf = array.slice(half, lefthalf.length);
    console.log("LEFT HALF: " + lefthalf);
    console.log("RIGHT HALF: " + righthalf);

    return MergeSort(Merge(lefthalf), Merge(righthalf));
}

MergeSort = function(left_arr, right_arr) {
    result = [];
    while ((left_arr.length > 0) && (right_arr.length > 0)) {
        if (left_arr[0] < right_arr.length) {
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

    return result;
}

// Tests
var results = {successes: 0, failures: 0};
testMergeSort = function(input) {
    output = Merge(input.concat());
    if (output === input.sort()) {
        results.successes++;
    } else {
        results.failures++;
        console.log(`Failure: ${output}`);
    }
}

inputs = [[], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [100, 1000, 10], [-1, -10, 4, 0], [1]];
for (x = 0; x < inputs.length; x++) {
    testMergeSort(inputs[x]);
}
console.log(`${results.successes} successes, ${results.failures} failures.`);
