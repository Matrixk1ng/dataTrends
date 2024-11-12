from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enables CORS for cross-origin requests

# AWS RDS Database connection information
db_user = 'your_rds_username'
db_password = 'your_rds_password'
db_host = 'your_rds_endpoint'  # Example: database-1.xxxxxxxx.us-east-1.rds.amazonaws.com
db_name = 'your_database_name'

# PostgreSQL connection string
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}')

@app.route('/api/data', methods=['GET'])
def get_data():
    query = "SELECT * FROM my_table"  # Replace with your actual table name
    df = pd.read_sql(query, engine)
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
