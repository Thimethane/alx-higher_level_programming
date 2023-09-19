#!/usr/bin/python3
""" The script that uses parameterized queries to prevent SQL injection"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    List all states from a MySQL database.

    Usage: ./0-select_states.py <mysql_username>
    <mysql_password> <database_name>
    """
    # Get MySQL credentials and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    """
    Execute the parameterized query to retrieve states
    matching the provided name
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
