from estd_connection import estd_connection




def delete_student(student_id):
    cursor=estd_connection()
    sql=f"""
    DELETE FROM STUDENT WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    print("Deleted Successfully")
    repeat=input("Do you want to continue? (Y/N)")
    return True if repeat.lower()=='y' else False


# read xuttai and write xuttai gareko because:
# delete garesi list will be small than previous so r+ garda tala ko remaining baki hunxa 
# so write xuttai gareko.write le purai over write gardinxa.
    