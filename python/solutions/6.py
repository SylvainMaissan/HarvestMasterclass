def calculate_cost(item_type, quantity, price):
    tax_rate = get_tax_rate(item_type)
    discount_rate = get_discount_rate(item_type)
    shipping_cost = get_shipping_cost(item_type, quantity)

    cost = quantity * price
    cost += cost * tax_rate
    cost -= cost * discount_rate
    cost += shipping_cost

    return cost


def get_tax_rate(type):
    if type == "food":
        return 0
    elif type == "clothing":
        return 0.1
    else:
        return 0.2


def get_discount_rate(type):
    if type == "food":
        return 0
    elif type == "clothing":
        return 0.1
    else:
        return 0.2


def get_shipping_cost(type, quantity):
    if type == "food":
        return 0
    elif type == "clothing":
        return 5.95
    else:
        return 9.95
