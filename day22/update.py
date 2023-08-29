from estd_connection import estd_connection

def update_student(student_id):
    cursor=estd_connection()
    key=input("Enter info you want to update ")
    new_value=input("Enter the new value ")

    sql=f"""
    UPDATE STUDENT SET {key}='{new_value}' WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    print(" Student updated succesfully")

            
    repeat=input("Do you want to continue? (Y/N)")
    return True if repeat.lower()=='y' else False


