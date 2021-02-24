def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            alphabet_occurrence_array[index] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))