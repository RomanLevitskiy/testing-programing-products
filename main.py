def start_condition_interactive_procedure(ana1, ana2, ana3, bin1, bin2, bin3):
    return ((ana1 >= 40.1 and ana1 <= 60.1) and (ana2 > 60.1)) or ((ana3 > 0) or bin1 > bin2 < bin3)


def read_from_file(filepath):
    with open(filepath, "r") as fd:
        return fd.readlines()

