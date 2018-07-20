#!/usr/bin/python3
""" takes in name of state as argument and lists all cities of that state """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    lst = []
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name from cities \
    INNER JOIN states ON cities.state_id = states.id \
    WHERE states.name LIKE BINARY %s ORDER BY cities.id", (argv[4],))
    cities = cur.fetchall()
    citycount = len(cities)
    for city in cities:
        lst.append(city[0])
    print(', '.join(lst))
    cur.close()
    db.close()
