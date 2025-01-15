from flask import Flask, jsonify, request
import util

app = Flask(__name__)

util.load_saved_artifacts()


@app.route('/get_location')
def get_location():
    response = jsonify({
        'locations': util.get_location()
    })
    response.headers.add('access-control-allow-origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('access-control-allow-origin', '*')
    return response


if __name__ == "__main__":
    print("starting python flask server for home price prediction...")
    app.run()
