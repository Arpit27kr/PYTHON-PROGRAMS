import mysql.connector as a
con = a.connect(host = "localhost", user = "root", passwd = "computerforfun", database = "banking")


def openAcc():
    n = input("enter name:")
    ac = input("enter account no. :")
    db = input("enter the D.O.B:")
    p = input("enter the phne  no. :")
    ad = input("enter the address:")
    ob = int (input("enter the openeing account :"))
    data1 = (n,ac,db, p, ad, ob)
    data2 = (n,ac,ob)
    sql3 = "insert into account values(%s, %s, %s, %s, %s, %s )"
    sql4 = "insert into amount  values(%s, %s, %s)"
    c = con.cursor()
    c.execute(sql3, data1)
    c.execute(sql4, data2)
    con.commit()
    print("entered data successfully")
    main()



def depoAmo():
    am = int(input("enter the amount:"))
    ac = input("enter the account no.")
    aj = "select balance form amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    tam = myresult[0] + am
    sql = "update amount set balance = %s where acno = %s"
    d = (tam, ac)
    c.execute(sql,d)
    con.commit()
    main()


def witham():
    am = int(input("enter the amount :"))
    ac = input("enter the account no.:")
    a = "select balance from the amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    tam = myresult[0] - am
    sql = "update amount set balance = %s where acno = %s"
    d = (tam, ac)
    c.execute(sql, d)
    con.commit()
    main()



def balance():
    ac = input("enter Account no.")
    a = "select balance form amount where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    print("Balance for account : ",ac," is ",myresult[0])
    main()



def dispacc():
    ac = input("enter Account no.")
    a = "select from account where acno. = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    for i in myresult:
        print(i,end = " ")
    main()


def closeac():
    ac = input("enter account no. :")
    sql3 = "delete from account where acno = %s"
    sql4 = "delete from account where acno = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(sql3, data)
    c.execute(sql4, data)
    con.commit()
    main()

def main():
    print("""
    1. OPEN NEW ACCOUONT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY 
    5. DISPLAY CUSTOMER DETAILS 
    6. CLOSE AN ACCOUNT""")
    choice = input("enter task no.")
    if (choice == "1"):
        openAcc()
    elif (choice == "2"):
        depoAmo()
    elif (choice == "3"):
        witham()
    elif (choice =="4"):
        balance()
    elif (choice =="5"):
        dispacc()
    elif (choice =="6"):
        closeac()
    else:
        print("wrong choice!")
main()
