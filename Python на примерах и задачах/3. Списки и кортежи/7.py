def find_max(arr):
    result = []
    max_value = max(arr)
    max_value_index = arr.index(max(arr))
    result.append(max_value)
    result.append(max_value_index)
    return result

