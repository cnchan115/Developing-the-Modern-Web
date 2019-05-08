from flask import Flask, render_template, redirect, url_for, request
import pymysql
app = Flask(__name__)
app.static_folder='static'

@app.route("/Home")
def Home():
	return render_template('index.html')

@app.route("/Snacks")
def Snacks():
	return render_template('snacks.html')

@app.route("/Drinks")
def Drinks():
	return render_template('drinks.html')

@app.route("/AboutUs")
def AboutUs():
	return render_template('about.html')

@app.route("/Feedback")
def Feedback():
	return render_template('feedback.html')

@app.route("/Login")
def Login():
	return render_template('login.html')

@app.route("/reLogin")
def reLogin():
	return render_template('relogin.html')

@app.route("/result", methods=['POST','GET'])
def result():
	db=pymysql.connect(host="localhost",user="root",password="root",db="Delicioso")
	cursor=db.cursor()
	cursor.execute("SELECT `username`, `password` FROM `Members`")
	result=cursor.fetchall()
	if request.method == 'POST':
		userName=request.form.get("username")
		userPassword=request.form.get("password")
		for row in result:
			if userName == row[0] and userPassword == row[1]:
				return render_template('c_info.html', title="Hello %s" %userName)
				break
		else:
			return render_template('relogin.html')
		db.close()

@app.route("/signUp", methods=['POST','GET'])
def signUp():
	if request.method == 'POST':
		Name = request.form.get("username")
		Password = request.form.get("password")
		db=pymysql.connect(host="localhost",user="root",password="root",db="Delicioso")
		cursor=db.cursor()	
		sql = """INSERT INTO `Members`(`username`,`password`) VALUES ('%s','%s')""" %(Name,Password)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()

		return render_template('login.html')
		db.close()

@app.route("/Comment", methods=['POST','GET'])
def Comment():
	if request.method == 'POST':
		Username = request.form.get("name")
		Email = request.form.get("email")
		Comment = request.form.get("feedback")
		db=pymysql.connect(host="localhost",user="root",password="root",db="Delicioso")
		cursor=db.cursor()	
		sql = """INSERT INTO `Comments`(`name`,`email`,`feedback`) VALUES ('%s','%s','%s')""" %(Username,Email,Comment)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()

		return render_template('index.html')
		db.close()

if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0", port=8000)
