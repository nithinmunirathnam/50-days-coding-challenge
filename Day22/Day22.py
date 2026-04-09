order_id = "ORD12345"  # string
customer_name = "Rahul"  # string
product_price = 799.99  # float
quantity = 3  # int
discount = 0.10  # float
is_member = True  # boolean

# print("Data types: ")
# print("order_id: ",type(order_id))
# print("customer_name: ",type(customer_name))
# print("customer_name:", type(customer_name))
# print("product_price:", type(product_price))
# print("quantity:", type(quantity))
# print("discount:", type(discount))
# print("is_member:", type(is_member))

total_price = product_price * quantity
print(total_price)

discount_amount = total_price * discount
price_after_discount = total_price - discount_amount
print(price_after_discount)

gst = price_after_discount * 0.18
final_amount = price_after_discount + gst
print(final_amount)

print("\n----- Final Bill -----")
print(f"Order ID: {order_id}")
print(f"Customer: {customer_name}")
print(f"Total Price: {total_price:.2f}")
print(f"Discount Applied: {'Yes' if is_member else 'No'}")
print(f"Final Amount (including GST): {final_amount:.2f}")
