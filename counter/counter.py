from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'funcode'

@app.route('/')         
def index():
    session['count'] += 1
    return render_template("index.html" , count = session['count'])

@app.route('/destroy_session')         
def destroy_session():
    session['count'] = 0
    return redirect('/')



# @app.route('/checkout', methods=['POST'])         
# def checkout()

if __name__=="__main__":   
    app.run(debug=True , port= 5001 )    