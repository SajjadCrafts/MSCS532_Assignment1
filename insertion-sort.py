
def insertion_sort_decreasing(arr):
    """
    Sort an array in monotonically decreasing order using Insertion Sort.
    
    Args:
        arr (list): The array to be sorted
        
    Returns:
        list: The sorted array in decreasing order
    """
    # Start from the second element (index 1) to the end of the array
    for i in range(1, len(arr)):
        # The key is the current element we want to insert in correct position
        key = arr[i]
        
        # Start comparing with the element just before the current one
        j = i - 1
        
        # Move elements of arr[0..i-1] that are smaller than key
        # to one position ahead of their current position
        # We're sorting in decreasing order, so we move elements that are < key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the key in its correct position
        arr[j + 1] = key
    
    return arr

