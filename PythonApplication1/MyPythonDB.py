import Employee as e


emp = e.Employee("Shah",200)

def mytesting():
	emp.displayEmployee()
	emp2 = e.Employee("Imran",200)
	emp2.displayEmployee()
	print("Employee %d" % emp.empCount)
	try:
		print("Employee.__doc__:", e.__doc__)
		print("Employee.__name__:", e.__name__)
		print("Employee.__module__:", e.__module__)
		##print("Employee.__bases__:", e.__bases__)
		##print("Employee.__dict__:", e.__dict__)
	except Exception as er: 
		print (er.args)
	finally:
		print("Code executed successfully!")

		
if __name__ == '__main__':
    mytesting() 