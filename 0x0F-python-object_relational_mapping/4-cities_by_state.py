#!/usr/bin/python3
""" Script that lists all cities from the database """
import MySQLdb
import sys


if __name__ == "__main__":
    """
    List all states from a MySQL database.

    Usage: ./0-select_states.py <mysql_username>
    <mysql_password> <database_name>
    """
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve cities with their respective states
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
