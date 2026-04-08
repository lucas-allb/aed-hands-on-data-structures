from src.my_array import MyArray


def linear_search(array: MyArray, target: int) -> int:
    
    for posicao in range(len(array)):
        if array[posicao] == target:
            return posicao
    return -1