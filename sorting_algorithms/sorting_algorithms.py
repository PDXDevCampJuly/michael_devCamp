# Implementation of various sorting algorithms for lists
##########################

from sys import argv

filename = (argv[1])

# retrieve the char10.txt file
with open(filename, "r") as f:
  our_list = eval(f.read())


# python sorting algorithm
def python_sort(our_list):
    return sorted(our_list)


def list_swap(our_list, low, high):
    """
    Uses simultaneous assignment to swap it with the one we are moving.
    """
    our_list[low], our_list[high] = our_list[high], our_list[low]
    return our_list


def selection_sort(our_list):
    """
    Look through the list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """

    # find the smallest
    # for start in range(len(our_list)):
    #     mindex = start
    #     minimum = our_list[start]
    #     for index in range(start + 1, len(our_list)):
    #         if our_list[index] < minimum:
    #             mindex = index
    #             minimum = our_list[index]
    #     if mindex != start:
    #         list_swap(our_list, start, mindex)
    # return our_list

    # len of the list is len - 1 as you move to the right
    for lowest_item in range(len(our_list) - 1):
        first_item = lowest_item
        for i in range(lowest_item + 1, len(our_list)):
            if our_list[i] < our_list[first_item]:
                first_item = i

        list_swap(our_list, lowest_item, first_item)
    return our_list


def insertion_sort(our_list):
    """
    Insert (via swaps) the next element in the sorted list of the previous
    elements.
    """
    for index in range(1, len(our_list)):
        candidate = our_list[index]
        comparison_index = index - 1
        while index >= 0:
            if candidate < our_list[comparison_index]:
                list_swap(our_list, comparison_index, comparison_index + 1)
                comparison_index -= 1
            else:
                break
        return our_list


def merge_sort(our_list):
    """
    Our first recursive algorithm.
    """
    pass

print(selection_sort(our_list))

