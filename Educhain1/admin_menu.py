from student_registration import register_student
from add_certificate import add_certificate
from verify_certificate import verify_certificate


def admin_menu(db, blockchain):
    while True:
        print("\n========== ADMIN / UNIVERSITY ==========")
        print("1. Register student")
        print("2. Add certificate")
        print("3. Verify certificate")
        print("4. Display blockchain")
        print("5. Check blockchain")
        print("6. Logout")

        choice = input("Choose option: ").strip()

        if choice == "1":
            register_student(db)

        elif choice == "2":
            add_certificate(db, blockchain)

        elif choice == "3":
            verify_certificate(db)

        elif choice == "4":
            blockchain.display_chain()

        elif choice == "5":
            if blockchain.verify_chain():
                print("\nBlockchain is valid.")
            else:
                print("\nBlockchain has been tampered with.")

        elif choice == "6":
            print("Admin logged out.")
            break

        else:
            print("Invalid option.")
