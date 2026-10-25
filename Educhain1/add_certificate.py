import os
from certificate_hash import calculate_file_hash


def add_certificate(db, blockchain):
    print("\n========== ADD CERTIFICATE ==========")

    student_id = input("Student ID: ").strip()
    student = db.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    filename = input("Certificate file path: ").strip()

    if not os.path.isfile(filename):
        print("Certificate file not found.")
        return

    certificate_type = input("Certificate type: ").strip()
    issuer = input("College / University name: ").strip()

    if not certificate_type or not issuer:
        print("Certificate type and issuer cannot be empty.")
        return

    certificate_hash = calculate_file_hash(filename)

    db.add_certificate(
        student_id,
        os.path.basename(filename),
        certificate_hash,
        issuer,
        certificate_type
    )

    blockchain.add_certificate(
        student_id,
        certificate_hash,
        issuer,
        certificate_type
    )

    print("\nCertificate added successfully.")
    print("Certificate Hash:")
    print(certificate_hash)
