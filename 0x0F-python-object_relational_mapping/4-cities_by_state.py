#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name from cities \
    INNER JOIN states on cities.state_id = states.id ORDER BY cities.id")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
