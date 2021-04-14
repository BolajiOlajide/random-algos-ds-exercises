/**
 * @param {number[]} arr
 * @return {number[]}
 */
 var replaceElements = function(arr) {
  var lastIndx = arr.length - 1;

  return arr.map((elem, idx) => {
      if (idx === lastIndx) {
          return -1;
      }

      var slicedArray = arr.slice(idx + 1);

      return Math.max(...slicedArray);
  })
};