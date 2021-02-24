s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    open_parenthesis = 0
    close_parenthesis = 0

    for parenthesis in string:
        if parenthesis == '(':
            open_parenthesis += 1
        else:
            close_parenthesis += 1

    if open_parenthesis == close_parenthesis:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!