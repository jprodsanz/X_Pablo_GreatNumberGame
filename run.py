from flask import Flask, render_template, url_for, request, redirect,session
import random

app = Flask(__name__)  
app.config ['SECRET_KEY'] = '05a21ff3e3c04f281944e3f8'

@app.route('/')
@app.route('/home')                  
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)

    return render_template('index.html')

@app.route('/guess', methods=['POST'])      
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')        
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)  