def change_list(arr: list[int], num: int):
    for i in range(len(arr)):
        if arr[i] > num:
            arr[i] = 0

arr = list(map(int, str(input("List of space separated whole numbers: ")).split()))
num = int(input("Numer: "))
change_list(arr, num)
print(arr)
