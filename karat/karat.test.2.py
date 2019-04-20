def get_employee_stats(employees, friendships):
    # IMPLEMENTATION GOES HERE

    #Parse employee data
    emp_tmp1=[]
    emp_tmp2=[]
    emp_id=[]
    emp_dept=[]
    emp_of=[]
    dept=[]
    dept_emp_ct=[]
    dept_of_ct=[]

    for ec,e in enumerate(employees, 0):
        emp_tmp1=employees[ec]
        emp_tmp2=emp_tmp1.split(",")
        emp_id.append(emp_tmp2[0])
        emp_dept.append(emp_tmp2[2])
        emp_of.append("0")

        #Create Department list
        if emp_tmp2[2] not in dept:
            dept.append(emp_tmp2[2])
            dept_emp_ct.append(0)
            dept_of_ct.append(0)

    #Parse friendships data
    f_tmp1=[]
    f_tmp2=[]
    f1=[]
    f2=[]

    for fc,f in enumerate(friendships):
        f_tmp1=(friendships)[fc]
        f_tmp2=f_tmp1.split(",")
        f1.append(f_tmp2[0])
        f2.append(f_tmp2[1])

    #Compare friendships
    for cc,f in enumerate(f1):
        c_f1_tmp=f1[cc]
        c_f2_tmp=f2[cc]
        for cc2,e in enumerate(emp_id):
            if (emp_id[cc2]) == c_f1_tmp:
                emp_dept_tmp=emp_dept[cc2]
                for cc3,e in enumerate(emp_id):
                    if (emp_id[cc3]) == c_f2_tmp:
                        emp_dept_tmp2=emp_dept[cc3]
                        if emp_dept_tmp != emp_dept_tmp2:
                            emp_of[cc2]=1
                            emp_of[cc3]=1

    #Count and output
    output={}
    tmp_out=[]
    for dc,d in enumerate(dept):
        dc_tmp=dept[dc]
        for dc2,e in enumerate(emp_id):
            if dc_tmp == (emp_dept[dc2]):
                dept_emp_ct[dc]=dept_emp_ct[dc]+1
                if emp_of[dc2] == 1:
                    dept_of_ct[dc]=dept_of_ct[dc]+1

        #output.append( '"' + dept[dc] + '": {"employees": ' + str(dept_emp_ct[dc]) + ', "employees_with_outside_friends": ' + str(dept_of_ct[dc]) + '}')

        #output.append('' + dept[dc] + '": {"employees": ' + str(dept_emp_ct[dc]) + ', "employees_with_outside_friends": ' + str(dept_of_ct[dc]) + '}')
        #tmp_out.append(dept[dc] + '\': {\'employees\': ' + str(dept_emp_ct[dc]))
        tmp_out=('{\'employees\': ' + str(dept_emp_ct[dc]) + ', \'employees_with_outside_friends\': ' + str(dept_of_ct[dc]) + '}')
        #print(tmp_out)

        #output[dept[dc]] = tmp_out.strip('\"')
        output[dept[dc]] = tmp_out

    print("Output")
    #print(output.replace('"', ''))
    out2=output
    print(out2.replace('"', ''))

    return output


# START TEST CASES
#
# You can add test cases below. Each test case should be a dict of the format:
#
# {
#     "name": "my custom test",
#     "employees": ...,
#     "frienships": ...,
#     "expected_output": ...
# }


tests = [
    {
        "name": "sample input",
        "employees": [
            "1,Richard,Engineering",
            "2,Erlich,HR",
            "3,Monica,Business",
            "4,Dinesh,Engineering",
            "6,Carla,Engineering",
            "9,Laurie,Directors"
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

# END TEST CASES
# DO NOT MODIFY BELOW THIS LINE

def main():
    def equal_outputs(a, b):
        return a == b

    passed = 0

    for test in tests:
        try:
            print("==> Testing {}...".format(test['name']))
            actual_output = get_employee_stats(test['employees'], test['friendships'])
            print("Actual_Output")
            print(actual_output)
            print("Expected_Output")
            #print(test)
            print(test['expected_output'])
            if equal_outputs(actual_output, test['expected_output']):
                print("PASS")
                passed += 1
            else:
                print("FAIL")
        except Exception as e:
            print("FAIL")
            print(e)

    print("==> Passed {} of {} tests".format(passed, len(tests)))

if __name__ == '__main__':
    main()
