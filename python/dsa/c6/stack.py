class Stack:
	"""LIFO Stack iplementation usin a Python list as underlyin storage."""

	def __init__(self):
		"""Create an empty stack"""
		self.data = []
		
	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self.data)

	def top(self):
		"""
		Return (but do not remove) the element at the top of the stack.
		Raise Empty exception if the stack is empty.
		"""
		if self.isEmpty():
			raise Empty('Stack is empty')
		return self.data[-1]

	def push(self, e):
		"""Add element e to the top of the stack."""
		self.data.append(e)

	def pop(self):
		"""
		Remove and return the element from the top of the stack (i.e., LIFO).
		Raise Empty exception if the stack is empty.
		"""
		if self.isEmpty():
			raise Empty('Stack is empty.')
		self.data.pop()

	def isEmpty(self):
		"""Return True if the stack is empty."""
		return len(self.data) == 0

if __name__ == '__main__':
	stack = Stack() 

	stack.push(5)
	stack.push(7)
	stack.push(1)
	stack.push(9)
	stack.push(2)

	for i in range(len(stack)):
		print(stack.top())
		stack.pop()