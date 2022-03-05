import psycopg2

def execute_command(elephantsql_client, insert_req):
    """ Execute a single INSERT request """
    try:
        # Create cursor object
        cur = elephantsql_client.cursor()

        # Execute command
        cur.execute(insert_req)

        # Commit changes
        elephantsql_client.commit()
    except (Exception, psycopg2.DatabaseError) as error:

        print("Error: %s" % error)

        # Reset to prev database state
        elephantsql_client.rollback()

        # Close cursor object
        cur.close()
        return 1
        
    cur.close()