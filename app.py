from flask import *

app=Flask(__name__)

@app.route('/')
def func():
    
    return "this is my first flask application after debug mode let us do this agian hey debug mode is on wow!!"
@app.route('/second')

def secfunction():
    return "this is my second function in pyhton flask frame work"

def addurlmethod():
    return "this is to show add url method"
app.add_url_rule('/name','addurlmethod',addurlmethod)

def home1():
    return "this is second method to show add url method"
app.add_url_rule('/second1','home1',home1)

@app.route('/names/<name>')
def function(name):
    return "Hello %s!!" %name

@app.route('/world/<name>')
def function1(name):
    return "this is world of %s" %name

@app.route('/blog1/<int:blogno>')
def blog(blogno):
    return "the total number of blogs are %s" %blogno
 

@app.route('/flask')
def fl():
    return "this is flask function"

@app.route('/python/')
def py():
    return "this is python function"


#url_for () function

@app.route('/admin')
def adminfunction():
    return "This function is for admin"
@app.route('/user/<name>')
def userfunction(name):
    return "this function is for user %s" %name 
@app.route('/wrong')
def wrongfunction():
    return "you have given wrong input"
@app.route('/fetch/<name>')
def fetchfunction(name):
    if name=="admin":
        return redirect(url_for('adminfunction'))
    elif name=='user':
        return redirect(url_for('userfunction',name="nandini"))
    elif name not in ['admin','user']:
        return redirect(url_for('wrongfunction'))
    
@app.route('/welcome/<name>')
def welcome(name):
    return "welcome %s" % name
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        user=request.form('nm')
        return redirect(url_for('welcome',name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('welcome',name=user))






if __name__=="__main__":
    app.run(debug=True)