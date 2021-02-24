shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()
    orders.sort()

    count = 0

    for order in orders:

        current_min = 0
        current_max = len(menus) - 1
        current_guess = (current_max + current_min) // 2

        while current_min <= current_max:
            if menus[current_guess] == order:
                count += 1
                break
            elif menus[current_guess] > order:
                current_max = current_guess - 1
            else:
                current_min = current_guess + 1
            current_guess = (current_max + current_min) // 2

    if count == len(orders):
        return True
    elif count < len(orders):
        return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)