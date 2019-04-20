karat.notes.py
>>> tests[0]['employees'][0]
'1,Richard,Engineering'
>>> tests[0]['employees'][0][0]
'1'


>>> tests[0]['friendships'][0][0]
'1'
>>> tests[0]['friendships'][0][1]
','
>>> tests[0]['friendships'][0][2]
'2'
>>>


emp=tests[0]['employees'][0]
emp.split(",")

frd=tests[0]['friendships'][0]
frd.split(",")

emp_list=[]

>>> emp_list=emp.split(",")
>>> emp_list
['1', 'Richard', 'Engineering']


for i in range(1, 6):
        emp=tests[0]['employees'][i]
        >>> tests[0]['employees'][0]
'1,Richard,Engineering'
>>> tests[0]['employees'][0][0]
'1'


>>> tests[0]['friendships'][0][0]
'1'
>>> tests[0]['friendships'][0][1]
','
>>> tests[0]['friendships'][0][2]
'2'
>>>


emp=tests[0]['employees'][0]
emp.split(",")

frd=tests[0]['friendships'][0]
frd.split(",")

emp_list=[]

>>> emp_list=emp.split(",")
>>> emp_list
['1', 'Richard', 'Engineering']

#Create a single list, but not nested
emp_list=[]
for e in range(1, 6):
        emp=tests[0]['employees'][e]
        emp_list.extend(emp.split(","))

#Create a nested list
emp_list=[]
for e in range(1, 6):
        emp=tests[0]['employees'][e]
        emp_list[e]=emp.split(",")

#Create multi list
emp_tmp1=[]
emp_tmp2=[]
emp_id=[]
emp_dept=[]
emp_of=[]
emp=tests[0]['employees']
for i,e in enumerate(emp):
        print(i)
        emp_tmp1=tests[0]['employees'][i]
        emp_tmp2=emp_tmp1.split(",")
        emp_id.append(emp_tmp2[0])
        emp_dept.append(emp_tmp2[2])
        emp_of.append("0")
