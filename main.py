import pymysql
db=pymysql.connect(host='localhost',user='root',password='123456',db='to_do_list')
def add_task():
    a=db.cursor()
    task_id=input("Enter task id")
    time=input("Enter time")
    task=input("kindly add you task name:-")
    status=input("Status of your task :-To be done /In process/Completed")
    date=input("Kindly enter the date:-")
    data=(task_id,time,date,task,status)
    sql='insert into all_task values(%s,%s,%s,%s,%s)'
    a.execute(sql,data)
    print("Task added successfully :)")
    db.commit()
def view_all_task():
    a = db.cursor()
    sql = 'select * from all_task'
    a.execute(sql)
    x=a.fetchall()
    for i in x:
        print("Task are :\n",i)
    db.commit()
def update_the_task():
    a = db.cursor()
    tid=input("Enter the task ID you want to update:-")
    data=(tid,)
    sq='select * from all_task where task_id=%s'
    a.execute(sq,data)
    y=a.fetchall()
    for j in y:
        print(j)
    while(True):
        print("Which field you want to update?")
        print("1]Task ID\n2]Time of the task\n3]Date of the task\n4]Task name\n5]Status of the task\n6]Exit")
        ch=int(input("Enter your choice"))
        if ch==1:
            newid=input("Enter new ID:-")
            data1=(newid,tid)
            sql1='update all_task set task_id=%s where task_id=%s '
            a.execute(sql1,data1)
            print("Task ID has been updated")
        elif ch==2:
            newtime=input("Enter new time:-")
            data6=(newtime,tid)
            sql6='update all_task set time=%s where task_id=%s '
            a.execute(sql6,data6)
            print("Task time has been updated")
        elif ch==3:
            newdate=input("Enter new date:-")
            data2=(newdate,tid)
            sql2='update all_task set date_of_task=%s where task_id=%s '
            a.execute(sql2,data2)
            print("Task date has been updated")
        elif ch==4:
            newtask=input("Enter new name:-")
            data3=(newtask,tid)
            sql3='update all_task set task_name=%s where task_id=%s '
            a.execute(sql3,data3)
            print("Task name has been updated")
        elif ch==5:
            newstatus=input("Enter new status:-")
            data4=(newstatus,tid)
            sql4='update all_task set status_of_the_task=%s where task_id=%s '
            a.execute(sql4,data4)
            print("Task status has been updated")
        elif ch==6:
            print("Thankyou:-)")
            break
        else:
            print("Please enter valid choice:-")
            continue
    db.commit()
def delete_the_task():
        a = db.cursor()
        tid = input("Enter task ID of which you want to delete the data:-")
        data = (tid)
        sql = 'select * from all_task where task_id=%s'
        a.execute(sql, data)
        x = a.fetchall()
        for i in x:
            print("Data of id :-", i)
        print("Are you sure you want to delete this data ?")
        print("1]Yes\n2]No")
        ch = int(input("Enter your choice:-"))
        if ch == 1:
            sql1 = 'delete from all_task where task_id=%s'
            a.execute(sql1, data)
            print("Record has been deleted successfully ")
        db.commit()

while (True):
    print("\t\t\t\t\t\t\t\t\t\tTO-DO-LIST")
    print("********************************************************************************************")
    print("\t1]Insert the task  \t2]View all task  \t3]Update the task  \t4]Delete the task  \t5]Exit")
    print("********************************************************************************************")

    ch = int(input("Please enter you choice:-"))
    if ch == 1:
        add_task()
    elif ch == 2:
        view_all_task()
    elif ch == 3:
        update_the_task()
    elif ch == 4:
        delete_the_task()
    elif ch == 5:
        print("Thankyou")
        break
    else:
        print("Enter valid choice:")
        continue




