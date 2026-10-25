import os
from certificate_hash import calculate_file_hash


def verify_certificate(db):
    print("\n========== CERTIFICATE VERIFICATION ==========")

    student_id = input("Student ID: ").strip()
    filename = input("Certificate file path: ").strip()

    if not os.path.isfile(filename):
        print("File not found.")
        return

    certificates = db.get_certificates(student_id)

    if not certificates:
        print("No certificate records found.")
        return

    current_hash = calculate_file_hash(filename)

    for certificate in certificates:
        stored_hash = certificate[1]

        if current_hash == stored_hash:
            print("\nCertificate VERIFIED")
            print("Issuer:", certificate[2])
            print("Type:", certificate[3])
            print("Stored Hash:", stored_hash)
            return

    print("\nCertificate verification FAILED.")
    print("The document may have been modified.")
