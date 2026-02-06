from byte_code.python_312.uabcs_parser import uabcs_parser  # type: ignore


# Function to test
def get_records_by_field(self, field_name, value):
    """Returns all records where specified field equals value"""
    pass


# Access Data
test_parser = uabcs_parser()
test_parser.parse_file("student_grades.uabcs")
test_parser.get_column_names


# Test for valid field_name
def test_invalid_field_name():
    # Invalid field name, should raise key error
    try:
        test_parser.get_records_by_field("Nickname", "Alice")
        assert False, "Test case failed, invalid field_name accepted."
        return False
    except KeyError:
        print("Test case passed, invalid field_name raised error")
        return True


def test_no_value_matches():
    actual = test_parser.get_records_by_field("NAME", "Frederick")
    expected = []
    assert (
        actual == expected
    ), "Test case failed, empty list not returned when no matches"
    print("Test case passed, empty list returned when no matches")
    return True


# lets see if it works
test_invalid_field_name()
test_no_value_matches()
