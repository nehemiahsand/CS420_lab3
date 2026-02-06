from fileinput import filename
from byte_code.python_312.uabcs_parser import uabcs_parser


# File to test
def parse_file(self, filename):
    """
    Parses a .uabcs file and returns list of record dictionaries.
    Raises ValueError for invalid file format or extension.
    Raises FileNotFoundError if file doesn't exist.
    """
    pass


############ Unit Tests ############


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


def test_unequal_column(filename):
    try:
        entrylength = len(parser.get_column_names())
        data = parser.parse_file(filename)
        for d in data:
            assert len(d) == entrylength
        return True
    except ValueError:
        return False


############# Example usage of the test #############

# Initialize a parser instance
parser = uabcs_parser()
