unsorted_list = [20, 12, 5, 18, 20456, 25,
                 730, 1532, 45, -46, 0, 0, 8, 8, 13, 58]


def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item - z):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
        print(mylist)
    return mylist


print(f"\nUnsorted list: \n{unsorted_list}\n")
new_list = bubble_sort(unsorted_list).copy()
print(f"New List: \n{new_list}\n")
