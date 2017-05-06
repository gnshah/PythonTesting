
import pypyodbc
 

class SQLDB:
	
	ConnectionString = ""

	def __init__(self, connection):
		self.ConnectionString=connection

	def DisplayRecord(self):

		try:

			con = pypyodbc.Connection(self.ConnectionString)
			cursor = con.cursor()
			
			SQLCommand = "Select * from Student "
			cursor.execute(SQLCommand)

			Results = cursor.fetchall()
			for row in Results:
				print(row)

		except pypyodbc.DatabaseError as e:
			print ("Error %s" %e)

		finally:
			if con:
				con.close

