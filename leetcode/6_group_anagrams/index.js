/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  var result = [];
  const idxToIgnore = [];


  for (let idx = 0; idx < strs.length; idx += 1) {
    var currentStr = strs[idx];
    var currentStrArr = currentStr.split('');
    var anagrams = [];

    if (idxToIgnore.includes(idx)) {
      continue;
    }

    strs.forEach((str, anagramIdx) => {
      const splitString = str.split('');
      console.log(str, currentStr, containsAll(splitString, currentStrArr))

      if ((splitString.length === currentStrArr.length) && (containsAll(splitString, currentStrArr))) {
        anagrams.push(str);
        idxToIgnore.push(anagramIdx);
      }
    });

    result.push(anagrams);
  }

  return result;
};

// const containsAll = (arr1, arr2) => arr2.every(arr2Item => arr1.includes(arr2Item));
const containsAll = (arr1, arr2) => {
  const sortedArr1 = arr1.sort();
  const sortedArr2 = arr2.sort();

  for (let i = 0; i < sortedArr1.length; i += 1) {
    if (sortedArr1[i] != sortedArr2[i]) {
      return false;
    }
  }

  return true;
}


console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) // [["bat"],["nat","tan"],["ate","eat","tea"]]
console.log(groupAnagrams([""])) // [[""]]
console.log(groupAnagrams(["a"])) // [["a"]]
console.log(groupAnagrams(["ddddddddddg", "dgggggggggg"])) // [["dgggggggggg"],["ddddddddddg"]]