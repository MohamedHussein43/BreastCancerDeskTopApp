import sqlite3
from sqlite3 import Error
from PyQt5 import QtWidgets, QtGui
class Backdatabase():
    def __init__(self, conn):
        self.conn = conn

    def create_patient_table(self,conn):
        """ create a table in the SQLite database """
        try:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS patients
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        phone TEXT NOT NULL,
                        weight INTEGER NOT NULL,
                        email TEXT NOT NULL,
                        status TEXT NOT NULL,
                        reportDate DATE NOT NULL,
                        Prediction REAL NOT NULL
                        )''')
            print('Table created successfully')
        except Error as e:
            print(e)

    def create_medical_data_table(self,conn):
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

    def insert_data_patient_table(self,conn, patientData):
        # Create a connection to the SQLite database
        # Create a cursor object
        cursor = conn.cursor()

        # Define the SQL query to insert a new record
        query = "INSERT INTO patients(name, age, phone, weight, email, status, reportDate, Prediction) VALUES(?,?,?,?,?,?,?,?)"

        # Execute the SQL query
        if len(patientData) == 8:
            cursor.execute(query, patientData)
            print("Data has been added succecfully!")
            print(patientData)
        else:
            print("There are some missing data")

        # Commit the changes to the database
        conn.commit()

    def Deletepatient(self, conn, ID):
        c = conn.cursor()
        c.execute("DELETE FROM patients WHERE id=?", (ID,))
        conn.commit()
        conn.close()

    def retreve_data_patient_table(self,conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients")
        rows = cursor.fetchall()
        l=[]
        for row in rows:
            l.append(list(row))
        return l

    def delete_data_patient_table(self,conn):
        c = conn.cursor()

        # Delete all rows from the 'patients' table
        c.execute("DELETE FROM patients")

        # Commit the changes
        conn.commit()

    def list_of_lists_to_list_of_dicts(self,conn):
        patients_data = self.retreve_data_patient_table(conn)
        keys = ['id','name', 'age', 'phone', 'weight', 'email', 'status', 'reportDate', 'Prediction']
        patients_dict_list = []
        for patient in patients_data:
            patient_dict = dict(zip(keys, patient))
            patients_dict_list.append(patient_dict)
        return patients_dict_list
    def insert_medical_data_table(self,conn, medicalpatientData):
        cursor = conn.cursor()
        query = "INSERT INTO medical_data(patient_id,radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,fractal_dimension_mean     ,radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se            , radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst,concave_points_worst, symmetry_worst,fractal_dimension_worst) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        if len(medicalpatientData) == 30:
            cursor.execute(query, medicalpatientData)
            print("Medical Data has been added succecfully!")
            print(medicalpatientData)
        else:
            print("There are some missing data")
        conn.commit()

#-----main-------------
class Database():
    def __init__(self):
        self.conn = self.create_connection()
        self.database = Backdatabase(self.conn)
        #self.database.create_patient_table(self.conn)
        '''row1 = ["John Doe", 30, "555-1234", 75.5, "john.doe@example.com", "active", "1992-01-01", "2023-05-06", 0.8]
        row2 = ["Jane Smith", 45, "555-5678", 62.2, "jane.smith@example.com", "inactive", "1977-04-12", "2023-05-06", 0.2]
        row3 = ["Bob Johnson", 50, "555-9876", 85.1, "bob.johnson@example.com", "active", "1972-08-29", "2023-05-06", 0.5]
        patientData = [row1, row2, row3]
        self.database.insert_data_patient_table(self.conn, patientData)'''
    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect('../Database/Patient.db')
            print(f'Successful connection to SQLite database version {sqlite3.version}')
            return conn
        except Error as e:
            print(e)

        return conn
    
    def deletePatient(self, ID):
        self.database.Deletepatient(self.conn, ID)
        print("deleted succecfully: ",ID)
    def setMedicalData(self,Data):
        self.database.insert_medical_data_table(self.create_connection(), Data)
        print("medical data add succecfully!")
        print(Data)
    def getPatients(self):
        data = self.database.list_of_lists_to_list_of_dicts(self.conn)
        self.conn.close()
        return data
    def insertPatient(self, data):
        self.database.insert_data_patient_table(self.conn, data)
        print("data inserted correctly")

    
#create_patient_table(conn)
#create_medical_data_table(conn)
#delete_data_patient_table(conn)
'''d = Database()
conn = d.create_connection()
b = Backdatabase(conn)
row1 = ["Emma Doe", 30, "555-1234", 75.5, "john.doe@example.com", "single", "2023-05-06", 0.8]
row2 = ["Sophia Smith", 45, "555-5678", 62.2, "jane.smith@example.com", "married", "2023-05-06", 0.2]
row3 = ["Ava Johnson", 50, "555-9876", 85.1, "bob.johnson@example.com", "married", "2023-05-06", 0.5]
patientData = [row1, row2, row3]
for i in patientData:
    b.insert_data_patient_table(conn, i)
print("===================================================================")
d = Database()
patients_dict_list = d.getPatients()
print(patients_dict_list)
print("===================================================================")
'''
'''d = Database()
cnn = d.create_connection()
b = Backdatabase(cnn)
b.create_patient_table(cnn)'''



