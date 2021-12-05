import pytest

@pytest.fixture(autouse=True)
def clean_text_file():
    with open("tests/test_read_file/testfile.txt", "w") as fd:
        pass

