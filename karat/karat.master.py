def get_employee_stats(employees, friendships):
    # IMPLEMENTATION GOES HERE
    return {}


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
