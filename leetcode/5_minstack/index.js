/**
 * initialize your data structure here.
 */
var MinStack = function() {
  this.stack = [];
  return this;
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
  this.stack.push(val);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.stack[this.stack.length - 1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
  return Math.min(...this.stack);
};

// var obj = new MinStack()
// obj.push(5)
// obj.push(2)
// obj.push(10)
// obj.push(6)
// obj.pop()
// var param_3 = obj.top()
// var param_4 = obj.getMin()

var minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
var param_3 = minStack.top();    // return 0
var param_4 = minStack.getMin(); // return -2

console.log(minStack, param_3, param_4)