/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  const tracker = [];

  for (let i = 0; i < s.length; i += 1) {
    const char = s[i];
    const isOpen = openBrackets.includes(char);

    if (isOpen) {
      tracker.push(char);
    } else {
      const lastChar = tracker[tracker.length - 1];

      if ((char === ')') && (lastChar === '(')) {
        const popIdx = tracker.indexOf('(');
        tracker.pop(popIdx);
        continue;
      }

      if ((char === ']') && (lastChar === '[')) {
        const popIdx = tracker.indexOf('[');
        tracker.pop(popIdx);
        continue;
      }

      if ((char === '}') && (lastChar === '{')) {
        const popIdx = tracker.indexOf('{');
        tracker.pop(popIdx);
        continue;
      }

      return false;
    }
  }

  return tracker.length === 0;
};

const openBrackets = ['(', '[', '{'];
const closeBrackets = [')', ']', '}'];

console.log(isValid("()")) // true
console.log(isValid("()[]{}")) // true
console.log(isValid("(]")) // false
console.log(isValid("([)]")) // false
console.log(isValid("{[]}")) // true