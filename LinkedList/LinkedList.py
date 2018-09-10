#!usr/bin/python3
#Chido Nguyen
#Practicing data structures in multi languages

#nodes have next and data
class Nodes:
	data = None
	nextNode = None

#LL itself has a head sentinel , the list operations like append/pre-pend/traverse etc
class LinkedList:
	headNode = None
	#prepend approach#
	def addNode(self,newNode):
		if self.headNode == None:
			self.headNode = newNode
		else:
			tmpNode = self.headNode
			self.headNode = newNode
			self.headNode.nextNode = tmpNode
	def printNode(self):
		tmpNode = self.headNode
		while tmpNode.nextNode != None:
			print(tmpNode.data)
			tmpNode = tmpNode.nextNode
		print(tmpNode.data)


def main():
	x = Nodes()
	x.data = 1
	y = Nodes()
	y.data = 2
	z = Nodes()
	z.data = 3
	list = LinkedList()
	list.addNode(z)
	list.addNode(y)
	list.addNode(x)
	list.printNode()
main()