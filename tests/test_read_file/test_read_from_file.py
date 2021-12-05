import pytest
from main import read_from_file

test_file_path_name = "tests/test_read_file/testfile.txt"


def create_test_data(test_data):
    with open(test_file_path_name, "w") as fd:
        fd.writelines(test_data)


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert test_data == read_from_file(test_file_path_name)