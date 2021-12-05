from main import start_condition_interactive_procedure
import pytest

#((ana1 >= 40.1 and ana1 <= 60.1) and (ana2 > 60.1)) or ((ana3 > 0) or bin1 > bin2 < bin3)
data_test_start_condition_int_proc_good = [(10.1, 20.2, 30.4, 50, 60, 70),
                                           (42.1, 42.2, 70.4, 40, 30, 70),
                                           (67.1, 29.2, -3.4, 56, 6, 40),
                                           (82.1, 90.2, -38.4, 95, 60, 70)]


data_test_start_condition_int_proc_with_error = [("10.1", 20.2, 30.4, 50, 60, 70),
                                           (None, "42.2", 70.4, 40, 30, 70),
                                           (67.1, True, "-3.4", 56, 6, 40),
                                           (82.1, 90.2, False, "95", 60, 70)]

@pytest.mark.parametrize("ana1, ana2, ana3, bin1, bin2, bin3", data_test_start_condition_int_proc_good)
def test_start_condition_interactive_procedure_good(ana1, ana2, ana3, bin1, bin2, bin3):
    assert start_condition_interactive_procedure(ana1, ana2, ana3, bin1, bin2, bin3) == True

@pytest.mark.parametrize("ana1, ana2, ana3, bin1, bin2, bin3", data_test_start_condition_int_proc_with_error)
def test_start_condition_interacitve_procedure_with_error(ana1, ana2, ana3, bin1, bin2, bin3):
    with pytest.raises(TypeError):
        assert start_condition_interactive_procedure(ana1, ana2, ana3, bin1, bin2, bin3) == True

