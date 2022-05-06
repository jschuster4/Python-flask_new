from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def checkerboard8():
    return render_template("index.html" , number_rows = 8 , number_columns = 8)  # Return an 8x8 checker board

@app.route('/<int:number_rows>')
def checkerboard_custom_rows(number_rows):
    return render_template("index.html", number_rows = number_rows , number_columns = 8)  

@app.route('/<int:number_rows>/<int:number_columns>')
def checkerboard_custom_size(number_rows, number_columns):
    return render_template("index.html", number_rows = number_rows , number_columns = number_columns)  

@app.route('/<int:number_rows>/<int:number_columns>/<string:color1>/<string:color2>')
def checkerboard_custom(number_rows, number_columns, color1, color2):
    return render_template("index.html", number_rows = number_rows , number_columns = number_columns, color1 = color1, color2 = color2)  



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True , port = 5001 )    # Run the app in debug mode.