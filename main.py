from schedule import Schedule

def main():
    schedule = Schedule()
    schedule.load_from_csv("courses.csv")

    while True:
        print("\nCourse Schedule Menu")
        print("1. Display All Courses")
        print("2. Search by Subject")
        print("3. Search by Subject & Catalog")
        print("4. Search by Instructor Last Name")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            schedule.print()

        elif choice == "2":
            subject = input("Enter subject: ")
            results = schedule.find_by_subject(subject)
            schedule.print(results)

        elif choice == "3":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog: ")
            results = schedule.find_by_subject_catalog(subject, catalog)
            schedule.print(results)

        elif choice == "4":
            name = input("Enter instructor last name: ")
            results = schedule.find_by_instructor_last_name(name)
            schedule.print(results)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
