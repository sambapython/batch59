import sqlite3
def get_con():
	con = sqlite3.connect("db1.sqlite3")
	cur=con.cursor()
	return con,cur
def create_table():
	con,cur=get_con()
	q="create table customer (id int, name varchar(250))"
	cur.execute(q)
	con.close()
def insert():
	c_id = input("Enter customer id:")
	c_name = input("enter cusatomer name:")
	q=f"insert into customer(id, name) values({c_id},'{c_name}')"
	con,cur=get_con()
	cur.execute(q)
	con.commit()
	con.close()
def browse(c_id=None):
	con,cur=get_con()
	if c_id:
		q=f"select * from customer where id={c_id}"
	else:
		q=f"select * from customer"
	cur.execute(q)
	data = cur.fetchall()
	con.close()
	return data
def update():
	c_id = input("Enter customer id:")
	c_name = input("enter cusatomer name:")
	exist_record = browse(c_id)
	print(exist_record)
	opt = input("Do you want to update(y/n)?")
	if opt=="y":
		con,cur=get_con()
		q=f"update customer set name='{c_name} where id={c_id}"
		cur.execute()
		con.commit()
		con.close()


