def calculate_cost(type, quantity, price, tax_rate, discount_rate, shipping_cost):
    cost = quantity * price
    cost += cost * tax_rate
    cost -= cost * discount_rate
    cost += shipping_cost
    return cost
