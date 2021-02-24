input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    count = 0
    division_occurrence_arr = [0] * 19


    for num in range(2, number):
        for i in range(1, num+1):
            if num % i == 0:
                division_occurrence_arr[num-1] += 1

    for occurrence in division_occurrence_arr:
        if occurrence == 2:
            count += 1

    prime_num_arr = [0] * count
    i = 0
    for index in range(len(division_occurrence_arr)):
        if division_occurrence_arr[index] == 2:
            prime_num_arr[i] = index + 1
            i += 1
        if i == 8:
            break

    return prime_num_arr


result = find_prime_list_under_number(input)
print(result)