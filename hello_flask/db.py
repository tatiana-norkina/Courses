import sqlite3




# Create table
# cur.execute('''CREATE TABLE stocks
#                (date text, trans text, symbol text, qty real, price real)''')

# # Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
# con.commit()

def sqldata(qry):

    con = sqlite3.connect('example.db')

    cur = con.cursor()

    data = [row for row in cur.execute(qry)]

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()
    return data
