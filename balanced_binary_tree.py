# abdullah alathel
import random

class BalancedSearch(object):
	def __init__(self,size=16):
		self.tree = [-1 for x in range(size)]
		self.size = size
		self.root = 1
		self.items = 0
		random = input('Choose a number')
		if type(random) is int:
		seed(random)
		print("came here")

		
	
		"""
@Name: insert
@Description:
    Receives a list of unordered integers and inserts them into the binary tree in such a manner that the resulting tree is balanced.
@Params:
    values (List) - unorderd list of integers
@Returns: None
	"""
	def insert(self,aList,start = 0,end = 0,root = None):
			
		if root == None:
			root = self.root
			if len(aList) == 3:
				self.tree[root]=aList[1]
				right = root*2+1
				left = root*2
				self.tree[left] = aList[0]
				self.tree[right]= aList[2]
				return
			else:
				if len(aList)%2 == 0:
					mid = int((len(aList)-2)/2)
					RightTreelist = aList[mid+1:]
					LeftTreelist = aList[1:mid]
					print("11LeftTreelist",LeftTreelist)
					print("11RightTreelist",RightTreelist)

				else:
					mid = int((len(aList)-1)/2)
					RightTreelist = aList[mid+1:]
					LeftTreelist = aList[0:mid]
					print("22LeftTreelist",LeftTreelist)
					print("22RightTreelist",RightTreelist)
					print(self.root)

				self.tree[root] = aList[mid]
				self.insert(LeftTreelist,0,mid,(self.root*2))
				self.insert(RightTreelist,mid+1,len(RightTreelist),(self.root*2+1))
				
			# loop until you find the location to insert
			# even if you have to extend this list
				
		"""
@Name: extend
@Description:
    extend the length of the list by 2
@Params:
    None
@Returns: None
		"""
		
	def extend(self):
		temp = [-1 for x in range(self.size)]
		self.tree.extend(temp)
		self.size *= 2
		print("AHA",self.items)
		
	def p(self):
		x = 0
		
		print("This is mE!",self.tree)
		print(len(self.tree))
		print (self.items)
		print("MEmEm",self.tree)
			"""
@Name: find
@Description:
    find if a value exists in the list and how many comparisons it took to find it
@Params:
    value to be seached
@Returns: number of comparisons
		"""
	def find(self,key):
	
		self.comparisons = 1

		if key == self.tree[self.root]:
			return True
		else:
			i = self.root
			while True:
				if key < self.tree[i]:
					i = self.leftChild(i)
				else:
					i = self.rightChild(i)
					
				if i >= self.size:
					return False
				
				if self.tree[i] == -1:
					return False   
					
				if self.tree[i] == key:
					return True
					
				self.comparisons += 1
				
				
	def leftChild(self,i):
		return 2 * i
		
	def rightChild(self,i):
		return 2 * i + 1
		

def seed(num): # num = 16 for 15 elments
	bs = BalancedSearch(num)	

	unique = []

# loop 1000 times
	for x in range(num-1):

# get a random number
		r = random.randint(0,1000)

# if it's not already in the list, enter it.
		if r not in unique:
			unique.append(r)

# Sort the list
	unique.sort()
	print(unique)
	print("Len",len(unique))
	bs.insert(unique)
bs = BalancedSearch(16)	
# Create a list to hold unique integers
unique = []

# loop 1000 times
for x in range(15):

# get a random number
	r = random.randint(0,1000)

# if it's not already in the list, enter it.
	if r not in unique:
		unique.append(r)

# Sort the list
unique.sort()
print(unique)
print("Len",len(unique))
bs.insert(unique)
bs.p()