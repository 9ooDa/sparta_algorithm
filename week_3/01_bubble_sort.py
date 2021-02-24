input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)

    for i in range(n - 1): # 마지막 element는 비교하지 않아도 돼서 빼주는
        for j in range(n - i - 1): # 버블의 갯수
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
