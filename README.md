# Bank Management System Using Python and MySQL

## Project Description

This is a simple Bank Management System developed using Python and MySQL Connector. The project allows users to create accounts, deposit money, withdraw money, check balance, view all accounts, and delete accounts.

## Technologies Used

* Python
* MySQL
* mysql-connector-python

## Project Structure

```
BANK_PROJECT_PYTHON/
│
├── db.py
├── operations.py
├── main.py
└── README.md
```

## Database Table

```sql
CREATE TABLE customers(
    acc_num BIGINT PRIMARY KEY,
    name VARCHAR(50),
    pin INT,
    balance FLOAT
);
```

## Features

### 1. Create Account

* Creates a new bank account.
* Stores account number, name, PIN, and initial balance.

### 2. Deposit Money

* Adds money to an existing account.

### 3. Withdraw Money

* Verifies account number and PIN.
* Checks available balance before withdrawal.

### 4. Check Balance

* Displays current account balance.

### 5. View Accounts

* Displays all customer records.

### 6. Delete Account

* Removes an account permanently from the database.

### 7. Exit Program

* Closes the application.

## Installation

### Install MySQL Connector

```bash
pip install mysql-connector-python
```

### Configure Database Connection

In `db.py`:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bank_db"
)

cursor = conn.cursor()
```

## How to Run

```bash
python main.py
```

## Sample Menu

```
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. View Accounts
6. Delete Account
7. Exit
```

## Author

Mahesh

## Future Improvements

* Change PIN
* Transfer Money
* Transaction History
* Exception Handling
* Login System
* Admin Panel
