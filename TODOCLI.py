import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="todo",
    password="00000",
    database="todo",
    port=3306
)

cursor=db.cursor()
table_name= "todo"

queries={"tasks": {"query":"""CREATE TABLE IF NOT EXISTS todo(task_id INT AUTO_INCREMENT PRIMARY KEY,
                                                                status VARCHAR(20),
                                                                what_todo VARCHAR(255))"""}}



task={
    "tasks": {"todo":["task_id",
                     "status",
                     "what_todo"],
                    "primary_key":"task_id"}
}

def create_table(cursor, db):
    query= queries["tasks"]["query"]
    cursor.execute(query)
    db.commit()
    print("Table is ready.")

def create(cursor, db,task,data,table_name):
    pk= task["tasks"]["primary_key"]
    columns=[col for col in task["tasks"]["todo"] if col != pk]
    placeholders=", ".join(["%s"] * len(columns)) 
    fields= ", ".join(columns)
    query=f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})"
    print(query)
    cursor.execute(query, tuple(data[column] for column in columns))
    db.commit()
    print("Record Created")
def read(cursor, db,table_name):
    cursor.execute(f"SELECT  * FROM {table_name}")
    for row in cursor.fetchall():
        print(row)
def update(cursor, db, task, pk_value, updated_data,table_name):
    pk = task["tasks"]["primary_key"]
    columns=[todo for todo in task["tasks"]["todo"] if todo != pk]
    placeholders= ", ".join([f"{col}=%s" for col in columns])
    query= f"UPDATE {table_name} SET {placeholders} WHERE {pk}=%s"
    print(query)
    cursor.execute(query, tuple(updated_data[column] for column in columns) + (int(pk_value),))
    db.commit()
    print("Record Updated.")

def delete(cursor, db,task, pk_value,table_name):
    pk= task["tasks"]["primary_key"]
    query=f"DELETE FROM {table_name} WHERE {pk}=%s"
    cursor.execute(query,(int(pk_value),))
    db.commit()
    print("Record Deleted.")

def mark_as_done(cursor, db, task,table_name):
    pk = task["tasks"]["primary_key"]
    cursor.execute(f"SELECT  * FROM {table_name} ")
    print("\n   Current Tasks    ")
    columns = task["tasks"]["todo"]
    for row in cursor.fetchall():
        row_dic= dict(zip(columns, row))
        print(f"{row_dic[pk]} | {row_dic['status']} | {row_dic['what_todo']}")

    choice = input(f"\n Enter {pk} of task to mark as done (or press enter to cancel.):")
    if not choice.strip():
        print("Cancelled.")
        return
    elif choice.strip():
        query = f"UPDATE {table_name} SET status=%s WHERE {pk}=%s"
        cursor.execute(query,("Done",(int(choice))))
        db.commit()
        print(f"Task {choice} marked as done ✅")

def main():
    create_table(cursor,db)
    print("SELECT OPERATION.\n 1. CREATE \n2. UPDATE \n 3. DELETE \n4. READ \n5. MARKS AS DONE")
    option=input("Enter option:")
    if option == '1':
        data= {"status": "Pending", "what_todo": input("Enter new task:")}
        create(cursor,db,task,data,table_name)
    elif option == '2':
        pk_value=input("Enter Task number: ")
        updated_data={"status":"Pending", "what_todo": input("Edit task:")}
        update(cursor, db, task, pk_value, updated_data,table_name)
    elif option == '3':
        pk_value=input("Enter Task number: ")
        delete(cursor, db,task, pk_value,table_name)
    elif option == '4':
        read(cursor, db,table_name)
    elif option == '5':
        mark_as_done(cursor, db,task,table_name)
    else:
        print("Invalid Input.")
if __name__ == "__main__":
    main()