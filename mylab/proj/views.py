import pdb
from proj import app
from flask import render_template, request
import querydb
import re
@app.route('/')
@app.route('/index')
def index():
	return "Hello World!"

@app.route('/render')
def render():
	title = "MMMEC Friends"
	friends = {'f1':'pawan', 'f2':'abhinav', 'f3':'gyanendra', 'f4':'divyank'}
	return render_template('index.html', title = title, friends = friends)

@app.route('/add_user',methods = ['POST'])
def add():
	fname = request.form["firstname"]
	print fname
	lname = request.form["lastname"]
	age = request.form["age"]
	sex = request.form["sex"]
	income = request.form["income"]
	#cmd = "insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (?,?,?,?,?)",(fname,lname,age,sex,income))
 	cmd = "insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s','%s',%d,'%s',%d)" %(fname,lname,int(age),sex,long(income))
	conn, cursor = querydb.conn()
	status = querydb.insert(cmd,conn, cursor)
	return status

	

@app.route('/show_user',methods = ['POST'])
def show():
	#pdb.set_trace()
	retValue = []
	user_name = request.form["username"]
	if user_name in ['All','all','ALL']:
	#if re.search ('^All$', user_name, re.I) != None:
		cmd = '''select * from EMPLOYEE'''
	else:
		print "else path"
		print user_name
		cmd = """select * from EMPLOYEE where FIRST_NAME = '%s'""" %(user_name)
	conn, cursor = querydb.conn()
	results = querydb.show(cmd,conn,cursor)
	#return "ok"
	for row in results:
		FIRST_NAME = row[0]
		LAST_NAME = row[1]
		AGE = row[2]
		SEX = row[3]
		INCOME = row[4]
		retValue.append("FIRST_NAME=%s, LAST_NAME=%s, AGE=%d, SEX=%s, INCOME=%d " % \
					(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME))
	return str(retValue)	
	
	








