import pymongo

#mongodb connection
connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)

database_name="scott"
student_db=client[database_name]

collection_name="rh"
collection=student_db[collection_name]

#mongodb read operations
print('Example query: : {"empno":"7369"}')
inp_emp = int(input('Input empno: '))
query={"empno":inp_emp}
result=collection.find(query)
for i in result:
    print(i)

print('Example query: : {"ename":"SMITH"}')
inp_emp = input('Input ename: ').upper()
query={"ename":inp_emp}
result=collection.find(query)
for i in result:
    print(i)

print('Example query: : {"job":"CLERK"}')
inp_emp = input('Input job: ').upper()
query={"job":inp_emp}
result=collection.find(query)
for i in result:
    print(i)

print('Example query: : {"sal":"800"}')
inp_emp = int(input('Input sal: '))
query={"sal":inp_emp}
result=collection.find(query)
for i in result:
    print(i)

print('Example query: : {"departamento.deptno":20}')
inp_emp = int(input('Input deptno: '))
query={ "departamento.deptno":inp_emp}
result=collection.find(query)
for i in result:
    print(i)

print('Example query: : {"departamento.dname":"RESEARCH}')
inp_emp = input('Input dname: ').upper()
query={ "departamento.dname":inp_emp}
result=collection.find(query)
for i in result:
    print(i)

print('Example query: : {"departamento.loc":"DALLAS"}')
inp_emp = input('Input loc: ').upper()
query={ "departamento.loc":inp_emp}
result=collection.find(query)
for i in result:
    print(i)

#mongodb update operations

#mongodb update employee
print('Example query: : {"empno":7934}')
emp_num = int(input('Input empno: '))
query={"empno":emp_num}
present_data = collection.find_one(query)
print(present_data)

new_num = int(input('Input new empno: '))
new_ename = input('Input new ename: ').upper()
new_job = input('Input new job: ').upper()
new_sal = int(input('Input new sal: '))
new_deptno = int(input('Input deptno: '))
new_dname = input('Input dname: ').upper()
new_loc = input('Input loc: ').upper()

new_data = {"$set":{"empno":new_num, "ename":new_ename, "job":new_job, "sal":new_sal, "departamento.deptno":new_deptno, "departamento.dname":new_dname, "departamento.loc":new_loc}}
result = collection.update_one(present_data, new_data)
print(result.modified_count, " object modified")

#mongodb update department 
"""
print('Example query: : {"deptno":20}')
deptno_num = int(input('Input empno: '))
query={"departamento.deptno":deptno_num}
present_data = collection.find(query)
print(collection.find_one(query))

new_deptno = int(input('Input deptno: '))
new_dname = input('Input dname: ').upper()
new_loc = input('Input loc: ').upper()

new_data = {"$set":{"departamento.deptno":new_deptno, "departamento.dname":new_dname, "departamento.loc":new_loc}}
result = collection.update_many(present_data, new_data)
print(result.modified_count, " object modified")
"""

#mongodb delete operations

#mongodb delete one employee
print('Example query: : {"empno":7934, "ename":"MILLER", "job":"CLERK", "sal":1300}')
emp_num = int(input('Input empno: '))
emp_ename = input('Input ename: ').upper()
emp_job = input('Input job: ').upper()
emp_sal = int(input('Input sal: '))
query={"empno":emp_num, "ename":emp_ename, "job":emp_job, "sal":emp_sal}
result = collection.find_one_and_delete(query)
print(result)

#mongodb delete one job
print('Example query: : {"job":"CLERK"}')
emp_job = input('Input job: ').upper()
query={"job":emp_job}
result = collection.delete_many(query)
print(result.deleted_count, " documents deleted")

#mongodb delete one department
print('Example query: : {"departamento.deptno":10, "departamento.dname":"ACCOUNTING", "departamento.loc":"NEW YORK"}')
emp_deptno = int(input('Input deptno: '))
emp_dname = input('Input dname: ').upper()
emp_loc = input('Input loc: ').upper()
query={"departamento.deptno":emp_deptno, "departamento.dname":emp_dname, "departamento.loc":emp_loc}
result = collection.delete_many(query)
print(result.deleted_count, " documents deleted")

