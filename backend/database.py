import sqlite3

conn = sqlite3.connect('barcodes.db')

print("Connected")

conn.execute(''' 
                CREATE TABLE DESCRIPTION 
                (
                    BARCODENUMBER INT PRIMARY KEY NOT NULL,
                    PRODUCTNAME TEXT NOT NULL,
                    PRODUCTAMOUNT INT NOT NULL
                );
''')

conn.execute('''
                CREATE TABLE AMOUNTHISTORY
                (
                    DATE TEXT NOT NULL,
                    AMOUNT INT NOT NULL,
                    TIME TEXT
                );
''')

print("Created")

