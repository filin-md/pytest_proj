from utils import arrs


def test_get(new_list):
    assert arrs.get(new_list, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(new_list):
    assert arrs.my_slice(new_list, 1, 3) == [2, 3]
    assert arrs.my_slice(new_list, 1) == [2, 3, 4]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(new_list, -1) == [4]
    assert arrs.my_slice(new_list, -10) == [1, 2, 3, 4]
