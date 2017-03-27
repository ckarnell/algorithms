var algos = require('./RandomAlgos');

// Function for comparing arrays for equality
Array.prototype.equals = function(arr) {
  if (this.length !== arr.length) {
    return false;
  }
  for (i = 0; i < this.length; i++) {
    if (this[i].constructor === Array) {
      if (!this[i].equals(arr[i])) {
        return false;
      }
    }
    if (this[i] !== arr[i]) {
      return false;
    }
  }
  return true;
}


// Tests
var Results = {"Successes": 0, "Failures": 0}
var compare = function(result, expected) {
    if (expected.constructor === Array) {
      if (expected.equals(result)) {
        // return true;
        Results.Successes++;
      } else {
        // return false;
        Results.Failures++;
      }
    } else if (result === expected) {
      // return true;
      Results.Successes++;
    } else {
      // return false;
      Results.Failures++;
    }
}

var print_results = function(results) {
  console.log(`Successes: ${results.Successes}\nFailures: ${results.Failures}`);
}

var compare_results = function(inputs) {
  for (i = 0; i < inputs.length; i++) {
    compare(inputs[i][0], inputs[i][1]);
  }
}

// TESTS
tests = [];
var test_func = function() {
  var inputs = [];
  inputs.push([algos.func("Hi ")("there"), "Hi there"]);
  inputs.push([algos.func("")("12345"), "12345"]);
  inputs.push([algos.func("12345")(""), "12345"]);
  compare_results(inputs);
}
tests.push(test_func);

var test_flattener = function() {
  var inputs = [];
  arr = algos.flattener([1, 2, [3, 4, [5], [6, 7]], 8, 9, [10]]);
  expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  inputs.push([arr, expected]);
  compare_results(inputs);
}
tests.push(test_flattener);

for (i = 0; i < tests.length; i++) {
  tests[i]();
}
print_results(Results);

