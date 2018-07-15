if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    m = max(arr)
    arr.remove(max(arr))
    for f in arr:
        if m == max(arr):
            arr.remove(max(arr))
        
    print(max(arr))
        
