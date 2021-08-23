from controllers.create import create_student_table, insert_data 
from controllers.read import print_table_description, print_student_data
from controllers.update import update_table_schema, update_marks_by_id
from controllers.delete import drop_student_table, delete_by_id


from utils.data import student_data


#create operations
create_student_table()
insert_data(student_data)


#update operations
update_table_schema()
update_marks_by_id(1, 80)


#read operations
print_table_description()
print_student_data()


#delete operations
delete_by_id(2)
drop_student_table()