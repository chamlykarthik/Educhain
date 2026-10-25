import getpass

from database import Database
from blockchain import EduChain
from admin_menu import admin_menu
from student_login import student_login
from student_menu import student_menu


ADMIN_PASSWORD = "admin123"


def main():
    db = Database()
    blockchain = EduChain()

    print("\n========================================")
    print("       EDUCHAIN EDUCATION SYSTEM")
    print("========================================")

    try:
        while True:
            print("\n========== MAIN MENU ==========")
            print("1. University / College")
            print("2. Student")
            print("3. Exit")

            choice = input("Choose option: ").strip()

            if choice == "1":
                password = getpass.getpass("Admin password: ")

                if password == ADMIN_PASSWORD:
                    admin_menu(db, blockchain)
                else:
                    print("Invalid admin password.")

            elif choice == "2":
                student = student_login(db)

                if student:
                    student_menu(db, blockchain, student)

            elif choice == "3":
                print("Thank you for using EduChain.")
                break

            else:
                print("Invalid option. Please choose 1, 2, or 3.")

    except KeyboardInterrupt:
        print("\n\nProgram interrupted.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
