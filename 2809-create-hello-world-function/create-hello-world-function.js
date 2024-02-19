/**
 * @return {Function}
 */
function createHelloWorld() {
    // Define the inner function
    const innerFunction = function (...args) {
        // Always return "Hello World" regardless of arguments
        return "Hello World";
    };

    // Return the inner function
    return innerFunction;
}


/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */