# For this exercise you will be strengthening your page-fu mastery.
# You will complete the PaginationHelper class, which is a utility
# class helpful for querying paging information related to an array.
#
# The class is designed to take in an array of values and an integer
# indicating how many items will be allowed per each page. The types
# of values contained within the collection/array are not relevant.

class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.__collection = collection
        self.__items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.__collection)

    # returns the number of pages
    def page_count(self):
        pages = len(self.__collection) // self.__items_per_page
        return pages + 1 if len(self.__collection) % self.__items_per_page != 0 else pages

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        start_index = page_index * self.__items_per_page
        stop_index = start_index + self.__items_per_page
        item_count = len(self.__collection[start_index:stop_index])
        return -1 if item_count == 0 or page_index < 0 else item_count

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        return -1 if len(self.__collection) <= item_index or item_index < 0 else item_index // self.__items_per_page
