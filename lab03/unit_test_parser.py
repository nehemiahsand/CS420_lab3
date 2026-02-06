# File to test
def parse_file(self, filename):
    """
    Parses a .uabcs file and returns list of record dictionaries.
    Raises ValueError for invalid file format or extension.
    Raises FileNotFoundError if file doesn't exist.
    """
    pass


############ Unit Tests ############


def test_parse_file_invalid_extension(filename):
    if not filename.endswith(".uabcs"):
        raise ValueError("Invalid file extension. Expected '.uabcs'")


############# Example usage of the test #############

print(test_parse_file_invalid_extension("grades.uabcs"))
