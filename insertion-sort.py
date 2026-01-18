
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

def test_insertion_sort_decreasing():
    """
    Test function to demonstrate the insertion sort algorithm
    with various test cases.
    """
    print("Testing Insertion Sort (Decreasing Order)")
    print("=" * 50)
    
    # Test Case 1: Random array
    test_array1 = [5, 2, 4, 6, 1, 3]
    print(f"Original array: {test_array1}")
    sorted_array1 = insertion_sort_decreasing(test_array1.copy())
    print(f"Sorted (decreasing): {sorted_array1}")
    print()
    
    # Test Case 2: Already sorted in decreasing order
    test_array2 = [9, 7, 5, 3, 1]
    print(f"Original array: {test_array2}")
    sorted_array2 = insertion_sort_decreasing(test_array2.copy())
    print(f"Sorted (decreasing): {sorted_array2}")
    print()
    
    # Test Case 3: Already sorted in increasing order (opposite)
    test_array3 = [1, 2, 3, 4, 5]
    print(f"Original array: {test_array3}")
    sorted_array3 = insertion_sort_decreasing(test_array3.copy())
    print(f"Sorted (decreasing): {sorted_array3}")
    print()
    
    # Test Case 4: Array with duplicate values
    test_array4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"Original array: {test_array4}")
    sorted_array4 = insertion_sort_decreasing(test_array4.copy())
    print(f"Sorted (decreasing): {sorted_array4}")
    print()
    
    # Test Case 5: Single element array
    test_array5 = [42]
    print(f"Original array: {test_array5}")
    sorted_array5 = insertion_sort_decreasing(test_array5.copy())
    print(f"Sorted (decreasing): {sorted_array5}")
    print()
    
    # Test Case 6: Empty array
    test_array6 = []
    print(f"Original array: {test_array6}")
    sorted_array6 = insertion_sort_decreasing(test_array6.copy())
    print(f"Sorted (decreasing): {sorted_array6}")
    print()
    
    print("=" * 50)
    print("All tests completed!")


