def show_student_records(db, blockchain, student_id):
    print("\n========== EDUCATION HISTORY ==========")

    student = db.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("Student ID:", student[0])
    print("Name:", student[1])
    print("Biometric:", student[3])

    certificates = db.get_certificates(student_id)

    if not certificates:
        print("\nNo certificates available.")
        return

    print("\nEducation Records:")

    for certificate in certificates:
        filename, certificate_hash, issuer, certificate_type = certificate

        print("\n--------------------------------")
        print("Document:", filename)
        print("Type:", certificate_type)
        print("Issuer:", issuer)
        print("Hash:", certificate_hash)

    records = blockchain.find_student_records(student_id)

    print("\nBlockchain Verification:")

    if not records:
        print("No blockchain records found.")
    else:
        for record in records:
            print(
                record["certificate_type"],
                "->",
                record["issuer"]
            )

    print("\nBlockchain valid:", blockchain.verify_chain())
