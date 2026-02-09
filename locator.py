from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim
#pip install geopy
#https://opencagedata.com/dashboard#geocoding
##pip install geopy
#for replit https://replit.com/@codybuddy2023/location-api#main.py
app = Flask(__name__)

# Initialize Nominatim geolocator (OpenStreetMap)
geolocator = Nominatim(user_agent="locate_me_app")

@app.route("/")
def home():
    return render_template("location.html")

# Geocoding route
@app.route("/geocode", methods=["POST"])
def geocode():
    data = request.get_json()
    location_name = data.get("location")

    if not location_name:
        return jsonify({"error": "Location is required"}), 400

    try:
        location = geolocator.geocode(location_name)
        if location:
            return jsonify({
                "latitude": location.latitude,
                "longitude": location.longitude,
                "display_name": location.address
            })
        else:
            return jsonify({"error": "Location not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
