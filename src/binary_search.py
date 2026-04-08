from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    
    menor = 0
    maior = len(array) -1


    while menor <= maior:
        mid = (menor + maior) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            menor = mid + 1
        else:
            maior = mid -1
    return -1