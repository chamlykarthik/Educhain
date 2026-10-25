import getpass


def student_login(db):
    print("\n========== STUDENT LOGIN ==========")

    student_id = input("Student ID: ").strip()
    password = getpass.getpass("Password: ")

    student = db.get_student(student_id)

    if student is None:
        print("Student not found.")
        return None

    # get_student() returns:
    # [0] student_id, [1] name, [2] password, [3] biometric
    if student[2] != password:
        print("Invalid password.")
        return None

    print("\n========== BIOMETRIC AUTHENTICATION ==========")
    print("Simulating biometric verification...")

    biometric = input("Enter registered biometric type: ").strip()

    if biometric.casefold() != str(student[3]).casefold():
        print("Biometric verification failed.")
        return None

    print("\nLogin successful.")
    return student
