import sqlite3



conn=sqlite3.connect('hotel.db')

#cursor
c=conn.cursor()
'''c.execute("""CREATE TABLE place_orderss (order_id text,dish_id int,dishname text,
    tableno int,
    quantity int,
    price double,
    FOREIGN KEY(dish_id) REFERENCES dishes(dish_id),
    FOREIGN KEY(price) REFERENCES dishes(price))"""
          )'''
#c.execute("SELECT * FROM place_orderss ")
query = "SELECT c_email,c_passwrd FROM chef_reg "
#query= "DELETE FROM chef_reg WHERE c_email=''"
#query = "SELECT email,passwrd FROM cust_reg"
#query = "DELETE  FROM place_orderss WHERE order_id=? and oid=? "
#query = "SELECT sum(price)  FROM place_orderss WHERE order_id=? "


# insert into table
c.execute(query)
res=c.fetchall()

print(res)
conn.commit()
conn.close()

