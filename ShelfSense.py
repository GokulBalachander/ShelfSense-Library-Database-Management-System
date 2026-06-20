from tabulate import tabulate
import mysql.connector as sql

# 1. FUNCTION TO ISSUE  A BOOK

def b_issue():
    ph = input('Enter phone number of customer: \n')
    acc = input('Enter accession number of book: \n')
    doi = input('Enter date of issuing in format YYYY/MM/DD: \n')
    try:
        q = "update customers set Issued_book = %s,Issued_date = %s where Phone_no = %s;"
        cur.execute(q, (acc, doi, ph))
        if cur.rowcount > 0:
            print('\n Issued successfully!!!')
        else:
            print('\n No results found!!!')
        mycon.commit()
    except sql.Error as e:
        print('Error :', e)


# 2. FUNCTION TO DEISSUE A BOOK

def b_deissue():
    ph = input('Enter phone number of customer: \n')
    try:
        q = "update customers set Issued_book = %s,Issued_date = %s where Phone_no = %s;"
        cur.execute(q, (None, None, ph))
        if cur.rowcount > 0:
            print('\n De - issued successfully!!')
        else:
            print('\n No results found!!')
        mycon.commit()
    except sql.Error as e:
        print('Error :', e)

    # 3. FUNCTION TO INSERT AS MANY BOOK DEATILS AS USER WANTS


def insert_books():
    n = 1
    while n:
        acc_no = input("Enter Accession Number:\n")
        book_name = input("Enter Book Name:\n")
        author = input("Enter Author:\n ")
        price = float(input("Enter Price:\n "))
        publish_date = input("Enter Publish Date (YYYY/MM/DD):\n")
        l = [acc_no, book_name, author, price, publish_date]
        for x in range(len(l)):
            if l[x] == '':
                l[x] = None
        t = tuple(l)
        try:
            query = "insert into books values(%s, %s, %s, %s, %s);"
            cur.execute(query, t)
        except sql.Error as e:
            print('Error :', e)
        else:
            print("\nBook added successfully!!!\n")
            mycon.commit()
        while True:
            cont = input("\nDo you want to add another book? (yes/no):\n").lower()
            if cont not in ('yes', 'no'):
                print('Invalid input!!!\n')
                continue
            elif cont == 'yes':
                break
            else:
                n = 0
                break


# 4. FUNCTION TO INSERT AS MANY CUSTOMERS AS USER WANTS

def insert_customers():
    n = 1
    while n:
        print()
        print("*****CUSTOMER REGISTRATION*********")
        phone_no = input("Enter Phone Number:\n ")
        name = input("Enter Name:\n ")
        gender = input("Enter Gender (M/F):\n")
        reg_date = input("Enter Registration Date (YYYY/MM/DD):\n ")
        l = [phone_no, name, gender, reg_date]
        for x in range(len(l)):
            if l[x] == '':
                l[x] = None
        t = tuple(l)
        try:
            query = "insert into customers (Phone_no, Name, Gender, Reg_date) VALUES (%s, %s, %s, %s)"
            cur.execute(query, t)
        except sql.Error as e:
            print('Error :', e)
        else:
            print("\nCustomer added successfully!!!!\n")
            mycon.commit()
        while True:
            cont = input("\nDo you want to add another customer? (yes/no):\n").lower()
            if cont not in ('yes', 'no'):
                print('\nInvalid input!!!!\n')
                continue
            elif cont == 'yes':
                break
            else:
                n = 0
                break


# 5. FUNCTION TO SEARCH A BOOK

def Search_Book():
    bname = input("Enter the book name to be searched: \n")
    bnm = '%' + bname + '%'
    try:
        query = "select * from books where Book_name like %s;"
        cur.execute(query, (bnm,))
        result = cur.fetchall()
        if result:
            headers = ["Acc no", "Book Name", "Author", "Price", "Published date"]
            print(tabulate(result, headers=headers, tablefmt="grid"))
        else:
            print('\n No results found!!!')
    except sql.Error as e:
        print('Error :', e)
    mycon.commit()


# 6. FUNCTION TO DISPLAY BORROWERS & BOOKS

def display_borrowers_and_books():
    try:
        query = "select Phone_no,Name,Gender,Reg_date,Issued_date,Issued_book,Book_name,Author,Price,Publish_date from customers c,books b where c.issued_book = b.Acc_no order by Name "
        cur.execute(query)
        results = cur.fetchall()
        if results:
            print()
            print("*********BORROWERS & BOOKS***************")
            headers = ['Phone no.', 'Name', 'Gender', 'Registered date', 'Issued date', 'Issued book', 'Book Name',
                       'Author', 'Price', 'Published date']
            print(tabulate(results, headers=headers, tablefmt="grid"))
            print('Number of borrowers is ', len(results))
        else:
            print("\nNo books have been borrowed!!!!!\n")
    except sql.Error as e:
        print('Error :', e)
    mycon.commit()


# 7. FUNCTION TO DISPLAY BOOK DETAILS

def display_books_table():
    try:
        query = "select * from books order by Book_name"
        cur.execute(query)
        result = cur.fetchall()
        if result:
            print()
            print("***********BOOK DETAILS*************\n")
            headers = ['Acc no', 'Book Name', 'Author', 'Price', 'Published date']
            print(tabulate(result, headers=headers, tablefmt="grid"))
            print('Number of books is :', len(result))
        else:
            print('\nNo results!!!!!!!!')
    except sql.Error as e:
        print('Error :', e)
    mycon.commit()


# 8. FUNCTION TO DISPLAY ALL CUSTOMER DETAILS

def Customer_details():
    try:
        query = "select * from customers order by Name;"
        cur.execute(query)
        result = cur.fetchall()
        if result:
            print()
            print('****CUSTOMER DETAILS**********\n')
            headers = ['Phone no.', 'Name', 'Gender', 'Registered date', 'Issued date', 'Issued book']
            print(tabulate(result, headers=headers, tablefmt="grid"))
            print('Total number of customers is', len(result))
        else:
            print('No results')
    except sql.Error as e:
        print('Error :', e)
    mycon.commit()


# 9. FUNCTION TO DELETE DETAILS OF A CUSTOMER

def Delete_Customer():
    ph = input("Enter phone number of customer to be deleted:\n")
    try:
        query = "delete from customers where Phone_no = %s;"
        cur.execute(query, (ph,))
        if cur.rowcount > 0:
            print("\nCustomer has been successfully deleted!!!\n")
        else:
            print("\nNo such customer was found!!!\n")
        mycon.commit()
    except sql.Error as e:
        print('Error :', e)


# 10. FUNCTION TO DELETE DETAILS OF A BOOK

def Delete_Book():
    acc = input("Enter accession number of book to be deleted:\n")
    try:
        query = "delete from books where Acc_no = %s;"
        cur.execute(query, (acc,))
        mycon.commit()
        if cur.rowcount > 0:
            print("Book has been successfully deleted!!!\n")
        else:
            print("\nNo such book was found!!!\n")
        mycon.commit()
    except sql.Error as e:
        print('Error :', e)


# 11. FUNCTION TO UPDATE CUSTOMER TABLE

def update_customer():
    try:
        ph = input('\nEnter phone number of customer to update:\n')
        q = 'select * from customers where Phone_no = %s'
        cur.execute(q, (ph,))
        result = cur.fetchall()
        if result:
            print()
            headers = ['Phone no.', 'Name', 'Gender', 'Registered date', 'Issued date', 'Issued book']
            print(tabulate(result, headers=headers, tablefmt="grid"))
            print()
            print('\nEnter updated details below. If a detail has not changed enter the previous detail :\n')
            phone_no = input("Enter Phone Number: \n")
            name = input("Enter Name: \n")
            gender = input("Enter Gender (M/F): \n")
            reg_date = input("Enter Registration Date (YYYY/MM/DD): \n")
            isd = input('Enter issued date (YYYY/MM/DD): \n')
            isb = input('Enter acc no. of issued book: \n')
            l = [phone_no, name, gender, reg_date, isd, isb, ph]
            for x in range(len(l)):
                if l[x] == '':
                    l[x] = None
            t = tuple(l)
            p = 'update customers set Phone_no = %s,Name = %s,Gender = %s,Reg_date = %s,Issued_date = %s,Issued_book = %s where Phone_no = %s'
            cur.execute(p, t)
            print('\nUpdation successful!!!!\n')
        else:
            print('\nNo such accession number exists!!!!\n')
        mycon.commit()
    except sql.Error as e:
        print('Error :', e)


# 12. FUNCTION TO UPDATE BOOK TABLE

def update_book():
    try:
        acc = input('\nEnter accession number of book to be updated:\n')
        q = 'select * from books where Acc_no = %s'
        cur.execute(q, (acc,))
        result = cur.fetchall()
        if result:
            print()
            headers = ['Acc no.', 'Book Name', 'Author', 'Price', 'Published date']
            print(tabulate(result, headers=headers, tablefmt="grid"))
            print()
            print('Enter updated details below. If a detail has not changed enter the previous detail')
            print()
            acc_no = input("Enter Accession Number: ")
            book_name = input("Enter Book Name: ")
            author = input("Enter Author: ")
            price = float(input("Enter Price: "))
            publish_date = input("Enter Publish Date (YYYY/MM/DD): ")
            l = [acc_no, book_name, author, price, publish_date, acc]
            for x in range(len(l)):
                if l[x] == '':
                    l[x] = None
            t = tuple(l)
            p = 'update books set Acc_no = %s,Book_name = %s,Author = %s,Price = %s,Publish_date = %s where Acc_no = %s'
            cur.execute(p, t)
            print('\nUpdation successful\n!!!!')
        else:
            print('\nNo such accession number exists\n')
        mycon.commit()
    except sql.Error as e:
        print('Error :', e)


# TO CONNECT TO MYSQL AND CREATE A DATABASE

while True:
    try:
        pw = input('\nEnter password: \n')
        mycon = sql.connect(host='localhost', user='root', password=pw)
    except sql.Error as e:
        print('Error :', e)
    else:
        break
cur = mycon.cursor()
if mycon.is_connected():
    print('Connected !!!\n')
else:
    print('Not connected !!!\n')
while True:
    print('Enter yes if a database is already created or no if you have to create:')
    r = input()
    if r.lower() == 'no':
        while True:
            nm = input('\nEnter name of new database: \n')
            try:
                cur.execute("create database `{}`;".format(nm))
                cur.execute("use `{}`;".format(nm))
                cur.execute(
                    "create table books(Acc_no varchar(7) primary key,Book_name varchar(40),Author varchar(30),Price float,Publish_date date);")
                cur.execute(
                    "create table customers(Phone_no char(12) primary key,Name varchar(30),Gender char(1),Reg_date date,Issued_date date,Issued_book varchar(7), foreign key(Issued_book) references books(Acc_no));")
                print('Database', nm, ' and tables have been created')
                break
            except sql.Error as e:
                print('Error :', e)
        break
    elif r.lower() == 'yes':
        while True:
            nm = input('Enter name of previously created database: \n')
            try:
                cur.execute("use `{}`".format(nm))
                break
            except sql.Error as e:
                print('Error :', e)
        print('\nDatabase', nm, 'accessed!!')
        break
    else:
        print('\nInvalid choice!!')


# FUNCTION FOR MAIN MENU

def main_menu():
    while True:
        print()
        print()
        print('1. Issuing a book: ')
        print('2. De -issuing a book: ')
        print('3. Inserting book details: ')
        print('4. Customer registeration: ')
        print('5. To search for a book: ')
        print('6. Display borrowers and borrowed books: ')
        print('7. To display all books: ')
        print('8. To display all customers: ')
        print("9. To delete a customer's detail: ")
        print("10. To delete a book's detais: ")
        print('11. Update details of a customer: ')
        print('12. Update details of a book: ')
        print('13. To exit loop:\n ')
        ch = input('Enter choice number:\n ')
        if ch == '1':
            b_issue()
        elif ch == '2':
            b_deissue()
        elif ch == '3':
            insert_books()
        elif ch == '4':
            insert_customers()
        elif ch == '5':
            Search_Book()
        elif ch == '6':
            display_borrowers_and_books()
        elif ch == '7':
            display_books_table()
        elif ch == '8':
            Customer_details()
        elif ch == '9':
            Delete_Customer()
        elif ch == '10':
            Delete_Book()
        elif ch == '11':
            update_customer()
        elif ch == '12':
            update_book()
        elif ch == '13':
            print('Exiting loop')
            break
        else:
            print('Invalid choice. Please try again')


# STARTING THE PROGRAM

main_menu()

mycon.commit()
cur.close()
mycon.close()
print('End of Program')