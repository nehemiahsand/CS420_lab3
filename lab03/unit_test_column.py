from byte_code.python_312.uabcs_parser import uabcs_parser  # type: ignore

# function to test
def get_column_names(self):
    """Returns list of column names from the parsed file"""
    pass

# test cases
parser = uabcs_parser()
parser.parse_file("student_grades.uabcs")

def check_type():
    try:
        output = parser.get_column_names()
        assert isinstance(output, list)
        return True
    except AssertionError:
        return False

def check_output():
    try:
        expected = ['NAME', 'SUBJECT', 'GRADE', 'PASS', 'POINTS']
        actual = parser.get_column_names()
        assert expected == actual
        return True
    except AssertionError:
        return False

def check_internal_state():
    try:
        output = parser.get_column_names()
        output.append("NEW_COLUMN")
        assert output != parser.get_column_names()
        return True
    except Exception:
        return False


#checking test cases
def main():
    passed = [check_type(), check_output(), check_internal_state()]
    print(f"\nUnit Testing uabcs_parser.get_column_names()")
    print(f"-----------------------------")
    print(f"Passed " + str(passed.count(True)) + " tests")
    print(f"Failed " + str(passed.count(False)) + " tests")
    print("")

if __name__ == "__main__":
    main()