# Updated pre-populated list of orders with 'Status' field
orders = [
    {'OrderID': 1, 'CustomerName': 'Alice', 'TotalAmount': 150, 'Status': 'completed'},
    {'OrderID': 2, 'CustomerName': 'Bob', 'TotalAmount': 90, 'Status': 'canceled'},
    {'OrderID': 3, 'CustomerName': 'Charlie', 'TotalAmount': 120, 'Status': 'completed'},
    {'OrderID': 4, 'CustomerName': 'Diana', 'TotalAmount': 80, 'Status': 'canceled'},
    {'OrderID': 5, 'CustomerName': 'Evan', 'TotalAmount': 200, 'Status': 'completed'}
]

# Function to select orders with TotalAmount > 100 and merge canceled orders
def process_orders(orders):
    high_value_orders = [order for order in orders if order['TotalAmount'] > 100]
    orders_canceled = [order for order in orders if order['Status'] == 'canceled']
    return high_value_orders, orders_canceled

# Using the function to get desired orders
high_value_orders, orders_canceled = process_orders(orders)

# Displaying the selected orders and canceled orders
print("Orders with TotalAmount > 100:")
for order in high_value_orders:
    print(order)

print("\nCanceled Orders:")
for order in orders_canceled:
    print(order)



"""
re-write the order selector as sql
"""