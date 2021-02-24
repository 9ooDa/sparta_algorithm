top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    received_top_order = [0] * len(heights)
    while heights:
        height = heights.pop() # popping out the last element
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > height:
                received_top_order[len(heights)] = i + 1
                break
    return received_top_order


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!