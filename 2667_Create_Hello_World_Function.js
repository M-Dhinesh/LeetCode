/**
 * @return {Function}
 */
var createHelloWorld = function() {
    const v = 'Hello World'
    return function(...args) {
        return v
    }
};
