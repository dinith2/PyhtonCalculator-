def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than root
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        max_heapify(arr, n, largest)

def min_heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is smaller than root
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    # Check if right child exists and is smaller than root
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    # Change root if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        min_heapify(arr, n, smallest)

# Example usage:
arr_max_heap = [4
