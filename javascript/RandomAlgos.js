// Functional problem: write a function func such that if you
// call it with func(str1)(str2), it returns str1+str2
var func = function(str1) {
    var result = function(str2) { 
        return str1 + str2;
    }
    return result;
}

// Function for flattening arrays
var flattener = function(arr) {
    var result = [];
    var flattener_recurse = function(current) {
        current.forEach(function(element) {
            if (typeof element === "number") {
                result.push(element);
            } else {
                flattener_recurse(element);
            }
        });
    }
    flattener_recurse(arr);
    return result;
}

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
var test = function(result, expected) {
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

var print_results = function(Results) {
  console.log(`Successes: ${Results.Successes}\nFailures: ${Results.Failures}`);
}

s = func("Hi ")("there");
test(s, "Hi there");

arr = [1, 2, [3, 4, [5], [6, 7]], 8, 9, [10]];
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
arr = flattener(arr);
test(arr, expected);

print_results(Results);

