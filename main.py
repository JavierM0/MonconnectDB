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

#mongodb delete operations

#mongodb delete one employee
print('Example query: : {"empno":7934, "ename":"MILLER", "job":"CLERK", "sal":1300}')
emp_num = int(input('Input empno: '))
emp_ename = input('Input ename: ').upper()
emp_job = input('Input job: ').upper()
emp_sal = int(input('Input sal: '))
query={"empno":emp_num, "ename":emp_ename, "job":emp_job, "sal":emp_sal}
collection.delete_one(query)
print('Procedure accepted')

#mongodb delete one job
print('Example query: : {"job":"CLERK"}')
emp_job = input('Input job: ').upper()
query={"job":emp_job}
collection.delete_many(query)
print('Procedure accepted')

#mongodb delete one department
print('Example query: : {"departamento.deptno":10, "departamento.dname":"ACCOUNTING", "departamento.loc":"NEW YORK"}')
emp_deptno = int(input('Input deptno: '))
emp_dname = input('Input dname: ').upper()
emp_loc = input('Input loc: ').upper()
query={"departamento.deptno":emp_deptno, "departamento.dname":emp_dname, "departamento.loc":emp_loc}
collection.delete_many(query)
print('Procedure accepted')


