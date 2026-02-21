from api_request import fetch_data
import json
import psycopg2

def connect_to_db():
    print("Connecting to database...")
    try:
        conn = psycopg2.connect(
            host = "127.0.0.1",
            port = 62024,
            dbname = "weather_data",
            user = "airflow",
            password = "airflow"
        )
        return conn

    except psycopg2.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        raise  # Re-raise the exception to signal failure

connect_to_db()

def create_table(conn):
    print("Creating table if not exists...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city VARCHAR(100),
                temperature FLOAT,
                Weather_descriptions TEXT,
                aqi JSONB,
                humidity INT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred while creating the table: {e}")
        raise  # Re-raise the exception to signal failure

conn = connect_to_db()
create_table(conn)

def insert_records(conn, data):
    print("Insert weather data into the database...")
    try:
       # breakpoint()
        print(type(data))
        print(data.keys())
        print(json.dumps(data, indent=2))
        weather = data['current'] # why error?
        location = data['location']
        
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
            city,
            temperature,
            Weather_descriptions,
            aqi,
            humidity
        ) VALUES (%s, %s, %s, %s, %s)
        """, (
        location['name'],
        weather['temperature'],
        weather['weather_descriptions'][0],
        json.dumps(weather['air_quality']),
        weather['humidity']
    ))
        conn.commit()
        print("Records inserted successfully.")

    except psycopg2.Error as e:
        print(f"An error occurred while inserting records: {e}")
        raise

data = fetch_data()
conn = connect_to_db()
create_table(conn)
insert_records(conn, data)