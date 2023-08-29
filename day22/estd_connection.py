# if we want to connect a database from a program ( Python,javaScript) then we need a database connector
# Database connector connects your program with database
# mysqlclient,psycopg2 etc are the db connectors


def estd_connection():
    import psycopg2         # python connection of postgress
    conn=psycopg2.connect(
        database="studenttestdb",
        user="postgres",
        password="postgress1212",    #own password
        host="127.0.0.1",
        port=5432
    )

    conn.autocommit=True
    print("Connection established successfully !!")
    cursor=conn.cursor()
    return cursor         

if __name__=="__main__":
    estd_connection()