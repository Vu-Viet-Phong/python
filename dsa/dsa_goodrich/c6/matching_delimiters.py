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

def is_matched(expr):
	"""Return True if all delimiters are properly match; False otherwise."""
	lefty = '({['
	righty = ']})'	
	S = Stack
	for i in expr:
		if i in lefty:
			S.push(c)
		elif c in righty:
			if S.isEmpty():	
				return False
			if righty.index(c) != lefty.index(S.pop()):
				return False
	return S.isEmpty()

def is_matched_htlm(raw):
	"""Return True if all HTML tags are properly match; False otherwise."""
	s = Stack()
	i = raw.find('<')
	while i != -1:
		j = raw.find('>', i+1)
		if i == -1:
			return False
		tag = raw[j+1:k]
		if not tag.startswith('/'):
			s.push(tag)
		else:
			if S.isEmpty():
				return False
			if tag[1:] != s.pop():
				return False
		i = raw.find('<', k+1)
	return s.isEmpty()

is_matched_htlm('raw.html')