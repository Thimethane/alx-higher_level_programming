#!/usr/bin/python3
""" lists all states with a name starting with 'N' (upper N) """
import MySQLdb
import sys


if __name__ == "__main__":
    """
    List all states from a MySQL database.

    Usage: ./0-select_states.py <mysql_username>
    <mysql_password> <database_name>
    """
    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        )

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
