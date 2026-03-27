# arr=[1, 3, -1, -3, 5, 3, 6, 7], k=3
#output = [3, 3, 5, 5, 6, 7]


def slid_window(arr, k):

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum    
    






print(slid_window([1, 3, -1, -3, 5, 3, 6, 7], k=3))