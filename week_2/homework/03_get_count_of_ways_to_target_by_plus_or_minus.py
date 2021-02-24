numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    count = 0
    result = 0
    target_index = 0

    while target_index < len(array):
        result = 0
        for n in range(len(array)):
            if target_index == n:
                result -= array[target_index]
            else:
                result += array[n]

        if result == target:
            count += 1

        target_index += 1

    return count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!