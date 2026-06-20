from db import conn,cursor

def create_account():
    acc_no=input("Enter Account Number : ")
    name=input("Enter Name : ")
    pin=input("Enter PIN : ")
    balance=float(input("Enter Initial Balance : "))
    if len(acc_no)!=12 or not acc_no.isdigit():
        print("Account Number must contain exactly 12 digits")
        return
    if len(pin) != 6 or not pin.isdigit():
        print("PIN must contain exactly 6 digits")
        return

    sql="insert into customers values(%s,%s,%s,%s)"
    values=(acc_no,name,pin,balance)

    cursor.execute(sql,values)

    conn.commit()

    print("Account Created Sucessfully")


def deposit():
    acc_no=int(input("Enter Account Number : "))
    amount=float(input("Enter Deposit Amount : "))

    sql="update customers set balance =balance+ %s where acc_num=%s"
    values=(amount,acc_no)

    cursor.execute(sql,values)

    conn.commit()

    print("Amount Deposited Successfully")

def withdraw():
    acc_no = int(input("Enter Account Number : "))
    pin = int(input("Enter PIN : "))
    amount = float(input("Enter Withdraw Amount :"))

    sql="select balance from customers where acc_num=%s and pin=%s"
    values=(acc_no,pin)

    cursor.execute(sql,values)

    data=cursor.fetchone()

    if data:
        balance=data[0]
        if balance>=amount:
            sql="update customers set balance=balance-%s where acc_num =%s"
            values=(amount,acc_no)

            cursor.execute(sql,values)

            conn.commit()

            print("Withdrawal Successful")

        else :
            print("Insufficient Balance ")
    else:
        print("Invalid Account Number or PIN")



def check_balance():
    acc_no = int(input("Enter Account Number : "))
    pin = int(input("Enter PIN : "))

    sql="select balance from customers where acc_num =%s and pin=%s"
    values=(acc_no,pin)

    cursor.execute(sql,values)

    data=cursor.fetchone()

    if data:
        print("Current Balance = ",data[0])
    else:
        print("Invalid Account Number or PIN")


def view_accounts():
    sql="select * from customers"
    cursor.execute(sql)

    data=cursor.fetchall()

    for row in data:
        print("Account Number :", row[0])
        print("Name           :", row[1])
        print("PIN            :", row[2])
        print("Balance        :", row[3])
        print("-" * 30)


def delete_account():
    acc_no=int(input("Enter Account Number : "))

    sql="delete from customers where acc_num=%s"
    values=(acc_no,)

    cursor.execute(sql,values)

    conn.commit()
    print("Account Deleted Successfully ")


def exit_program():
    print("Thank You for Using Bank Management System")
