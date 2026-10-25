from student_history import show_student_records


def student_menu(db, blockchain, student):
    student_id = student[0]

    while True:
        print("\n========== STUDENT PORTAL ==========")
        print("Welcome,", student[1])
        print("1. View Education History")
        print("2. View Blockchain")
        print("3. Logout")

        choice = input("Choose option: ").strip()

        if choice == "1":
            show_student_records(db, blockchain, student_id)

        elif choice == "2":
            blockchain.display_chain()

        elif choice == "3":
            print("Student logged out.")
            break

        else:
            print("Invalid option.")
