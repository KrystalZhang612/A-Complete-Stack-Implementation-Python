#!/usr/bin/env python3


#use linked with supplemental class named NodeClass to implement stack data structure

class NodeClass:
	
	#initialization of the node tree 
	
	def __init__(self, data):
		
		self.value = data
		
		self.PreviousNode = None
		
		self.NextNode = None
		
		
#Stack class 
		
class Stack:
	
	#the initializer: a stack is always initizlied as empty. 
	
	#when the tail node is NULL, the entire stack is empty initialized
	
	def __init__(self):
		
		self.TailNode = None
	
	#define the push() function to add an element onto the stack
	
	def push(self, data):
		
		#passing data from NodeClass to new node here in stack 
		
		NewNode = NodeClass(data)
		
		#check if stack is empty
		
		#if stack is empty, push the data onto the stack
		
		if self.TailNode == None:
			
			self.TailNode = NewNode
			
		
		#else if the stack is not empty 
		
		#let the tail node be the previous node of the data to push in 
		
		#push the data(NewNode) onto the next node position of the current tail node 
		
		#now the top most node position is TailNode, we then push the data onto that node 
	
		else:
			
			NewNode.PreviousNode = self.TailNode
			
			self.TailNode.NextNode = NewNode
			
			self.TailNode = NewNode 
			
	#define the pop() function to remove the most recently added element 
	#from the collection and returns the element folowed by LIFO method 
	
	def pop(self):
		
		
		#check if stack is empty
		
		#Stack Underflow. Nothing to pop out. 
		
		if self.TailNode == None:
			
			print ("Error: Stack Underflow. Cannot pop out any elements from stack.")
			
			return 
		
		#else if the stack is not empty 
		
		#assign the data of the tail node as the current data 
		
		data = self.TailNode.value 
		
		#assign previous node of the tail node as the current previous node 
		
		PreviousNode = self.TailNode.PreviousNode
		
		#if the current previous node is not NULL
		
		if PreviousNode != None:
			
			#pop out the next node of the current previous node
			
			#remove he most recently added data on that position 
			
			PreviousNode.NextNode = None 
			
		#pop out the previous node of the current tail node 
		
		self.TailNode.PreviousNode = None 
		
		#assign the current previous node as the current tail node, done popping 
		
		self.TailNode = PreviousNode 
		
		return data
	
	
	#implement peek() function to return the most recently added element (without removing it)
	
	def peek(self):
		
		#check if the stack is empty
		
		#return error, no value to return at the top of the stack 
		
		if self.TailNode == None:
			
			print ("Error: Stack Underflow. Nothing to return.")
			
			return 
			
		#else return the peek value of the stack at tail position 
		
		return self.TailNode.value 
	
	
	
		

#Driver code 
	
if __name__ == '__main__':
	
	#start with an empty stack st and perform the following functions in order 
	
	st = Stack()
	
	st.push(3)
	
	st.peek()
	
	#print("The returned value is: ",st.peek())
	#the returned value is 3. test passed. 
	
	st.push(4)
	
	st.push(5)
	
	#print("The deleted and returned value is: ", st.pop())
	#the deleted and returned value is 5. test passed. 
	
	st.pop()
	
	st.peek()
	
	#print("The returned value is: ", st.peek()) 
	#the returned value is 4. test passed. 
	
	st.push(6)
	
	#print("The deleted and returned value is: ", st.pop())
	#the deleted and returned value is 6. test passed. 
	
	st.pop()
	
#Some extra tests 
	
	
	#start with an empty stack st and perform the following functions in order.
	
	TestingStack = Stack() 
	
	TestingStack.push(15)
	
	TestingStack.peek()
	
	#print("The returned value is: ", TestingStack.peek()) 
	#the returned value is 15. test passed. 
	
	TestingStack.push(24)
	
	TestingStack.push(28)
	
	#print("The deleted and returned value is: ", TestingStack.pop())
	#the deleted and returned value is 28. test passed. 
	
	TestingStack.pop()
	
	TestingStack.peek() 
	
	#print("The returned value is: ", TestingStack.peek()) 
	#he returned value is 24. test passed. 
	
	TestingStack.push(19) 
	
	
	#print("The deleted and returned value is: ", TestingStack.pop()) 
	#the deleted and returned value is 19. test passed. 
	
	TestingStack.pop()
	
	
	
	
	
	
	
	
	
	


	
	
	
	
	
	
	
		
	
			
			
			
			
		
		
		
		
			
			
		
		
		
		
		
	
	
	
	