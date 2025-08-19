import sqlite3
import datetime


DB_NAME="expenses.db"

def create_table():
  conn=sqlite3.connect(DB_NAME)
  c=conn.cursor()
  c.execute('''create table if not exists expenses(
            id INTEGER primary key AUTOINCREMENT,
            date text,
            amount REAL,
            category TEXT,
            note text)''')
  conn.commit()
  conn.close()

def add_expense(amount,category,note=" "):
  conn=sqlite3.connect(DB_NAME)
  c=conn.cursor()
  date=datetime.date.today().isoformat()
  c.execute("Insert into expenses(date,amount,category,note) VALUES(?,?,?,?)",(date,amount,category,note))
  conn.commit()
  conn.close()
  print("Expense Added Successfully")

def list_expenses():
  conn=sqlite3.connect(DB_NAME)
  c=conn.cursor()
  c.execute("SELECT * FROM expenses order by date DESC ")
  rows=c.fetchall()
  conn.close()
  if not rows:
    print("not expense found")
    return
  print("\nID  |  Amount  | category  | Note")
  print("-"*50)
  for row in rows:
    print(f"{row[0]:<3}  {row[1]:<10} {row[2]:<8} {row[3]:<10} {row[4]}")
    print()

def delete_expense(expense_id):
  conn=sqlite3.connect(DB_NAME)
  c=conn.cursor()
  c.execute("delete from expenses Where id=?",(expense_id,))
  conn.commit()
  conn.close()

  print("Expense deleted successfully")


def summary_by_category():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = c.fetchall()
    conn.close()
    print("\nCategory-wise Summary")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]}: {row[1]}")
    print()

  


  

def  main():
  create_table()
  while True:
   print("\nExpense Tracker")
   print("\n1.Add Expense")
   print("\n2.List Expense")
   print("\n3.Delete Expnse")
   print("\n4.Summary by Category")
   print("\nExit")
   choice=input("Please Enter your choise")

   if choice=="1":
     amount=float(input("Enter amount "))
     category=input("Enter category")
     note=input("Enter note (optional)")
     add_expense(amount,category,note)
   elif choice=="2":
     list_expenses()
   elif choice=="3":
     expense_id=input("Please Enter expense id for deleting Expense")
     delete_expense(expense_id)
   elif choice =="4":
     summary_by_category()
   elif choice=="5":
     print("Bye")
     break
   else:
     print("Invalid Choice Please Try again")

     
 

     







if __name__ =="__main__":
    main()
