from byte_code.python_312.uabcs_parser import uabcs_parser  # type: ignore


############ Parser File Tests ############


def test_valid_file_extension():
    try:
        assert parser.parse_file("invalid_file.txt")  # Invalid extension
        return False
    except ValueError:
        return True


def test_file_not_found():
    try:
        assert parser.parse_file("non_existent_file.uabcs")  # File doesn't exist
        return False
    except FileNotFoundError:
        return True


def test_equal_column(filename):
    try:
        data = parser.parse_file(filename)
        entrylength = len(parser.get_column_names())
        for d in data:
            assert len(d) == entrylength
        return True
    except ValueError:
        return False


############## Records by field tests ##############


# Test for valid field_name
def test_invalid_field_name():
    # Invalid field name, should raise key error
    try:
        parser.get_records_by_field("NAME", "Alice")
        return False
    except KeyError:
        print("Test case passed, invalid field_name raised error")
        return True


def test_no_value_matches():
    actual = parser.get_records_by_field("NAME", "Frederick")
    expected = []
    assert (
        actual == expected
    ), "Test case failed, empty list not returned when no matches"
    print("Test case passed, empty list returned when no matches")
    return True


# Execution
if __name__ == "__main__":
    parser = uabcs_parser()
    parser.parse_file("student_grades.uabcs")
    parser.get_column_names()

    passed = [
        test_valid_file_extension(),
        test_file_not_found(),
        test_equal_column("student_grades.uabcs"),
        test_invalid_field_name(),
        test_no_value_matches(),
    ]

    print(f"\nUnit Testing uabcs_parser.parse_file and get_records_by_field")
    print(f"-----------------------------")
    print(f"Passed " + str(passed.count(True)) + " tests")
    print(f"Failed " + str(passed.count(False)) + " tests")
    print("")
