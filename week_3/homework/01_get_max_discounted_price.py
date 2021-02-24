shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    total_price = 0
    index_difference = abs(len(prices) - len(coupons))
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    for i in range(len(coupons)):
        total_price += prices[i] * (1 - coupons[i] / 100)

    for length_diff in range(index_difference):
        if len(coupons) < len(prices):
            total_price += prices[len(coupons) + length_diff]

    return int(total_price)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
