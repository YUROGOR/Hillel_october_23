from hw_lesson_7 import sort_list_asc
from hw_lesson_7 import sort_list_desc
from hw_lesson_7 import sort_list_alpha


def test_sort_number_by_asc():
    list_number = [34, 456, 11, -100, 77, 888, -35, 1031]
    assert sort_list_asc(list_number) == [-100, -35, 11, 34, 77, 456, 888, 1031]


def test_sort_number_by_desc():
    list_number = [34, 456, 11, -100, 77, 888, -35, 1031]
    assert sort_list_desc(list_number) == [1031, 888, 456, 77, 34, 11, -35, -100]


def test_sort_by_sum_alfa():
    list_word = ['груша', 'яблуко', 'диня', 'слива', 'апельсин']
    assert sort_list_alpha(list_word) == ['диня', 'груша', 'слива', 'яблуко', 'апельсин']
