from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'funcode'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])         
def process_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')         
def result():
    return render_template("result.html", 
        name = session['name'],
        location = session['location'],
        language = session['language'],
        comments = session['comments'])


# @app.route('/process' , methods=['POST'])         
# def process_form():

#     session['name'] = request.form['name']
#     session['location'] = request.form['location']
#     session['language'] = request.form['language']
#     session['comments'] = request.form['comments']
#     return render_template('result.html' , name = session['name'],
#         location = session['location'],
#         language = session['language'],
#         comments = session['comments'])
# # @app.route('/results')         
# def show():
#     return render_template("results.html", name = session['name'],
#         location = session['location'],
#         language = session['language'],
#         comments = session['comments'])



# @app.route('/checkout', methods=['POST'])         
# def checkout()

if __name__=="__main__":   
    app.run(debug=True , port= 5001 )    