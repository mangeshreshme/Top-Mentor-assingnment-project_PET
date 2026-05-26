import pickle


'''BOOK FUNCTIONS'''

def create_book():
    f = open("book.dat", "ab")
    book = {}

    book['id'] = int(input("Enter Book ID: "))
    book['name'] = input("Enter Book Name: ")
    book['author'] = input("Enter Author Name: ")
    book['status'] = "Available"

    pickle.dump(book, f)
    f.close()

    print("Book Created Successfully")


def display_books():
    try:
        f = open("book.dat", "rb")
        print("\n--- Book Records ---")
        while True:
            book = pickle.load(f)
            print(book)
    except:
        f.close()


def search_book():
    bid = int(input("Enter Book ID: "))
    found = False

    try:
        f = open("book.dat", "rb")
        while True:
            book = pickle.load(f)
            if book['id'] == bid:
                print(book)
                found = True
    except:
        f.close()

    if not found:
        print("Book Not Found")


# ---------- STUDENT FUNCTIONS ----------

def create_student():
    f = open("student.dat", "ab")
    student = {}

    student['id'] = int(input("Enter Student ID: "))
    student['name'] = input("Enter Student Name: ")
    student['book'] = None

    pickle.dump(student, f)
    f.close()

    print("Student Created Successfully")


def display_students():
    try:
        f = open("student.dat", "rb")
        print("\n--- Student Records ---")
        while True:
            student = pickle.load(f)
            print(student)
    except:
        f.close()


# ---------- ISSUE BOOK ----------

def issue_book():
    sid = int(input("Enter Student ID: "))
    bid = int(input("Enter Book ID: "))

    students = []
    books = []

    # load students
    try:
        f = open("student.dat", "rb")
        while True:
            students.append(pickle.load(f))
    except:
        pass
    try:
        f.close()
    except:
        pass

    # load books
    try:
        f = open("book.dat", "rb")
        while True:
            books.append(pickle.load(f))
    except:
        pass
    try:
        f.close()
    except:
        pass

    for s in students:
        if s['id'] == sid and s['book'] is None:
            for b in books:
                if b['id'] == bid and b['status'] == "Available":
                    s['book'] = bid
                    b['status'] = "Issued"
                    print("Book Issued Successfully")

    # save students
    f = open("student.dat", "wb")
    for s in students:
        pickle.dump(s, f)
    f.close()

    # save books
    f = open("book.dat", "wb")
    for b in books:
        pickle.dump(b, f)
    f.close()


# ---------- DEPOSIT BOOK ----------

def deposit_book():
    sid = int(input("Enter Student ID: "))

    students = []
    books = []

    try:
        f = open("student.dat", "rb")
        while True:
            students.append(pickle.load(f))
    except:
        pass
    try:
        f.close()
    except:
        pass

    try:
        f = open("book.dat", "rb")
        while True:
            books.append(pickle.load(f))
    except:
        pass
    try:
        f.close()
    except:
        pass

    for s in students:
        if s['id'] == sid and s['book'] is not None:
            for b in books:
                if b['id'] == s['book']:
                    b['status'] = "Available"
            s['book'] = None
            print("Book Deposited Successfully")

    # save again
    f = open("student.dat", "wb")
    for s in students:
        pickle.dump(s, f)
    f.close()

    f = open("book.dat", "wb")
    for b in books:
        pickle.dump(b, f)
    f.close()


# ---------- MAIN MENU ----------

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Book Issue")
    print("2. Book Deposit")
    print("3. Administration Menu")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        issue_book()

    elif choice == 2:
        deposit_book()

    elif choice == 3:
        print("\n--- ADMIN MENU ---")
        print("1. Create Student")
        print("2. Display Students")
        print("3. Create Book")
        print("4. Display Books")
        print("5. Search Book")

        admin = int(input("Enter Choice: "))

        if admin == 1:
            create_student()
        elif admin == 2:
            display_students()
        elif admin == 3:
            create_book()
        elif admin == 4:
            display_books()
        elif admin == 5:
            search_book()

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")