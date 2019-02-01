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
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
