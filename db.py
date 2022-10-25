import psycopg2

DEFAULT_DATABSE_NAME = "nftdb"
DEFAULT_TABLE_NAME = "tokens"

CREATE_DATABASE_QUERY = "CREATE DATABASE " + DEFAULT_DATABSE_NAME
CREATE_TABLE_QUERY  = "CREATE TABLE " + DEFAULT_TABLE_NAME + \
                        " (token_id TEXT PRIMARY KEY NOT NULL, \
                            name TEXT NOT NULL, \
                            image TEXT NOT NULL, \
                            description TEXT NOT NULL, \
                            token_uri TEXT NOT NULL);"

INSERT_DATA_QUERY = "INSERT INTO " + DEFAULT_TABLE_NAME + "(token_id, name, image, description, token_uri)" + \
                    " VALUES (%s, %s, %s, %s, %s)"

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "root"

def checkDatabaseExistence(cursor) -> bool:

    cursor.execute("SELECT datname FROM pg_catalog.pg_database;")
    databases = cursor.fetchall()

    if( (DEFAULT_DATABSE_NAME, ) in databases):
        print("Database status is: True")
        return True 
    return False
    print("Database status is: False")

def checkTableExistence(cursor) -> bool:


    check_table_existence_query = "select exists(select * from information_schema.tables where table_name='" + DEFAULT_TABLE_NAME + "')"

    cursor.execute(check_table_existence_query)

    exists = cursor.fetchone()[0]
    print("Table status is: " + str(exists))
    return exists

def connect(dbname=DEFAULT_DATABSE_NAME, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host="localhost", port=5432):
    if(dbname is None):
        conn = psycopg2.connect(user=user, password=password, 
                            host="localhost", port=5432)

        return conn

    elif(dbname is not None):
        conn = psycopg2.connect(database=dbname, user=user, password=password, 
                            host="localhost", port=5432)

        return conn


def save(data: list) -> bool:
    

    conn = None 
    cursor = None

    try:
        conn = connect(dbname=DEFAULT_DATABSE_NAME)
    
    except Exception as e:
        print(e)
        conn = connect(dbname=None)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        cursor.execute(CREATE_DATABASE_QUERY)
        cursor.close()
        conn.close

    conn = connect(dbname=DEFAULT_DATABSE_NAME)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    if(not checkTableExistence(cursor)):
        print("Creating a table")
        cursor.execute(CREATE_TABLE_QUERY)
        

    for element in data:
        
        record_to_insert = (element["token_id"], element["name"], element["image"], element["description"], element["token_uri"])
        #print(cursor.mogrify(INSERT_DATA_QUERY, (42, "ff", "ff", "ff", "ff")))
        try:
            cursor.execute(INSERT_DATA_QUERY, record_to_insert)
        except:
            continue
        

    if(cursor):
        cursor.close()

    if(conn):
        conn.close() 