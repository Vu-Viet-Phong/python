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

def reverse_file(filename):
	"""Overwrite given file with its contents line-by-line reversed."""
	S = Stack()
	origin = open(filename)
	for line in origin:
		S.push(line.rstrip('\n'))
	origin.close()

	output = open(filename, 'w')
	while not S.isEmpty():
		output.write(S.pop() + '\n')
	output.close()

# Driver Code
filename = "test.txt"
reverse_file(filename)
   
# Now reading the content of the file
with open(filename) as file:
    for f in file.readlines():
        print(f, end="")