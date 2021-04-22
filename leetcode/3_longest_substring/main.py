def lengthOfLongestSubstring(word):
	counter = 0
	stack = []

	for index in range(len(word)):
		char = word[index]
		if char in stack:
			counter = max(counter, len(stack))
			old_index = stack.index(char)
			stack = stack[old_index + 1:] + [char]
		else:
			stack.append(char)

	return max(counter, len(stack))

print(lengthOfLongestSubstring("dvdf"))     # 3
print(lengthOfLongestSubstring("bbbbb"))    # 1
print(lengthOfLongestSubstring("pwwkew"))   # 3
print(lengthOfLongestSubstring(""))         # 0
print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring(" "))        # 1
print(lengthOfLongestSubstring("ckilbkd"))  # 5
print(lengthOfLongestSubstring("au"))       # 2
print(lengthOfLongestSubstring("aa"))       # 1