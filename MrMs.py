import sys
class Ex(Exception):
	"""class for handling exceptions"""
	def __init__(self, case): #initialize class
		errorText = ["Age < 0",
					"Rate < 0",
					"Name couldnt be a number",
					"Rate couldnt be NaN",
					"No persons to rate"]
		self.value = "Undefined error!"
		for i in range(0,len(errorText)):
			if(case==i): 
				self.value = "Error: "+errorText[i]
				break


class MrMs:
	"""class that contains basic functions for Mr and Ms"""
	
	def create(self, name, age, rate, sex):
		"""function that creates person"""
		#exceptions handling
		if(age<0):raise Ex(0) 
		if(rate<0):raise Ex(1)
		if(isinstance(name,int)):raise Ex(2)

		#set variables
		self.name = name
		self.age = age
		self.rate = rate
		self.sex = sex

	def setRate(self,rate):
		"""function that sets rate"""
		try:
			#exceptions handling
			if(isinstance(rate,int)==False):raise Ex(3)
			if(rate<0):raise Ex(1)
			
			#set rate
			self.rate =  rate
		except Ex as ex:
			print(ex.value)	
			sys.exit()


class Mister(MrMs):
	"""class to create Mister"""
	def __init__(self, name, age, rate=0): #initialize class
		try:
			super().create(name, age, rate, "male") #create mister
		except Ex as ex:
			print(ex.value)	
			sys.exit()
		
		

class Miss(MrMs):
	"""class to create Miss"""
	def __init__(self, name, age, rate=0): #initialize class
		try:
			super().create(name, age, rate, "female") #create miss
		except Ex as ex:
			print(ex.value)	
			sys.exit()	

class Rate:
	"""class to rate all candidates"""
	def __init__(self, *persons): #initialize class
		try:
			if(len(persons)==0):raise Ex(4) #exceptions handling
			self.candidates = persons
		except Ex as ex:
			print(ex.value)	
			sys.exit()	

	def showWinner(self):
		"""function that shows winner"""
		winner = self.candidates[0] #set first candidate as winner
		for i in range(0,len(self.candidates)):
			if(self.candidates[i].rate > winner.rate):
				winner = self.candidates[i] #set person with highest rating as winner
		print("Congratulations, "+winner.name+" wins!")

	def candidatesSort(self,by="rate"):
		""" function that sorts all candidates"""
		rateTable = list(self.candidates)
		if(by=="rate"):
			#sort candidates by rate
			rateTable.sort(key = lambda x: x.rate)
			rateTable.reverse()
		if(by=="name"):
			#sort candidates by name
			rateTable.sort(key = lambda x: x.name)
		if(by=="age"):
			#sort candidates by age
			rateTable.sort(key = lambda x: x.age)
			rateTable.reverse()
		print("-------------- Rate Table --------------")
		for i in range(0,len(self.candidates)):
			print(rateTable[i].name+" "+str(rateTable[i].age)+" years, rate: "+str(rateTable[i].rate))
				
