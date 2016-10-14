from flask import Flask,render_template,request,redirect,session,flash
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def idx():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def submit():
    if len(request.form['name']) < 1:
    	flash('Name can not be empty!')
    elif len(request.form['comment']) < 1:
    	flash('Comment can not be empty!')	
    elif len(request.form['comment']) > 121:
    	flash('Comment is larger than 120 characters!')
    else:	
    	print request.form
    	flash('Success!')
    return render_template('result.html', data=request.form)
app.run(debug=True)	