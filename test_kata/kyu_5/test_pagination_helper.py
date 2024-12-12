import pytest

from kyu_5.pagination_helper import PaginationHelper


test_data = ((PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4), 6, 2, {'input': 0, 'res': 4}, {'input': 5, 'res': 1}),
             (PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4), 6, 2, {'input': 1, 'res': 2}, {'input': 2, 'res': 0}),
             (PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4), 6, 2, {'input': 2, 'res': -1}, {'input': 20, 'res': -1}),
             (PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4), 6, 2, {'input': -7, 'res': -1}, {'input': -10, 'res': -1}),
             (PaginationHelper([], 18), 0, 0, {'input': 0, 'res': -1}, {'input': 5, 'res': -1}),
             (PaginationHelper([], 18), 0, 0, {'input': 1, 'res': -1}, {'input': 2, 'res': -1}),
             (PaginationHelper([], 18), 0, 0, {'input': -3, 'res': -1}, {'input': 20, 'res': -1}),
             (PaginationHelper([], 18), 0, 0, {'input': 9, 'res': -1}, {'input': -10, 'res': -1}),)


@pytest.mark.parametrize('create_pagin_helper, item_count, page_count, page_item_count, page_index', test_data)
def test_normal_paginator_helper(create_pagin_helper, item_count, page_count, page_item_count, page_index):
    assert create_pagin_helper.item_count() == item_count
    assert create_pagin_helper.page_count() == page_count
    assert create_pagin_helper.page_item_count(page_item_count['input']) == page_item_count['res']
    assert create_pagin_helper.page_index(page_index['input']) == page_index['res']
