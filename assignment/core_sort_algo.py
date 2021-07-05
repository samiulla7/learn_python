# bubble sort
def bubble_sor(arr):
    n = len(arr)
    for iter_num in range(n-1,0,-1):
        for j in range(iter_num):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sor2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


inp_arr = [2,9,5,1,8,4,6]
bubble_sor2(inp_arr)
print(inp_arr)