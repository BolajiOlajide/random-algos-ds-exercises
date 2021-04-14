from typing import List

class FirstUnique:
	def __init__(self, nums: List[int]):
		self._queue = nums


	def showFirstUnique(self) -> int:
		_dups = [x for i, x in enumerate(self._queue) if i != self._queue.index(x)]
		for item in self._queue:
			if item not in _dups:
				return item
		return -1


	def add(self, value: int) -> None:
		self._queue = [*self._queue, value]

# firstUnique = FirstUnique([809]);
# print(firstUnique.showFirstUnique()); # return 809
# firstUnique.add(809);          # the queue is now [809,809]
# print(firstUnique.showFirstUnique()); # return -1
# print(firstUnique._queue)

# firstUnique = FirstUnique([2,3,5]);
# print(firstUnique.showFirstUnique()); # return 2
# firstUnique.add(5);            # the queue is now [2,3,5,5]
# print(firstUnique.showFirstUnique()); # return 2
# firstUnique.add(2);            # the queue is now [2,3,5,5,2]
# print(firstUnique.showFirstUnique()); # return 3
# firstUnique.add(3);            # the queue is now [2,3,5,5,2,3]
# print(firstUnique.showFirstUnique()); # return -1

firstUnique = FirstUnique([233])
print(firstUnique.showFirstUnique())
firstUnique.add(11)
print(firstUnique.showFirstUnique())