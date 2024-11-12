from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import psycopg2.extras


try:
    conn = psycopg2.connect(
        dbname='',  # Change to the actual database name if needed
        user='',
        password='',  # Make sure this is correct
        host='database-1.cpae2o6w06c0.us-east-2.rds.amazonaws.com',
        port='5432',
        sslmode='require'
    )
    print("Database connected")
except Exception as ex:
    print(ex)
    print("Database not connected")


#nt_cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)


#app = Flask(__name__)
#CORS(app)  # Enables CORS for cross-origin requests

# AWS RDS Database connection information
#db_user = 'obinna'
#db_password = 'flame86362'
#db_host = 'database-1.cpae2o6w06c0.us-east-2.rds.amazonaws.com'  # Example: database-1.xxxxxxxx.us-east-1.rds.amazonaws.com
#db_name = 'postgresql'

# PostgreSQL connection string
#engine = create_engine(f'postgresql+psycopg2://obinna:flame86362@database-1.cpae2o6w06c0.us-east-2.rds.amazonaws.com/database-1')

#@app.route('/api/data', methods=['GET'])
#def get_data():
#    query = "SELECT * FROM my_table"  # Replace with your actual table name
#    df = pd.read_sql(query, engine)
#    data = df.to_dict(orient='records')
#    return jsonify(data)
#
#if __name__ == '__main__':
#    app.run(debug=True)
