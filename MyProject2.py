import sqlite3

conn = sqlite3.connect('myfile.db')
c = conn.cursor()

c.execute('CREATE TABLE Accounts (policeID INTEGER PRIMARY KEY AUTOINCREMENT,name text NOT NULL, age Number(2) NOT NULL, email text NOT NULL, passw text NOT NULL)')
c.execute('CREATE TABLE Branch (branchID INTEGER PRIMARY KEY AUTOINCREMENT, branch_name Varchar NOT NULL)')
c.execute('CREATE TABLE CriminalInfo (criminalID INTEGER PRIMARY KEY AUTOINCREMENT, name text NOT NULL, age Number(2) NOT NULL, crime text NOT NULL, date Date NOT NULL, victim text NOT NULL)')
c.execute('CREATE TABLE Victims (victimID INTEGER PRIMARY KEY AUTOINCREMENT, victim text NOT NULL, victim_age Number(2) NOT NULL)')
c.execute('CREATE TABLE Address (victimID References Victims (victimID) On Delete Cascade, victim_address text NOT NULL)')

c.execute('INSERT INTO Accounts (name, age, email, passw) VALUES ("Arpit", 19, "arpit@gmail.com", "12345")')
#c.execute('INSERT INTO Accounts (name, age, email, passw) VALUES ("", 19, "arpit@gmail.com", "")')

c.execute('INSERT INTO Branch (branch_name) VALUES("Koramangala")')
c.execute('INSERT INTO Branch (branch_name) VALUES("Indiranagar")')
c.execute('INSERT INTO Branch (branch_name) VALUES("Rajajinagar")')
c.execute('INSERT INTO Branch (branch_name) VALUES("MG Road")')
c.execute('INSERT INTO Branch (branch_name) VALUES("HSR Layout")')
c.execute('INSERT INTO Branch (branch_name) VALUES("RR Nagar")')
c.execute('INSERT INTO Branch (branch_name) VALUES("Whitefield")')
c.execute('INSERT INTO Branch (branch_name) VALUES("BTM Layout")')
c.execute('INSERT INTO Branch (branch_name) VALUES("Jayanagar")')
c.execute('INSERT INTO Branch (branch_name) VALUES("Electronic City")')
c.execute('INSERT INTO Branch (branch_name) VALUES("Bellandur")')
c.execute('INSERT INTO Branch (branch_name) VALUES("Banashankari")')

c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Manish", 56, "Theft", "12/31/20", "Shreyas")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Kamal", 43, "Murder", "12/4/19", "Sonal")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Sonam", 32, "Robbery", "10/16/19", "Komal")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Rajesh", 34, "Child Abuse", "12/31/20", "Sunali")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Abhimanyu", 29, "Kidnapping", "12/16/19", "Kartik")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Keshav", 39, "Genocide", "12/31/20", "Aditya and Others")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Aadi", 51, "Torture", "7/17/19", "Bhuvan")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Gautami", 21, "Theft", "5/8/19", "Abhyuday")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Aaquib", 43, "Human Trafficking", "11/6/19", "Sana and Others")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Amit", 29, "Rape", "11/22/18", "Komal")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Ajey", 35, "Arson", "1/17/18", "Abhishek")')
c.execute('INSERT INTO CriminalInfo (name, age, crime, date, victim) VALUES("Ashish", 45, "Drug Trafficking", "3/21/18", "So Many")')

c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Abhyuday", 25)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Bhuvan", 34)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Komal", 27)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Kartik", 43)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Avneet", 35)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Abhimanyu", 42)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Manish", 37)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Ashish", 23)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Abhishek", 45)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Sonal", 15)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Siddhant", 38)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Sunali", 32)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Shreyas", 26)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Keshav", 58)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Rajesh", 35)')
c.execute('INSERT INTO Victims (victim, victim_age) VALUES("Faizal", 44)')

c.execute('INSERT INTO Address VALUES (1, "304 MG Road")')
c.execute('INSERT INTO Address VALUES (2, "67 Koramangala")')
c.execute('INSERT INTO Address VALUES (3, "5 Feet Road")')
c.execute('INSERT INTO Address VALUES (4, "RR Nagar")')
c.execute('INSERT INTO Address VALUES (5, "97 Jayanagar")')
c.execute('INSERT INTO Address VALUES (6, "Electronic City")')
c.execute('INSERT INTO Address VALUES (7, "21 Koramangala")')
c.execute('INSERT INTO Address VALUES (8, "RR Nagar")')
c.execute('INSERT INTO Address VALUES (9, "Gulbarga")')
c.execute('INSERT INTO Address VALUES (10, "86 MG Road")')
c.execute('INSERT INTO Address VALUES (11, "Kolar")')
c.execute('INSERT INTO Address VALUES (12, "HSR Layout")')
c.execute('INSERT INTO Address VALUES (13, "25 Banashankari")')
c.execute('INSERT INTO Address VALUES (14, "Hyderabad")')
c.execute('INSERT INTO Address VALUES (15, "92 Rajajinagar")')
c.execute('INSERT INTO Address VALUES (16, "Tumkur")')

# Trigger
c.execute('CREATE TRIGGER trigg1 '
          'BEFORE INSERT ON Accounts '
          'BEGIN SELECT CASE WHEN NEW.email NOT LIKE "%_@_%._%" '
          'THEN RAISE (ABORT, "Invalid") '
          'END; '
          'END;')

c.execute('CREATE TRIGGER trigg2 '
          'BEFORE INSERT ON Accounts '
          'BEGIN SELECT CASE WHEN NEW.age NOT BETWEEN 18 AND 70 '
          'THEN RAISE (ABORT, "Invalid") '
          'END; '
          'END;')

conn.commit()
conn.close()
print('Table Created !')
