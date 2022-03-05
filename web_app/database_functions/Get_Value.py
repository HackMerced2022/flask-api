import psycopg2

def get_value(elephantsql_client, command):
    # A "cursor", a structure to iterate over db records to perform queries
    cur = elephantsql_client.cursor()

    try:
        # Execute commands in order
        cur.execute(command)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        elephantsql_client.rollback()
        cur.close()
        return 1

    # Get cur value
    returned = cur.fetchall()
    
    # Close communication with the PostgreSQL database server
    cur.close()

    return returned