import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('Patient.db')
        print(f'Successful connection to SQLite database version {sqlite3.version}')
        return conn
    except Error as e:
        print(e)

    return conn

def create_patient_table(conn):
    """ create a table in the SQLite database """
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS patients
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL,
                      phone INTEGER NOT NULL,
                      weight INTEGER NOT NULL,
                      email TEXT NOT NULL,
                      status TEXT NOT NULL,
                      dateOfBirth DATE NOT NULL,
                      reportDate DATE NOT NULL,
                      Prediction REAL NOT NULL
                      )''')
        print('Table created successfully')
    except Error as e:
        print(e)

def create_medical_data_table(conn):
    """ create a medical data table in the SQLite database """
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS medical_data
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      patient_id INTEGER NOT NULL,
                      radius_mean REAL NOT NULL,
                      texture_mean REAL NOT NULL,
                      perimeter_mean REAL NOT NULL,
                      area_mean REAL NOT NULL,
                      smoothness_mean REAL NOT NULL,
                      compactness_mean REAL NOT NULL,
                      concavity_mean REAL NOT NULL,
                      concave_points_mean REAL NOT NULL,
                      symmetry_mean REAL NOT NULL,
                      fractal_dimension_mean REAL NOT NULL,
                      radius_se REAL NOT NULL,
                      texture_se REAL NOT NULL,
                      perimeter_se REAL NOT NULL,
                      area_se REAL NOT NULL,
                      smoothness_se REAL NOT NULL,
                      compactness_se REAL NOT NULL,
                      concavity_se REAL NOT NULL,
                      concave_points_se REAL NOT NULL,
                      symmetry_se REAL NOT NULL,
                      fractal_dimension_se REAL NOT NULL,
                      radius_worst REAL NOT NULL,
                      texture_worst REAL NOT NULL,
                      perimeter_worst REAL NOT NULL,
                      area_worst REAL NOT NULL,
                      smoothness_worst REAL NOT NULL,
                      compactness_worst REAL NOT NULL,
                      concavity_worst REAL NOT NULL,
                      concave_points_worst REAL NOT NULL,
                      symmetry_worst REAL NOT NULL,
                      fractal_dimension_worst REAL NOT NULL,
                      FOREIGN KEY (patient_id) REFERENCES patients (id))''')
        print('Medical data table created successfully')
    except Error as e:
        print(e)

conn = create_connection()
create_patient_table(conn)
create_medical_data_table(conn)
conn.close()
