from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="my_location_app")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask Location API is running!"})

@app.route("/get-location", methods=["POST"])
def get_location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")

    if not lat or not lon:
        return jsonify({"error": "Latitude and Longitude are required."}), 400

    try:
        location = geolocator.reverse(f"{lat}, {lon}")
        if location:
            return jsonify({"address": location.address})
        else:
            return jsonify({"error": "Location not found."}), 444
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)