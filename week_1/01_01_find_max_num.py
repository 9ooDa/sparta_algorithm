input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:  # python 의 for ~ else 문은 “for문에서 break가 발생하지 않았을 경우”의 동작을 else문에 적어주는 것이다.
            return max


result = find_max_num(input)
print(result)
