# Qs1 Database : a database is an organized collection of data where we can easily store and retrieve data
# sql databases = relational databases...store data in a particular format
# no sql databases = distributed databses .... store databases in a dynamic format
# Qs2 DDL stands for data definition language. It is used to define what type of data we are storing in a relation
#create = used to create a table
print("CREATE TABLE if not exists database_name.tablename(columns + datatype)")
#drop = used to delete the entire table
print("Drop table database.tablename")
#alter = it is used to modify a table ..i.e. add or subtract rows or columns
print("ALTER table table_name add column colours datatype")
#truncate = used to empty the contents of a table
print("truncate table table_name")

#Qs 2 DML = it stands for data manipulation lanuage ... it is used to manipulate the data in a table
# insert = used to insert records into a table
print("insert into table table_name values (..........)")
# update = used to update an existing table
print("update tablename Set column = value WHERE condition")
# delete = used to delete records ina table
print("delete from table_name where condition")

#Qs 4 DQL = it stands for data query language and is used to extract data from a table using queries
print("SELECT * FROM table_name") # selects all columns from a table
print("select c1 , c2 from table_name") # selects selected columns from a table

#Qs 5 primary key = it is a column which uniquely identifies each record in a relation
# used to define by writing "PRIMARY KEY" infront of table while creating columns
# foreign key = used to link two tables together....it refers to primary key in another table

#Qs 6 python code used to connect mysql
import mysql.connector
mydb = mysql.connector.connect( host = "localhost" , user = "abc" , password = "password")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
#CURSOR() =  used to exceute statements to communicate with sql database
#execute() = when combined with cursor executes all sql statements

#Qs7 Order of execution of sql clauses ina sql query
# from , group by , having , select , order by , limit/offset 

