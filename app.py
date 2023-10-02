from flask import Flask, request, jsonify
import dynamic_pricing 
import joblib

app = Flask(__name__)

loaded_rf_model = joblib.load("random_forest_model.pkl")

@app.route('/', methods=['POST'])
def predict_amt():
    try:
        # Get data from the request
        data = request.get_json()

        # Use your machine learning model to make predictions
        prediction = loaded_rf_model.predict(data)  # Replace with your model code
    
        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=True)
