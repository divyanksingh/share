import MySQLdb
import re
from flask import render_template
#@staticmethod
# Open database connection
def conn():
	db = MySQLdb.connect(host="localhost",user ="root",passwd = "welcome12",db = "friends")
#NOTE:  THESE details must be set from cmd prompt sql including database name

# prepare a cursor object using cursor() method
	cursor = db.cursor()
	return db, cursor


def insert(query, db, cursor):
	print query
	try:
		cursor.execute(query)
		db.commit()
		status = "Success"
		#db.close()
		#return "Record inserted successfully"
	except:
		db.rollback()
		status = "Fail"
		#db.close()
		#return render_template('error.html', Msg = "Record insert failed")
	finally:
		db.close()
		return status
		
def show(query,db,cursor):
	print query
	try:
		cursor.execute(query)
		results = cursor.fetchall()
		db.close()
		return results
	except:
		db.close()
		return render_template('error.html', Msg = "You have an error")
		

