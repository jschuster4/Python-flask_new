from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/play')
def play():
    return render_template("index.html", num_boxes = 3, color = 'blue')  # Return the string 'Hello World!' as a response

@app.route('/play/<int:num_boxes>')
def level_2(num_boxes):
    return render_template('index.html' , num_boxes = num_boxes, color = 'blue')  # Return the string 'Hello World!' as a response

@app.route('/play/<int:num_boxes>/<string:color>')
def level_3( num_boxes , color ):
    return render_template('index.html' , num_boxes = num_boxes, color = color)  # Return the string 'Hello World!' as a response



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True , port = 5001 )    # Run the app in debug mode.