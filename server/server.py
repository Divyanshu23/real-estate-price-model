from flask import Flask, request, jsonify
import utils

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': utils.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_area_types', methods=['GET'])
def get_area_types():
    response = jsonify({
        'area_types': utils.get_area_types()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/predict_prices", methods=["GET","POST"])
def get_prices():
  total_sqft = float(request.form['total_sqft'])
  location = request.form['location']
  area = request.form["area"]
  bedrooms = int(request.form['bedrooms'])
  bathrooms = int(request.form['bathrooms'])
  balcony = int(request.form['balcony'])

  response = jsonify({
        'estimated_price': utils.predict_prices(location, area, total_sqft, bedrooms, bathrooms, balcony)
    })
  response.headers.add('Access-Control-Allow-Origin', '*')

  return response

if __name__ == "__main__":
  print("Starting Python Flask Server...")
  utils.get_locations()
  app.run()