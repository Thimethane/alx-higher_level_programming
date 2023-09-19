#!/usr/bin/python3
""" Takes the state name as an argument and lists all cities for that state"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    # Expecting: username, password, database name, state name
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    # Execute the SQL query to join cities and states,
    # and fetch city names for the specified state
    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
    """
    cursor.execute(query, (state_name,))

    # Fetch all the city names for the specified state
    cities = [row[0] for row in cursor.fetchall()]

    # Print the city names, separated by commas
    print(", ".join(cities))

    # Close the cursor and connection
    cursor.close()
    db.close()
