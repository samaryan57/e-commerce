from getpass import getpass
from datetime import datetime

#for animation:

import time

#getpass makes the password invisible in the console

#mysql connection:

import mysql.connector as sql
print('\033[H\033[J')
pwd = getpass("\n\nPlease enter the password for this system's MySQL Server: ")
conn = sql.connect(host = "localhost", user = "root", password = pwd)
if conn.is_connected:
    print("\n\nConnection to database is succesful.\n\n")
cur = conn.cursor()

#intro animation:

def intro():
    for i in range(1):
            
        time.sleep(0.7)
        print('\033[H\033[J')
            
        print("\t\t**       ***      ******     ********    **********")
        print("\t\t*                               *                 *")
        print("\t\t*                              * *                *")
        print("\t\t*                             *   *               *")
        print("\t\t*                            *     *              *")
        print("\t\t*                             *   *               *")
        print("\t\t*                  *****     ********    ****     *")
        print("\t\t*                  *                        *     *")
        print("\t\t*                   *                      *      *")
        print("\t\t*                     *                  *        *")
        print("\t\t*                            * * * *              *")
        print("\t\t*                                                 *")
        print("\t\t *                   * *        *   *     *      *")            
        print("\t\t         *           *         * *  *      *    *")          
        print("\t\t          *          * *       ***  *     *    *")            
        print("\t\t           *         *         * *  *      *  *")            
        print("\t\t                   * *         * *  *     *  *")                
        print("\t\t                     *                     *")                    
        print("\t\t                       *                 *")                            
        print("\t\t                              *   *")
        print("\t\t                                *                     ")

        time.sleep(0.5)                                                                   
        print('\033[H\033[J')

        print("\t\t**       ***      ******         ******************")
        print("\t\t*                                   *             *")
        print("\t\t*                                  * *            *")
        print("\t\t*                                 *   *           *")
        print("\t\t*                                *     *          *")
        print("\t\t*                                 *   *           *")
        print("\t\t*                  *****         ************     *")
        print("\t\t*                  *                        *     *")
        print("\t\t*                   *                      *      *")
        print("\t\t*                     *                  *        *")
        print("\t\t*                                * * * *          *")
        print("\t\t*                                                 *")
        print("\t\t *                   * *            *   * *      *")
        print("\t\t         *           *             * *  *  *    *")
        print("\t\t          *          * *           ***  * *    *")
        print("\t\t           *         *             * *  *  *  *")
        print("\t\t                   * *             * *  * *  *")
        print("\t\t                     *                     *")
        print("\t\t                       *                 *")
        print("\t\t                                  *   *")
        print("\t\t                                    *                 ")

        time.sleep(0.4)                                                                   
        print('\033[H\033[J')

        print("\t\t**       ***               ************************")
        print("\t\t*                                   *             *")
        print("\t\t*                                  * *            *")
        print("\t\t*                                 *   *           *")
        print("\t\t*                                *     *          *")
        print("\t\t*                                 *   *           *")
        print("\t\t*                           *****************     *")
        print("\t\t*                           *               *     *")
        print("\t\t*                            *             *      *")
        print("\t\t*                              *         *        *")
        print("\t\t*                                * * * *          *")
        print("\t\t*                                                 *")
        print("\t\t *                            * *   *   * *      *")
        print("\t\t         *                    *    * *  *  *    *")
        print("\t\t          *                   * *  ***  * *    *")
        print("\t\t           *                  *    * *  *  *  *")
        print("\t\t                            * *    * *  * *  *")
        print("\t\t                              *            *")
        print("\t\t                                *        *")
        print("\t\t                                  *   *")
        print("\t\t                                    *                 ")

        time.sleep(0.3)                                                                   
        print('\033[H\033[J')

        print("\t\t**                      ***************************")
        print("\t\t*                                   *             *")
        print("\t\t*                                  * *            *")
        print("\t\t*                                 *   *           *")
        print("\t\t*                                *     *          *")
        print("\t\t*                                 *   *           *")
        print("\t\t*                           *****************     *")
        print("\t\t*                           *               *     *")
        print("\t\t*                            *             *      *")
        print("\t\t*                              *         *        *")
        print("\t\t*                                * * * *          *")
        print("\t\t*                                                 *")
        print("\t\t *                            * *   *   * *      *")
        print("\t\t                        *     *    * *  *  *    *")
        print("\t\t                         *    * *  ***  * *    *")
        print("\t\t                          *   *    * *  *  *  *")
        print("\t\t                            * *    * *  * *  *")
        print("\t\t                              *            *")
        print("\t\t                                *        *")
        print("\t\t                                  *   *")
        print("\t\t                                    *                 ")

        time.sleep(0.2)                                                                   
        print('\033[H\033[J')                                                      
        
        print("\t\t                      *****************************")                                                            
        print("\t\t                      *             *             *")                                
        print("\t\t                      *            * *            *")
        print("\t\t                      *           *   *           *")
        print("\t\t                      *          *     *          *")
        print("\t\t                      *           *   *           *")
        print("\t\t                      *     *****************     *")
        print("\t\t                      *     *               *     *")
        print("\t\t                      *      *             *      *")
        print("\t\t                      *        *         *        *")
        print("\t\t                      *          * * * *          *")
        print("\t\t                      *                           *")
        print("\t\t                       *      * *   *   * *      *")
        print("\t\t                        *     *    * *  *  *    *")
        print("\t\t                         *    * *  ***  * *    *")
        print("\t\t                          *   *    * *  *  *  *")
        print("\t\t                            * *    * *  * *  *")
        print("\t\t                              *            *")
        print("\t\t                                *        *")
        print("\t\t                                  *   *")
        print("\t\t                                    *                 ")

        time.sleep(0.7)
            

#admin

def admin():
    cur.execute("show databases;")
    db = cur.fetchall()
    c = 0
    for t in db:
        if t[0] == "fab":
            c+=1
    if c == 0:
        print("\n\nThis system is running the program for the first time, so the software will create the database with all the records in it.\n\n(Delete the database anytime by running 'drop database fab;' query in MySQL.)\n\n")
        cur.execute("create database fab;")
        cur.execute("use fab;")
        cur.execute("create table produce(icode int primary key, s_name varchar(30) not null, iname varchar(30) not null, qty_in_tonne int not null, discount_inpercent int(2) default 0, price_perkg int not null, phone_no bigint);")
        cur.execute("create table p_order(orderno int primary key, s_name varchar(30) not null, iname varchar(30), qty_bought_in_tonnes int not null, total_price int not null, c_name varchar(30) not null, status varchar(30) default 'Approval awaited' );")
        cur.execute("create table s_credentials(s_name varchar(30) primary key, s_pwd int not null);")
        cur.execute("create table c_credentials(c_name varchar(30) primary key, c_pwd int not null);")
        cur.execute("create table admins(a_name varchar(30) primary key, a_pwd int not null);")
        cur.execute("insert into admins values('Riley',12345);")
        cur.execute("insert into s_credentials values('vedant',12345);")
        conn.commit()
        cur.execute("insert into s_credentials values('ayush',23456);")
        conn.commit()
        cur.execute("insert into s_credentials values('mridul',34567);")
        conn.commit()
        cur.execute("insert into c_credentials values('aryan',12345);")
        conn.commit()
        cur.execute("insert into c_credentials values('srinivas',23456);")
        conn.commit()
        cur.execute("insert into c_credentials values('yazna',34567);")
        conn.commit()
        cur.execute("insert into produce values(1001,'vedant','tomatoes',5,0,30,1234567890);")
        conn.commit()
        cur.execute("insert into produce values(1002,'mridul','potatoes',6,0,40,2345678901);")
        conn.commit()
        cur.execute("insert into produce values(1003,'ayush','french beans',4,0,50,3456789012);")
        conn.commit()
        cur.execute("insert into produce values(1004,'mridul','pumpkins',3,0,30,2345678901);")
        conn.commit()
        cur.execute("insert into produce values(1005,'ayush','potatoes',5,0,30,3456789012);")
        conn.commit()
        cur.execute("insert into p_order values(1001,'vedant','tomatoes',2,60000,'aryan','Approval awaited');")
        conn.commit()
        cur.execute("insert into p_order values(1002,'ayush','french beans',3,150000,'yazna','Approved');")
        conn.commit()
        cur.execute("insert into p_order values(1003,'mridul','pumpkins',2,60000,'aryan','Approved');")
        conn.commit()
        cur.execute("insert into p_order values(1004,'vedant','tomatoes',1,30000,'srinivas','Approval awaited');")
        conn.commit()
        print("\n\n\t\t\tDatabase Successfully Created.")
    
    elif c == 1:
        cur.execute("use fab;")  
        while True:
            print("\n\n *** Welcome "+a_name+" ! ***")
            ah1 = int(input("\n\nWhat would you like to do?\n\n1.View tables in database\n\n2.Add/remove discounts\n\n3.Remove stockout records\n\n4.Exit\n\nEnter choice no.: "))
            if ah1 == 1:
                while True:   
                    print("\n\nThese are the tables in the database: ")
                    print()
                    cur.execute("show tables;")
                    alst1 = cur.fetchall()
                    get_records(alst1)
                    ah2 = input("\n\nSelect the table you would like to view\n\n(please type the characters in the exact same manner): ")
                    cur.execute("select * from %s;"%(ah2))
                    alst2 = cur.fetchall()
                    cur.execute("desc %s;"%(ah2))
                    alst3 = cur.fetchall()
                    print("\n\nHere is the "+ah2+" table: ")
                    get_header_rows(alst3)
                    print()
                    get_records(alst2)
                    ah3 = input("\n\nWould you like to view more tables?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
                    if ah3 == "y":
                        continue
                    else:
                        print("\n\nAlright, redirecting to the prompt page...")
                        break
            elif ah1 == 2:
                print()
                cur.execute("select distinct iname from produce;")
                alst4 = cur.fetchall()
                get_records(alst4)
                ah4 = input("\n\nEnter the item for which you would like to provide a discount\n\n(please type the characters in the exact same manner): ")
                ah5 = int(input("\n\nWhat percentage of total would you like to discount?\n\n(please enter only a 1 or 2 digit positive number. *if you would like to remove a discount from the selected item, enter 0): "))
                cur.execute("update produce set discount_inpercent = %s where iname = '%s';"%(ah5,ah4))
                conn.commit()
                if ah5 > 0:
                    print("\n\nThank you for providing the customers with such a generous discount!")
                print("\n\nYour intended discount was sucessfully applied:\n\n")
                cur.execute("select * from produce where iname = '%s';"%(ah4))
                alst5 = cur.fetchall()
                cur.execute("desc produce;")
                alst8 = cur.fetchall()
                get_header_rows(alst8)
                print()
                get_records(alst5)
                print("\n\nredirecting to the prompt page...")
            elif ah1 == 3:
                cur.execute("select * from produce where qty_in_tonne = 0;")
                alst6 = cur.fetchall()
                cur.execute("desc produce;")
                alst7 = cur.fetchall()
                get_header_rows(alst7)
                print()
                get_records(alst6)
                ah6 = input("\n\nProceeding to delete the above records\n\nPress y to continue, anything else to abort(Note: Deleted records can't be produced back): ")
                if ah6 == "y":
                    cur.execute("delete from produce where qty_in_tonne = 0;")
                    conn.commit()
                    print("\n\nRecords sucessfully deleted, this action can't be undone.")
                    print("\n\nredirecting to the prompt page...")
                else:
                    print("\n\nAlright, redirecting to the prompt page...")
            else:
                print("\n\nExiting the admin menu...")
                break

            p = input("\n\nContinue to the main menu of admin or Exit the admin menu?\n\n[enter y to continue, any other character to exit]: ")
            if p == "y":
                continue
            else:
                print("\n\nThank you!")
                break
                       
#function to get the header row of the table:

def get_header_rows(l):
    b = []
    for i in range(len(l)):
        t = l[i]
        v = t[0]
        b.append(v)
    print(b)

#use this function to extract value from a single sql record output:

def get_value(list1):
    t1 = list1[0]
    v1 = t1[0]
    return v1

#use this function to print multiple records from sql:

def get_records(list2):
    for i in list2:
        print(i)

#The 'search by category' function:

def search():
    print()
    cur.execute("select distinct iname from produce;")
    l1 = cur.fetchall()
    get_records(l1)
    ch3 = input("\n\nSelect item whose details you would like to view\n\n(please type the characters in the exact same manner): ")
    print()
    cur.execute("select * from produce where iname = '%s'"%(ch3))
    l2 = cur.fetchall()
    cur.execute("desc produce;")
    slst1 = cur.fetchall()
    get_header_rows(slst1)
    print()
    get_records(l2)
    ch4 = input("\n\nWould you like to buy your selected item?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
    if ch4 == "y":
        ch5 = int(input("\n\nPlease enter the item code of the item you want to chose: "))
        print()
        cur.execute("select * from produce where icode = %s"%(ch5))
        print(cur.fetchall())
        cur.execute("select discount_inpercent from produce where icode = '%s'"%(ch5))
        l6 = cur.fetchall()
        ch8 = get_value(l6)
        if ch8 > 0:
            print("\n\nThere is currently a kind discount of "+str(ch8)+" percent for your selected produce. Do order now to not miss this offer! ")
        ch6 = input("\n\nProceed to placing an order for the above selected item?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
        if ch6 == "y":
            #getting date n time:
            now = datetime.now()
                                    
            #calculating total price:
            while True:
                amt = int(input("\n\nPlease enter the quantity of "+ch3+" you would like to order(in tonnes): "))
                cur.execute("select qty_in_tonne from produce where icode = %s"%(ch5))
                l7 = cur.fetchall()
                ch9 = get_value(l7)
                if amt > ch9:
                    print("\n\n******* Your requested amount is more than what is available with the seller. Please re enter the quantity within the range of available quantity. *******")
                    print("\n\nAvailable qty: "+str(ch9)+" tonnes")
                    continue
                break
            cur.execute("select price_perkg from produce where icode = %s"%(ch5))
            lst = cur.fetchall()
            price = get_value(lst)
            tot_price = (1-(ch8/100))*amt*price*1000 
                                    
            #producing primary key for the new order:
            cur.execute("select max(orderno) from p_order;")
            lst2 = cur.fetchall()
            new_ordno = get_value(lst2) + 1
                                    
            #producing the seller's name:
            query3 = "select s_name from produce where icode = %s"%(ch5)
            cur.execute(query3)
            lst3 = cur.fetchall()
            seller = get_value(lst3)
                                    
            #inserting new record into order table:
            query4 = "insert into p_order values(%s,'%s','%s',%s,%s,'%s','%s')"%(new_ordno,seller,ch3,amt,tot_price,c_name,'Approval awaited')
            cur.execute(query4)
            conn.commit()
                                    
            print("\n\nYour order has been sucessfully placed.\nYou will get an email for the payment link once the seller approves the order.")
            print("\n\nHere is the invoice of your order: \n\n")
            
            #invoice function called
            invoice(c_name,now,ch3,ch5,amt,price,tot_price)
        else:
            print("\n\nYou have aborted your order. Kindly continue to the FAB page to place a new order. Thank you!")
    else:
        print("\n\nYou have chosen to cancel your purchase.\n\nFAB was glad to have you! Keep shopping at FAB!")

#Use this function to create invoices:

def invoice(v1,v2,v3,v4,v5,v6,v7):
    obj = open("/Users/aryan/Desktop/Python/senior year final cs project/Bill template.txt","w+")
    #**in case of Windows OS, change the format of the file address accordingly
    str0 = "**********************************************"
    str1 = "\n\n\n\t\tFARMERS ASSOCIATION OF BIA\t\t\t\t\n\n"
    str2 = "Name of the Customer: "+v1+"\n"
    str3 = "Date and Time of placing order: "+str(v2)+"\n"
    str4 = "Produce ordered: "+v3+"\n"
    str5 = "icode of the produce: "+str(v4)+"\n"
    str6 = "Amount(in tonnes) purchased: "+str(v5)+"\n"
    str7 = "Price per kg of the produce ordered: "+str(v6)+"\n"
    str8 = "Total due: "+ str(v7)+"\n"
    str9 = "Thank you for placing the order, we look forward to see u again!\n\n\n"
    str10 = "*********************************************"
    lst = [str1,str2,str3,str4,str5,str6,str7,str8,str9,str10]
    obj.write(str0)
    obj.writelines(lst)
    obj.close()
    obj = open("/Users/aryan/Desktop/Python/senior year final cs project/Bill template.txt","r")
    stu = obj.read()
    print()
    print(stu)
    obj.close()

#Function to add produce by seller:

def add_produce():
    while True:
        cur.execute("select max(icode) from produce;")
        lst4 = cur.fetchall()
        fh2 = get_value(lst4) + 1
        fh3 = input("\n\nEnter the name of the produce you want to add: ")
        cur.execute("select iname from produce where s_name = '%s'"%(s_name))
        plst1 = cur.fetchall()
        q = []
        for i in range(len(plst1)):
            t6 = plst1[i]
            v6 = t6[0]
            q.append(v6)
        fh7 = int(input("\n\nEnter quantity in tonnes to be put up for sale: "))
        if fh3 in q:
            cur.execute("select qty_in_tonne from produce where s_name = '%s' and iname = '%s'"%(s_name,fh3))
            plst2 = cur.fetchall()
            fh8 = get_value(plst2)
            cur.execute("update produce set qty_in_tonne = %s where s_name = '%s' and iname = '%s'"%(fh7+fh8,s_name,fh3))
            conn.commit()
            print("\n\nYay! Your produce's record was successfully added to the database!")
            print()
            cur.execute("select * from produce where s_name = '%s' and iname = '%s'"%(s_name,fh3))
            print(cur.fetchall())
        else:
            fh5 = int(input("\n\nEnter price per kg of produce: "))
            fh6 = int(input("\n\nEnter your phone number: "))
            query1 = "insert into produce values(%s,'%s','%s',%s,%s,%s,%s)"%(fh2,s_name,fh3,fh7,0,fh5,fh6)
            cur.execute(query1)
            conn.commit()
            print("\n\nYay! Your produce's record was successfully added to the database!")
            print()
            cur.execute("select * from produce where icode = %s"%(fh2))
            print(cur.fetchall())
        c = input("\n\nWould you like to add more records?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
        if c == "y":
            continue
        else:
            break
    print("\n\nThank you for using FAB portal!")


#main menu:

while True:
   try:
    intro()
    print("\n\n\nContinue as\n\n1.a Customer(or)\n\n2.a Seller(or)\n\n3.an Admin?\n\n*If the system is running the software for the first time, login as an admin to create the databases.")
    ch1 = int(input("\n\nEnter choice no.: "))
    if ch1 == 1:
        #login
        c_name = input("\n\nEnter Username: ")
        c_pwd = int(getpass("\n\nEnter Password: "))
        while True:
            cur.execute("use fab;")
            cur.execute("select c_name from c_credentials;")
            p1 = cur.fetchall()
            x = []
            for i in range(len(p1)):
                t1 = p1[i]
                v1 = t1[0]
                x.append(v1)
            if c_name in x:
                cur.execute("select c_pwd from c_credentials;")
                p2 = cur.fetchall()
                y = []
                for i in range(len(p2)):
                    t2 = p2[i]
                    v2 = t2[0]
                    y.append(v2)
                if c_pwd in y:
                    print("\n\nWelcome")
                    ch2 = int(input("\n\nWhat would you like to do?\n\n 1.Search by Category (or)\n\n 2.View Order status\n\nEnter option no.->"))
                    if ch2 == 1:
                        search()
                    elif ch2 == 2:
                        print("\n\nThis is your orders' status->\n\n")
                        cur.execute("select * from p_order where c_name = '%s'"%(c_name))
                        l3 = cur.fetchall()
                        cur.execute("desc p_order;")
                        slst2 = cur.fetchall()
                        get_header_rows(slst2)
                        print()
                        get_records(l3)
                        ch7 = int(input("\n\nDo u want to continue \n\n1.Buying(or)\n\n2.Exit?\n\nEnter choice no.: "))
                        if ch7 == 1:
                            search()
                        elif ch7 == 2:
                            print("\n\nThank you for visiting! Do check out our blog on Indian agricultures and current affairs!")
                        else:
                            print("\n\n******* Invalid entry! Try again. *******")
                    else:
                        print("\n\n******* Invalid entry! Try again. *******")
                else:
                    print("\n\n******* Oops!Invalid password!Try again. *******")
                    break
            else:
                print("\n\n******* Sorry, but it seems like this username does not exist. *******")
                c1 = input("\n\nWould you like to create a new Customer Account?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
                if c1 == "y":
                    while True:
                        new_cname = input("\n\nEnter new username (use only small case text, don't use any special character): ")
                        if new_cname in x:
                            print("\n\n******* Username already exists. Please choose a different username. *******")
                            continue
                        else:
                            while True:
                                new_cpwd = int(getpass("\n\nEnter a password for your account: "))
                                rnew_cpwd = int(getpass("\n\nRe-enter your new password: "))
                                if new_cpwd == rnew_cpwd:
                                    cur.execute("insert into c_credentials values('%s',%s);"%(new_cname,new_cpwd))
                                    conn.commit()
                                    print("\n\nYour Customer Account was successfully created.\n\nredirecting to login page...")
                                    break
                                else:
                                    print("\n\n******* Re-entered password not same as entered password, please retry. *******")
                                    continue
                            break
                else:
                    print("\n\n******* Sorry, but you need to create an account to continue.\n\nredirecting to home page...")
            break
        prompt = input("\n\nDo u want to continue to the FAB page?\n[enter 'y' to stay, any other character to exit]: ")
        if prompt == "y":
            continue
        else:
            print("\n\nThank you for using FAB, help support us by inviting more sellers and clients to this platform! Happy shopping!")
            print("© 2020, all rights reserved by Farmers' Association of BIA\n\n")
            break

    elif ch1 == 2: 
        #login
        s_name = input("\n\nEnter username: ")
        s_pwd = int(getpass("\n\nEnter password: "))
        while True:
            cur.execute("use fab;")
            cur.execute("select s_name from s_credentials;")
            p3 = cur.fetchall()
            w = []
            for i in range(len(p3)):
                t3 = p3[i]
                v3 = t3[0]
                w.append(v3)
            if s_name in w:
                cur.execute("select s_pwd from s_credentials;")
                p4 = cur.fetchall()
                z = []
                for i in range(len(p4)):
                    t4 = p4[i]
                    v4 = t4[0]
                    z.append(v4)
                if s_pwd in z:
                    cur.execute("use fab;")
                    print("\n\nWelcome")
                    fh1 = int(input("\n\nWhat would you like to do today?\n\n 1.Add new produce to the database(or)\n\n 2.View your orders?\n\nEnter option no.->"))
                    if fh1 == 1:
                        add_produce()
                    elif fh1 == 2:
                        print("\n\nThis is our orders' status->\n\n")
                        cur.execute("select * from p_order where s_name = '%s'"%(s_name))
                        l4 = cur.fetchall()
                        cur.execute("desc p_order;")
                        slst3 = cur.fetchall()
                        get_header_rows(slst3)
                        print()
                        get_records(l4)
                        fh3 = input("\n\nWould you like to approve any pending order?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
                        if fh3 == "y":
                            print()
                            get_header_rows(slst3)
                            print()
                            get_records(l4)
                            fh4 = int(input("\n\nPlease select the orderno of the order you would like to approve: "))
                            cur.execute("select iname from p_order where orderno = %s"%(fh4))
                            l7 = cur.fetchall()
                            fh5 = get_value(l7)
                            cur.execute("select qty_bought_in_tonnes from p_order where orderno = %s"%(fh4))
                            l9 = cur.fetchall()
                            fh7 = get_value(l9)
                            query2 = "update p_order set status = '%s' where orderno = %s"%('Approved',fh4)
                            cur.execute(query2)
                            conn.commit()
                            cur.execute("select qty_in_tonne from produce where s_name = '%s' and iname = '%s'"%(s_name,fh5))
                            l8 = cur.fetchall()
                            fh6 = get_value(l8)
                            rem_qty = fh6 - fh7
                            cur.execute("update produce set qty_in_tonne = %s where s_name = '%s' and iname = '%s'"%(rem_qty,s_name,fh5))
                            conn.commit()
                            cur.execute("select * from p_order where orderno = %s"%(fh4))
                            print(cur.fetchall())
                            print("\n\nYour selected order is approved. Payment link sent to customer via email. Can expect payment within 15 days from the date of approval.")
                            fh2 = input("\n\nHey "+s_name+"! Would you like to add a new produce for sale to the database?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
                            if fh2 == "y":
                                add_produce()
                            else:
                                print("\n\nOkay, hope to see you soon! Have a nice day!")
                        else:
                            print("\n\nOkay, hope to see you soon! Have a nice day!")
                    else:
                        print("\n\n******* Invalid entry! Try again. *******") 
                else:
                    print("\n\n******* Oops!Invalid password!Try again. *******")
                    break
            else:
                print("\n\n******* Sorry, but it seems like this username does not exist. *******")
                s1 = input("\n\nWould you like to create a new Seller Account?\n\n[enter 'y' for 'yes, any other character for 'no']: ")
                if s1 == "y":
                    while True:
                        new_sname = input("\n\nEnter new username (use only small case text, don't use any special character): ")
                        if new_sname in w:
                            print("\n\n******* Username already exists. Please choose a different username. *******")
                            continue
                        else:
                            while True:
                                new_spwd = int(getpass("\n\nEnter a password for your account: "))
                                rnew_spwd = int(getpass("\n\nRe-enter your new password: "))
                                if new_spwd == rnew_spwd:
                                    cur.execute("insert into s_credentials values('%s',%s);"%(new_sname,new_spwd))
                                    conn.commit()
                                    print("\n\nYour Seller Account was successfully created.\n\nredirecting to login page...")
                                    break
                                else:
                                    print("\n\n******* Re-entered password not same as entered password, please retry. *******")
                                    continue
                            break
                else:
                    print("\n\n******* Sorry, but you need to create an account to continue.\n\nredirecting to home page...")
            break
        prompt = input("\n\nDo you want to continue to the FAB page?\n[enter 'y' to stay, any other character to exit]: ")
        if prompt == "y":
            continue
        else:
            print("\n\nThank you for using FAB, help support us by inviting more sellers and clients to this platform! Happy shopping!")
            print("© 2020, all rights reserved by Farmers' Association of BIA\n\n")
            break
    
    elif ch1 == 3:
        #login
        a_name = input("\n\nEnter username: ")
        a_pwd = int(getpass("\n\nEnter password: "))
        while True:
            if a_name == "Riley":
                if a_pwd == 12345:
                    admin()
                else:
                    print("\n\n******* Oops!Invalid password!Try again. *******")
                    break
            else:
                print("\n\n******* Sorry, but no admin exists by your given username.\n\nredirecting to home page...")
            break
        prompt = input("\n\nDo you want to continue to the FAB page?\n[enter 'y' to stay, any other character to exit]: ")
        if prompt == "y":
            continue
        else:
            print("\n\nThank you for using FAB, help support us by inviting more sellers and clients to this platform! Happy shopping!")
            print("© 2020, all rights reserved by Farmers' Association of BIA\n\n")
            break

   except ValueError:
       print("\n\n******* Invalid entry!!Try again *******")
       continue