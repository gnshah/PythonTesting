import Employee as e
import classtest as a

emp = e.Employee("Shah",200)

##Polymorphism Example. 

def makeSound(animalType):
	animalType.sound()


def mytesting():
	emp.displayEmployee()
	emp2 = e.Employee("Imran",200)
	emp2.displayEmployee()
	print("Employee %d" % emp.empCount)
	try:


		print("Polymorphism Example")
		bearObj = a.Bear()
		dogObj = a.Dog()
		makeSound(bearObj)
		makeSound(dogObj)

		
		print("Inheritance Example")

		brian = a.User("Brian")
		brian.printName()

		diana = a.programmer("Diana")
		diana.printName()
		diana.doPython()

		print ("Encapsulation")

		car = a.Car()
		car.drive()
		car.setspeed(300)
		car.drive()

		##Functional Overloading
		car.setspeed(100,"Toyota")
		car.drive()
	

		##Reading Text File
		filename = open("mytextfile.txt","r")
		handle = filename.readlines()

		wordcount = 0 
		for line in handle:
			print (line)
			words = line.split(" ")
			for word in words:
				wordcount +=1

		print (wordcount)

		##CSV File TEST

		csvfile = WorkwithCSV()
		
	


		print("Employee.__doc__:", e.__doc__)
		print("Employee.__name__:", e.__name__)

	
		

	except Exception as er: 
		print (er.args)
	finally:
		print("Code executed successfully!")

		



		 
if __name__ == '__main__':
    mytesting() 
