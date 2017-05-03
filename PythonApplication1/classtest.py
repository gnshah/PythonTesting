import csv
import os.path

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
class Workwithcvs:
	##working procedure with CSV files

	cFilename = ""
	FileHandler = object
	Fileopen = False

	#def __init__(self, filename=None):
	#	if filename is not None:
	#		self.cFilename = filename	

	def openfile(self, filename=None):
		if filename is None:
			print("Please specify the File name")
		try:
			if os.path.isfile(filename):
				self.Fileopen = True	
				self.cFilename = filename
				print("File open and ready for operation")
			else:
				Print("File not found!")
				return
		except FileNotFoundError:
			print ("File " + self.cFilename + " not found!")
		
	def AddHeaderRecord(self):
		try:
			if self.Fileopen is True:
				with open(self.cFilename,"w",newline='') as self.FileHandler:
					filewriter = csv.writer(self.FileHandler, dialect='excel')
						##delimiter=',',quoting=csv.QUOTE_MINIMAL)
					filewriter.writerow(['Student Name','Student Class Name','Grade'])
			else:
				Print("File is not found / open")
			return
		except Exception as er: 
			print (er.args)


	def AddRecord(self,studentname,classname,grade):
		if self.Fileopen is True:
			try:
				with open(self.cFilename,"a",newline='') as self.FileHandler:
					filewriter = csv.writer(self.FileHandler, dialect='excel')
					filewriter.writerow([studentname,classname,grade])
			except Exception as er: 
				print (er.args)
		else:
			Print("File is not found / open")	
		return				

	def DisplayRecord(self):
		if self.Fileopen is True:
			try:
				with open(self.cFilename,"r") as self.FileHandler:
					filereader = csv.reader(self.FileHandler)
					for row in filereader:
						print (row)
			except Exception as er: 
				print (er.args)			
		else:
			Print("File is not found / open")	
		return				

		