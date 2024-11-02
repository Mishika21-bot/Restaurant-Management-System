import mysql.connector

try:
    x = mysql.connector.connect(
        host="localhost",
        user="roof",
        password="admin123",
        database="mydata"
    )
    cbj = x.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

def vmen():
    try:
        print("\n\n\n-------Available Dishes-------\n\n\n")
        q = "SELECT * FROM menu"
        cbj.execute(q)
        menu = cbj.fetchall()
        if menu:
            for i in menu:
                print("DISH NUMBER:", i[0], "\n", "---->", i[1], " (TYPE:", i[3], ")", "\n", "PRICE:", i[2])
                print("\n\n")
        else:
            print("No items available in the menu.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    yn = input("DO YOU WANT TO ORDER AN ITEM? Type (1 for yes / 2 for going back to main page): ")
    if yn == "1":
        byo()
    else:
        print("THANK YOU")
        print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")

def byo():
    try:
        ID = int(input("ENTER DISH NO. OF THE ITEM YOU WANT TO ORDER: "))
        QUANTITY = int(input("ENTER QUANTITY: "))
        NAME = input("ENTER YOUR NAME: ")
        MOBNO = int(input("ENTER YOUR MOBILE NUMBER: "))
        ADDRESS = input("ENTER YOUR ADDRESS: ")

        a = "SELECT * FROM menu WHERE ID = %s"
        cbj.execute(a, (ID,))
        a = cbj.fetchone()
        if a:
            b = a[2]
            c = QUANTITY * b
            ins = "INSERT INTO cusdet (ID, QUANTITY, NAME, MOBNO, ADDRESS, TOTALPRICE) VALUES (%s, %s, %s, %s, %s, %s)"
            cbj.execute(ins, (ID, QUANTITY, NAME, MOBNO, ADDRESS, c))
            x.commit()
            print("\nTHANKS FOR YOUR ORDER\n")
            print("YOUR ORDER HAS BEEN PLACED SUCCESSFULLY\n")
            print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE")
        else:
            print("Invalid dish ID. Please try again.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")

def vyo():
    try:
        c = int(input("Enter your mobile number: "))
        d = "SELECT * FROM cusdet WHERE MOBNO = %s"
        cbj.execute(d, (c,))
        p = cbj.fetchall()
        if p:
            print("\nYOUR RECENT ORDERS\n")
            r = "SELECT menu.ID, menu.DISH_NAME, menu.TYPE, cusdet.TOTALPRICE, cusdet.MOBNO, cusdet.ADDRESS FROM menu, cusdet WHERE cusdet.MOBNO = %s AND menu.ID = cusdet.ID"
            cbj.execute(r, (c,))
            e = cbj.fetchall()
            for j in e:
                print("ID:", j[0], "\n", "ITEM NAME:", j[1], "\n", "ITEM TYPE:", j[2], "\n", "TOTAL PRICE:", j[3], "\n", "MOBILE NUMBER:", j[4], "\n", "ADDRESS:", j[5], "\n")
        else:
            print("No recent orders found for this number.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except ValueError:
        print("Invalid input. Please enter a valid mobile number.")

def cyo():
    try:
        c = int(input("Enter your mobile number: "))
        e = "DELETE FROM cusdet WHERE MOBNO = %s"
        cbj.execute(e, (c,))
        x.commit()
        print("\n\nYOUR ORDER HAS BEEN CANCELLED")
        print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE\n\n")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except ValueError:
        print("Invalid input. Please enter a valid mobile number.")

def fdbck():
    fd = input("Enter your name: ")
    print("Write something about us --")
    fdi = input()
    try:
        q = "INSERT INTO feedback (name, feedback) VALUES (%s, %s)"
        cbj.execute(q, (fd, fdi))
        x.commit()
        print("\nThanks for your feedback :)\n")
        print("YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE\n\n")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def start():
    print("\n\n\n")
    print("            ....................................................WELCOME TO....................................................")
    print("                                                 [:::::::> GROVE STREET RESTAURANT <:::::::]")
    print("            ...............................................................................................................")
    print("\nPress assigned keys to go forward:")
    print("1. CUSTOMER ")
    print("2. EXIT ")

def start1():
    while True:
        print("\n1. VIEW MENU")
        print("2. VIEW YOUR ORDERS")
        print("3. CANCEL ORDER")
        print("4. FEEDBACK")
        print("5. EXIT")
        
        try:
            ch1 = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if ch1 == 1:
            vmen()
        elif ch1 == 2:
            vyo()
        elif ch1 == 3:
            cyo()
        elif ch1 == 4:
            fdbck()
        elif ch1 == 5:
            print("Exiting to main menu.")
            break
        else:
            print("\nINVALID CHOICE\nTRY AGAIN\n")

while True:
    start()
    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if ch == 1:
        start1()
    elif ch == 2:
        print("Thank you")
        break
    else:
        print("INVALID CHOICE\nTRY AGAIN")
