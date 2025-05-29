# This file contains the main CLI entry point.
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))

from lib.cli.user_menu import UserMenu
from lib.cli.job_menu import JobMenu
from lib.cli.application_menu import ApplicationMenu
from lib.database.db import init_db, SessionLocal

def main():
    init_db()
    session = SessionLocal()
    user_menu = UserMenu(session)
    job_menu = JobMenu(session)
    application_menu = ApplicationMenu(session)

    while True:
        print("\n=== Skills-Link-Jobs CLI ===")
        print("1. User Management")
        print("2. Job Management")
        print("3. Application Management")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            user_menu.show_menu()
        elif choice == "2":
            job_menu.show_menu()
        elif choice == "3":
            application_menu.show_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()