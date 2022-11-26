from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return ("Hello world")




@app.route('/celsius/<int:a>')
def celsius(a):
    number = a+273.15
    result = {
        "Celsius Value": a,
        "Coverted in Kelvin": number
    }
    return jsonify(result)

@app.route('/kelvin/<int:a>')
def kelvin(a):
    number = a-273.15
    result = {
        "Kelvin Value": a,
        "Coverted in Celsius": number
    }
    return jsonify(result)    

if __name__ == "__main__":
     app.run(debug=True)