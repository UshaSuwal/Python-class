
from estd_connection import estd_connection

cursor=estd_connection()

#cursor.execute("DROP TABLE STUDENT")    # pailai table exist xa vane first tyo table drop garxa then again create

sql="""
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    AGE INT
)
"""
cursor.execute(sql)
print("Table Created Successfully !!")