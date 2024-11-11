from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests from the frontend

# Connect to a local SQLite database (or other DB if desired)
engine = create_engine("sqlite:///mydatabase.db")

@app.route('/api/data', methods=['GET'])
def get_data():
    # Query the database for data to display
    query = "SELECT * FROM my_table"  # Replace with your table name
    df = pd.read_sql(query, engine)
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
