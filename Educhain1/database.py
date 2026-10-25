import sqlite3

DB_FILE = "educhain.db"


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                biometric TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certificates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                filename TEXT NOT NULL,
                certificate_hash TEXT NOT NULL,
                issuer TEXT NOT NULL,
                certificate_type TEXT NOT NULL
            )
        """)

        self.connection.commit()

    def register_student(self, student_id, name, password, biometric):
        try:
            self.connection.execute("""
                INSERT INTO students
                (student_id, name, password, biometric)
                VALUES (?, ?, ?, ?)
            """, (student_id, name, password, biometric))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_student(self, student_id):
        cursor = self.connection.execute("""
            SELECT student_id, name, password, biometric
            FROM students
            WHERE student_id = ?
        """, (student_id,))
        return cursor.fetchone()

    def add_certificate(self, student_id, filename, certificate_hash,
                        issuer, certificate_type):
        self.connection.execute("""
            INSERT INTO certificates
            (student_id, filename, certificate_hash, issuer, certificate_type)
            VALUES (?, ?, ?, ?, ?)
        """, (student_id, filename, certificate_hash, issuer, certificate_type))
        self.connection.commit()

    def get_certificates(self, student_id):
        cursor = self.connection.execute("""
            SELECT filename, certificate_hash, issuer, certificate_type
            FROM certificates
            WHERE student_id = ?
        """, (student_id,))
        return cursor.fetchall()

    def close(self):
        self.connection.close()
