from strategy import Order, ShippingCost
from strategy import FedExStrategy, PostalStrategy, UpsStrategy


order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

order = Order()
strategy = UpsStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

print('Tests passed')
