from flask import Flask

app = Flask(__name__)

@app.route("/") # @ sign wraps the code for the route
def hello_world():
    return "<p>Hello, World!</p>"

# venv/Scripts/Activate.ps1


#@app.route("/predict", methods =["POST"]) # @ sign wraps the code for the route
#def predict():
    #data = request.get_json()
    #clf.predict(data)
    #return predictions #json
    #predictions = [[1]]


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
