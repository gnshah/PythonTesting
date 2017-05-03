
import csv

class Bear(object):
 	def sound(self):
		 print("Broarrr")

class Dog(object):
	def sound(self):
		print("Woof Woof!")


		##Inheritance Exmapl 
class User:
	name =""

	def __init__(self, name):
		self.name=name

	def printName(self):
		print("Name = " + self.name)

class programmer(User):
	def __init__(self, name):
		self.name = name 

	def doPython(self):
		print ("Programming Python")
	
	##Encapsulation	
class Car:
	__maxspeed = 0
	__name = ""
	
	def __init__(self):
		self.__maxspeed = 400
		self.__name = "Audi Q8"

	def drive(self):
		print ("I am Driving " + self.__name + " with speed of " + str(self.__maxspeed) + "mile") 

	#def setspeed(self, speed, name=None):

	#	self.__maxspeed = speed

	def setspeed(self, speed, name=None):
		if (name is None):
			self.__maxspeed=speed
		else:
			self.__maxspeed= speed
			self.__name = name


	##Working with CSV Files
class WorkwithCSV:
	##working procedure with CSV files

	__cFilename = ""
	__FileHandler = object
	__Fileopen = False

	#def __init__(self, filename=None):
	#	if filename is not None:
	#		self.__cFilename = filename	

	def openfile(self, filename=None):
		if filename is None:
			print("Please specify the File name")
		try:
			self.__cFilename = filename
			self.__FileHandler = open(self.__cFilename,"wb")
			self.__FileHandler.close()

		except FileNotFoundError:
			print ("File " + self.__cFilename + " not found!")
		finally:
			print("File open and ready for operation")
			return
	
		def AddHeaderRecord(self):
			if self.__Fileopen is True:
				with open(self.__cFilename,"wb") as self.__FileHandler:
					filewriter = csv.writer(self.__FileHandler, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
					filewriter.writerow(['Student Name','Student Class Name','Grade'])
			else:
				Print("File is not found / open")
			return
	
	def AddRecord(self,studentname,classname,grade):
		if self.__Fileopen is True:
			with open(self.__cFilename,"wb") as self.__FileHandler:
				filewriter = csv.writer(self.__FileHandler, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([studentname,classname,grade])
		else:
			Print("File is not found / open")	
		return				

	def DisplayRecord(self):
		if self.__Fileopen is True:
			with open(self.__cFilename,"wb") as self.__FileHandler:
				filereader = csv.reader(self.__FileHandler)
				for row in filereader:
					print (row)			
		else:
			Print("File is not found / open")	
		return				

		