
tests = [
    {
        "name": "sample input",
        "employees": [
            "1,Richard,Engineering",
            "2,Erlich,HR",
            "3,Monica,Business",
            "4,Dinesh,Engineering",
            "6,Carla,Engineering",
            "9,Laurie,Directors",
#            "10,Dave,Business",
#            "12,Joe,Directors"
        ],
        "friendships": [
            "1,2",
            "1,3",
            "1,6",
            "2,4"
        ],
        "expected_output": {
            "Engineering": {"employees": 3, "employees_with_outside_friends": 2},
            "HR": {"employees": 1, "employees_with_outside_friends": 1},
            "Business": {"employees": 1, "employees_with_outside_friends": 1},
            "Directors": {"employees": 1, "employees_with_outside_friends": 0}
        }
    }
];


#Parse employee data
emp_tmp1=[]
emp_tmp2=[]
emp_id=[]
emp_dept=[]
emp_of=[]
dept=[]
dept_emp_ct=[]
dept_of_ct=[]
emp=tests[0]['employees']
for ec,e in enumerate(emp):
    emp_tmp1=tests[0]['employees'][ec]
    emp_tmp2=emp_tmp1.split(",")
    emp_id.append(emp_tmp2[0])
    emp_dept.append(emp_tmp2[2])
    emp_of.append("0")

    if emp_tmp2[2] not in dept:
        #dept_of_ct = dept_of_ct+1
        dept.append(emp_tmp2[2])
        dept_emp_ct.append(0)
        dept_of_ct.append(0)

#print("Employee data")
#print(emp_id)
#print(emp_dept)
#print(emp_of)
#print("Departments")
#print(dept)
#print(dept_of_ct)


#Parse friendships data
f_tmp1=[]
f_tmp2=[]
f1=[]
f2=[]
frd=tests[0]['friendships']
for fc,f in enumerate(frd):
    f_tmp1=tests[0]['friendships'][fc]
    f_tmp2=f_tmp1.split(",")
    f1.append(f_tmp2[0])
    f2.append(f_tmp2[1])

#print("Friends data")
#print(f1)
#print(f2)

#Compare friendships
for cc,f in enumerate(f1):
    c_f1_tmp=f1[cc]
    c_f2_tmp=f2[cc]
    #print(c_f1_tmp)
    #print(c_f2_tmp)
    for cc2,e in enumerate(emp_id):
        if (emp_id[cc2]) == c_f1_tmp:
            #print(emp_id[cc2])
            #print(c_f1_tmp)
            emp_dept_tmp=emp_dept[cc2]
            #print(emp_dept_tmp)
            for cc3,e in enumerate(emp_id):
                if (emp_id[cc3]) == c_f2_tmp:
                    emp_dept_tmp2=emp_dept[cc3]
                    #print(emp_dept_tmp2)
                    if emp_dept_tmp != emp_dept_tmp2:
                        emp_of[cc2]=1
                        emp_of[cc3]=1

#Count and output
#print(emp_id)
#print(emp_dept)
print(emp_of)

for dc,d in enumerate(dept):
    dc_tmp=dept[dc]
#    print(dc_tmp)
    for dc2,e in enumerate(emp_id):
        if dc_tmp == (emp_dept[dc2]):
            dept_emp_ct[dc]=dept_emp_ct[dc]+1
            #print(dept[dc], dept_emp_ct[dc])
            if emp_of[dc2] == 1:
                #print("emp_of is true")
                dept_of_ct[dc]=dept_of_ct[dc]+1

    print(dept[dc], dept_emp_ct[dc], dept_of_ct[dc])
