import getpass


def register_student(db):
    print("\n========== STUDENT REGISTRATION ==========")

    student_id = input("Student ID: ").strip()
    name = input("Student Name: ").strip()

    if not student_id or not name:
        print("Student ID and name cannot be empty.")
        return

    password = getpass.getpass("Create Password: ")

    if not password:
        print("Password cannot be empty.")
        return

    print("\nBiometric Registration")
    print("1. Fingerprint")
    print("2. Face")
    print("3. Retina")

    biometric_types = {
        "1": "Fingerprint",
        "2": "Face",
        "3": "Retina"
    }

    biometric_choice = input("Select biometric: ").strip()
    biometric = biometric_types.get(biometric_choice)

    if biometric is None:
        print("Invalid biometric choice.")
        return

    result = db.register_student(
        student_id, name, password, biometric
    )

    if result:
        print("\nStudent registered successfully.")
        print("Biometric:", biometric)
    else:
        print("\nStudent ID already exists.")
