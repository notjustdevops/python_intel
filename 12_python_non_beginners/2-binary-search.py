
def binary_search(sorted_list, search, start, stop):
    if start > stop:
        return False
    else:
        middle_index = (start + stop) // 2
        if search == sorted_list[middle_index]:
            return middle_index
        elif search < sorted_list[middle_index]:
            return binary_search(sorted_list, search, start, middle_index - 1)
        else:
            return binary_search(sorted_list, search, middle_index + 1, stop)


sorted_list = [10, 12, 15, 18, 20, 25, 30, 32, 45, 46, 78, 123, 1458]
search = 25
start = 0
stop = len(sorted_list)


x = binary_search(sorted_list, search, start, stop)

if not x:
    print(f"Sorry. Item {search} NOT Found.")
else:
    print(f"Success! Item {search} found at Index {x}.")
