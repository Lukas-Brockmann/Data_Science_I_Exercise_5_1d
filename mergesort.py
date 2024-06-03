import matplotlib.pyplot as plt

# Split a list into two halfs (first up to one element longer)
def _split(input_list):
        mid = len(input_list) // 2
        return input_list[:mid], input_list[mid:]

# Merge two lists into one ascendingly sorted list
def _merge(list_a, list_b):
        result = []
        while len(list_a) > 0 and len(list_b) > 0: # While both lists are not empty
            if list_a[0] < list_b[0]:   
                result.append(list_a.pop(0))
            else:
                result.append(list_b.pop(0))

        # Append the remaining elements of the non-empty list
        result.extend(list_a)
        result.extend(list_b)

        return result

# Recursively sort input_list using merge sort algorithm
def sort(input_list):
    if len(input_list) <= 1: # Base case
        return input_list
    else:   # Recursive case, split the list and merge the sorted halves
        list_a, list_b = _split(input_list)
        return _merge(sort(list_a), sort(list_b))

# Plot the input_list before and after sorting, use demo=True for an example list
def plot(input_list=[], demo=False):
    if demo:
        input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    x = range(len(input_list))
    plt.title("List before sorting")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.bar(x, input_list)
    plt.show()
    
    sorted_list = sort(input_list)

    plt.title("List after sorting")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.bar(x, sorted_list)
    plt.show()

# Just some addage to create a conflict in the repository