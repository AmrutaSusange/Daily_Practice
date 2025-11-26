def arr_sum(arr):
    if not arr:
        return 0
    return arr[0] + arr_sum(arr[1:])

if __name__ == "__main__":
    print(arr_sum([1,2,3,4,5]))