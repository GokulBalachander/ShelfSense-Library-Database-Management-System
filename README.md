# Library Database Management System (LDMS)

A command-line Library Database Management System built with **Python** and **MySQL**. It allows librarians to manage book inventory and customer records, track book issuing/de-issuing, and search across the catalog — all backed by a relational database with referential integrity.

## Features

- **Book Management** — add, update, delete, and search books by name
- **Customer Management** — register, update, delete, and view customer details
- **Issuing System** — issue and de-issue books to/from customers, with automatic tracking of issue dates
- **Borrower Reports** — view all current borrowers along with the books they've issued
- **Formatted Output** — all query results displayed as clean, readable tables using `tabulate`

## Tech Stack

- **Language:** Python 3.6+
- **Database:** MySQL
- **Libraries:** `mysql-connector-python`, `tabulate`
- **Tools:** MySQL Workbench, Visual Studio Code

## Database Schema

**Books**

| Field | Type | Key |
|---|---|---|
| Acc_no | VARCHAR(7) | PRIMARY KEY |
| Book_name | VARCHAR(40) | |
| Author | VARCHAR(30) | |
| Price | FLOAT | |
| Publish_date | DATE | |

**Customers**

| Field | Type | Key |
|---|---|---|
| Phone_no | CHAR(12) | PRIMARY KEY |
| Name | VARCHAR(30) | |
| Gender | CHAR(1) | |
| Reg_date | DATE | |
| Issued_date | DATE | |
| Issued_book | VARCHAR(7) | FOREIGN KEY → Books(Acc_no) |

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd library-database-management-system
   ```

2. **Install dependencies**
   ```bash
   pip install mysql-connector-python tabulate
   ```

3. **Set up MySQL**
   Make sure MySQL is installed and running locally. The program will prompt you to either create a new database or connect to an existing one on first run.

4. **Run the program**
   ```bash
   python library_management.py
   ```

## Usage

On launch, the program asks for your MySQL password and whether to create a new database or use an existing one. Once connected, you'll see a menu:

```
1.  Issuing a book
2.  De-issuing a book
3.  Inserting book details
4.  Customer registration
5.  Search for a book
6.  Display borrowers and borrowed books
7.  Display all books
8.  Display all customers
9.  Delete a customer's details
10. Delete a book's details
11. Update details of a customer
12. Update details of a book
13. Exit
```

Enter the corresponding number to perform an action.

## Limitations

- Command-line only — no graphical user interface
- No backup or recovery mechanism for data loss
- No encryption or access control on sensitive data
- Designed for single-user, local use rather than concurrent multi-user access

## Authors

- Gokul Balachander
- Sreegovind Erambathu
- Nandagopal R Nair
