from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
@app.route('/success/<name>')
def success(name):
	#return render_template('success.html',name=user)
	return render_template('success.html',name=name)
@app.route('/')
def index():
	return render_template('log1.html')
@app.route('/check1',methods=['POST','GET'])
def check1():
	if request.method =='POST':
		user = request.form['nm']
		return redirect(url_for('success',name=user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success',name=user))
