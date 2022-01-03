
class DLL:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None
			self.prev = None

	def __init__(self):
		self.head = None

	def push(self, data):
		node = self.Node(data)
		node.next = self.head
		if self.head is not None:
			self.head.prev = node
		self.head = node

	def printList(self, node):

		print("\nTraversal in forward direction")
		while node:
			print(" {}".format(node.data))
			last = node
			node = node.next

		print("\nTraversal in reverse direction")
		while last:
			print(" {}".format(last.data))
			last = last.prev



dll = DLL()
dll.push('A')
dll.push('B')
dll.push('C')
dll.push('D')
dll.printList(dll.head)
