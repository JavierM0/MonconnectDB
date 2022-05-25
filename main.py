import os
import pymongo

#mongodb connection
connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)
database_name="scott"
student_db=client[database_name]
collection_name="rh"
collection=student_db[collection_name]

#   create(7777, "ANDRES", "ANALYST", 3000, 20, "RESEARCH", "DALLAS")
def create(empno, ename, job, sal, deptno, dname, loc):
	doc = {
			"empno": empno,
			"ename": ename,
			"job": job,
			"sal": sal,
			"departamento": {
				"deptno": deptno,
				"dname": dname,
				"loc": loc
				}
			}
	return collection.insert_one(doc)

#   read(loc = "DALLAS")
def read(empno = None, ename = None, job = None, sal = None, deptno = None, dname = None, loc = None):
	query = dict()
	if empno: query["empno"] = empno
	if ename: query["ename"] = ename
	if job: query["job"] = job
	if sal: query["sal"] = sal
	if deptno: query["departamento.deptno"] = deptno
	if dname: query["departamento.dname"] = dname
	if loc: query["departamento.loc"] = loc
	return collection.find(query)

#   update(7777, loc = "LA", deptno = 13)
def update(empno, ename = None, job = None, sal = None, deptno = None, dname = None, loc = None):
	query = {
			"empno": empno
			}
	doc = dict()
	if ename: doc["$set"] = { "ename" : ename }
	if job: doc["$set"] = { "job" : job }
	if sal: doc["$set"] = { "sal" : sal }
	if deptno: doc["$set"] = { "departamento.deptno" : deptno }
	if dname: doc["$set"] = { "departamento.dname" : dname }
	if loc: doc["$set"] = { "departamento.loc" : loc }
	return collection.update_one(query, doc)

#   delete(7777)
def delete(empno):
	query = {
			"empno": empno
			}
	return collection.delete_one(query)

CRUD = "\
  .oooooo.   ooooooooo.   ooooo     ooo oooooooooo.   \n\
 d8P'  `Y8b  `888   `Y88. `888'     `8' `888'   `Y8b  \n\
888           888   .d88'  888       8   888      888 \n\
888           888ooo88P'   888       8   888      888 \n\
888           888`88b.     888       8   888      888 \n\
`88b    ooo   888  `88b.   `88.    .8'   888     d88' \n\
 `Y8bood8P'  o888o  o888o    `YbodP'    o888bood8P'   \n\
"
while os.system("clear") == False:
	print(CRUD)
	x = input("command: ")[0].upper()
	if x == "C":
		empno = int(input("\tempno: "))
		ename = input("\tename: ")
		job = input("\tjob: ")
		sal = int(input("\tsal: "))
		deptno = int(input("\tdeptno: "))
		dname = input("\tdname: ")
		loc = input("\tloc: ")
		print(create(empno, ename, job, sal, deptno, dname, loc))
	if x == "R":
		empno = input("\tempno: ")
		empno = int(empno) if empno else None
		ename = input("\tename: ")
		job = input("\tjob: ")
		sal = input("\tsal: ")
		sal = int(sal) if sal else None
		deptno = input("\tdeptno: ")
		deptno = int(deptno) if deptno else None
		dname = input("\tdname: ")
		loc = input("\tloc: ")
		for i, emp in enumerate(read(empno, ename, job, sal, deptno, dname, loc)):
			print(i, emp)
	if x == "U":
		empno = int(input("\tempno: "))
		ename = input("\tename: ")
		job = input("\tjob: ")
		sal = input("\tsal: ")
		sal = int(sal) if sal else None
		deptno = input("\tdeptno: ")
		deptno = int(deptno) if deptno else None
		dname = input("\tdname: ")
		loc = input("\tloc: ")
		print(update(empno, ename, job, sal, deptno, dname, loc))
	if x == "D":
		empno = int(input("\tempno: "))
		print(delete(empno))
	input()

