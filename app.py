from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('reg.html')
@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['username']
    return render_template('greet.html',name=username)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
    