// Functional problem: write a function func such that if you
// call it with func(str1)(str2), it returns str1+str2
module.exports.func = function(str1) {
    var result = function(str2) { 
        return str1 + str2;
    }
    return result;
}

// Function for flattening arrays
module.exports.flattener = function(arr) {
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

