from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
all_QuotesName = []
all_QuotesAge = []
all_QuotesMessage = []

@app.route('/',methods = ['GET','POST']) # What methods are needed?
def home():
	try:
		if request.method == 'GET':
			return render_template('home.html')
		else:
			login_session['name'] = request.form['name']
			login_session['age'] = request.form['age']
			login_session['message'] = request.form['message']
			all_QuotesName.append(login_session['name'])
			all_QuotesAge.append(login_session['age'])
			all_QuotesMessage.append(login_session['message'])
			return render_template('thanks.html')
	except:
		return render_template('error.html')
	
length = len(all_QuotesName)


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html',hi = length,name=all_QuotesName,age=all_QuotesAge,message=all_QuotesMessage) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)