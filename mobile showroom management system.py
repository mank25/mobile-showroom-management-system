import mysql.connector
import uuid
con=mysql.connector.connect(host="localhost",user="root",password="kevlar0725",db="x4")
if con.is_connected():
    print("Connceted")
else:
    print("Unable to connect")
cur=con.cursor()
cur.execute("create table if not exists costumer(costumer_id varchar(70) primary key,name varchar(30),E_Mail varchar(30),mobile varchar(10),address varchar(50));")
con.commit()
def check(A,M,w):
    try:
        cur.execute("create table if not exists main(company varchar(10), model varchar(10) ,colour varchar(10), storage varchar(3), screen_size varchar(50),price varchar(50), quantity varchar(10));")
        cur.execute("select*from main where model={} and colour={} and storage={};".format(A,M,w))
        info=cur.fetchall()
        if info==[]:
            return False
        else:
            return True
    except Exception as e:
        print("Error ", e)
def check2(s):
    try:
        cur.execute("create table if not exists costumer(costumer_id varchar(70) primary key,name varchar(30),E_Mail varchar(30),mobile int(10),address varchar(50));")
        cur.execute("select*from costumer where costumer_id={} ;".format(s))
        info=cur.fetchall()
        if info==[]:#([XJHJX],[8237482])
            return False
        else:
            return True
    except Exception as e:
        print("Error ", e)

def add():
    print("|ADD PRODUCT|")
    b="'"+input("ENTER COMPANY: ")+"'"
    c="'"+input("ENTER MODEL NAME: ")+"'"
    n="'"+input("ENTER COLOUR: ")+"'"
    e="'"+(input("ENTER STORAGE(Gb): "))+"'"
    f="'"+(input("ENTER SCREEN SIZE:  "))+"'"
    g="'"+(input("ENTER PRICE: "))+"'"
    
    if check(c,n,e):
        print("YOUR PRODUCT ALREADY EXISTS PLEASE")
        cur.execute('select quantity from main where model={} and colour={} and storage={};'.format(c,n,e))
        info=cur.fetchall()
        for i in info:
            print("NUMBER OF PRODUCTS ALREADY IN STOCK ",info[0][0])
        h="'"+str(int(input('ENTER THE QUANTITY TO BE ADDED'))+int(info[0][0]))+"'"
        cur.execute('update main set quantity={} where model={} and colour={} and storage={};'.format(h,c,n,e))
        con.commit()
        print ("updated")
    else:
        h1="'"+(input("ENTER QUANTITY: "))+"'"
        cur.execute('insert into main values({},{},{},{},{},{},{});'.format(b,c,n,e,f,g,h1))
        con.commit()
        print('Record Added\n')

def remove():
    print("|REMOVE PRODUCT|")
    print(" Products Available: ")
    cur.execute('select*from main')
    info=cur.fetchall()
    print("company\t\tModel\t\t\tColour\t\tstorage\t\tscreen size\tprice\t\tquantity")
    for x in info:
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],))
    j="'"+input("Enter Model: ")+"'"
    q="'"+input("Enter colour: ")+"'"
    y="'"+input("Enter Storage")+"'"
    if check(j,q,y):
        cur.execute("select*from main where model={} and colour={} and storage={};".format(j,q,y))
        j1=cur.fetchall()
        for x in j1:
            print(x)
        cur.execute("select quantity from main where model={} and colour={} and storage={};".format(j,q,y))
        j1=cur.fetchall()
        k="'"+str((int(j1[0][0]))-int(input('ENTER QUANTITY')))+"'"
        if k=="'0'":
            cur.execute("delete from main where model={} and colour={} and storage={};".format(j,q,y))
            con.commit()
            print("updated")
        else:
            cur.execute('update main set quantity={} where model={} and colour={} and storage={};'.format(k,j,q,y))
            con.commit()
            print ("Updated\n")     
    else:
        print("Product not found")

def stock():
    print("|STOCK|")
    print("Stock available is :")
    print("company\t\tmodel\t\t\t\tColour\t\tStorage")
    cur.execute("select*from main;")
    info=cur.fetchall()
    for i in info:
        print("{}\t\t{}\t\t\t{}\t\t{}".format(i[0],i[1],i[2],i[3]))
        
        
def details():
    r="'"+input("ENTER COMPANY")+"'"
    s="'"+input("ENTER MODEL")+"'"
    a="'"+input("ENTER STORAGE")+"'"
    cur.execute("select * from main where company={} and model={} and storage={};".format(r,s,a))
    info=cur.fetchall()
    print("product details are:")
    print("company\t\tmodel\t\t\tcolour\t\tScreen Size\tPrice\t\tQuantity")
    for i in info:
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i[0],i[1],i[2],i[4],i[5],i[6],))
        

def addcostumer():
    costid="'"+str(uuid.uuid4())+"'"
    print("Costumer's unique id:",costid)
    b="'"+input("ENTER NAME: ")+"'"
    c="'"+input("E-MAIL: ")+"'"
    n="'"+input("ENTER MOBILE NUMBER: ")+"'"
    e="'"+(input("ENTER ADDRESS: "))+"'"
    cur.execute('insert into costumer values({},{},{},{},{});'.format(costid,b,c,n,e))
    con.commit()
    print('Record Added\n')
    
def removecostumer():
    cur.execute('select*from costumer')
    info=cur.fetchall()
    print("Id,Name,E-Mail,Mobile Number,Address")
    for x in info:
        print(x)
    j="'"+input("Enter Id: ")+"'"
    if check2(j):
        cur.execute("delete from costumer where costumer_id={};".format(j))
        print("Deleted")     
    else:
        print("Costumer not found")

def updatecostumer():
    cur.execute('select*from costumer')
    info=cur.fetchall()
    for x in info:
        print(x)
    p="'"+input("Enter costumer's id:")+"'"
    print("select the information you want to upadate:")
    option=int(input("\n1.NAME: \n2.E-MAIL: \n3.MOBILE NUMBER: \n4.ADDRESS: \n"))
    while option!=0:
        if option==1:
            cur.execute("select name from costumer where costumer_id={};".format(p))
            info=cur.fetchall()
            for i in info:
                print("old name =")
                print(i[0])
            x="'"+input('Enter new name')+"'"
            cur.execute("update costumer set name={} where costumer_id={};".format(x,p))
            con.commit()
            print("updated")
        elif option==2:
            cur.execute("select E_Mail from costumer where costumer_id={};".format(p))
            info=cur.fetchall()
            for i in info:
                print("old e-mail id")
                print(i[0])
            y="'"+input("enter new e-mail id: ")+"'"
            cur.execute("update costumer set E_Mail={} where costumer_id={};".format(y,p))
            con.commit()
            print("updated")
        elif option==3:
            cur.execute("select mobile from costumer where costumer_id={};".format(p))
            info=cur.fetchall()
            for i in info:
                print("old mobile Number: ")
                print(i[0])
            y="'"+input("enter new mobile number: ")+"'"
            cur.execute("update costumer set mobile={} where costumer_id={};".format(y,p))
            con.commit()
            print("updated")
        elif option==4:
            cur.execute("select address from costumer where costumer_id={};".format(p))
            info=cur.fetchall()
            for i in info:
                print("old Address: ")
                print(i[0])
            y="'"+input("enter new address: ")+"'"
            cur.execute("update costumer set address={} where costumer_id={};".format(y,p))
            con.commit()
            print("updated")
        elif option==5:
            break
        else:
            print("something went wrong")
            break
        option=int(input("\n1.NAME: \n2.E-MAIL: \n3.MOBILE NUMBER: \n4.ADDRESS: \n5.exit\n"))
def costumerdatabase():
    cur.execute("select * from costumer")
    info=cur.fetchall()
    for i in info:
        print(i)
        
def costumerdetails():
    x="'"+input("Enter id")+"'"
    cur.execute("select * from costumer where costumer_id={};".format(x))
    info=cur.fetchall()
    for i in info:
        print(i)

def costumer():
    print("COSTUMER CORNER:")
    a=int(input("what do you want to do:\n1. Add costumer \n2. Remove costumer \n3 Update Costumer \n4. costumer database \n5. costumer Details \n6.exit\n"))
    while a!=0:
        if a==1:
            addcostumer()
        elif a==2:
            removecostumer()
        elif a==3:
            updatecostumer()
        elif a==4:
            costumerdatabase()
        elif a==5:
            costumerdetails()
        elif a==6:
            break
        else:
            print("something went wrong")        
        a=int(input("what do you want to do:\n1. Add costumer \n2. Remove costumer \n3 Update Costumer \n4. costumer database \n5. costumer Details \n6.exit\n"))
        
a=int(input("what do you want to do:\n1. Add product \n2. Remove Product \n3. Mobile Stock \n4. Product Details \n5.Costumer Section\n6. Exit \n"))
while a!=0:
    if a==1:
        add()
    elif a==2:
        remove()
    elif a==3:
        stock()
    elif a==4:
        details()
    elif a==5:
        costumer()
    elif a==6:
        break
    else:
        print("something went wrong")
        break
    a=int(input("what do you want to do:\n1. Add product \n2. Remove Product \n3. Mobile Stock \n4. Product Details \n5.Costumer Section\n6. Exit \n"))
