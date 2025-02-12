# Here’s a list of essential functionalities for your e-commerce system with brief descriptions:

# 1. register_user(data)
#       -Register a new user with name, email, and phone number.
# login_user(email, password)
#       -Authenticate user credentials and return an access token.
# get_user_profile(user_id)
#       -Retrieve user profile details.
# update_user_profile(user_id, data)
#       -Update user details like name, phone number, or email.
# list_categories()
#       -Fetch all available product categories.
# add_category(name)
#       -Add a new product category.
# list_products(category_id=None)
#       -Retrieve all products or filter by category.
# add_product(data)
#       -Add a new product with name, price, quantity, and category.
# update_product(product_id, data)
#       -Update product details like price, quantity, or name.
# delete_product(product_id)
#       -Remove a product from the catalog.
# add_to_cart(user_id, product_id, quantity)
#       -Add a product to the user’s cart.
# remove_from_cart(user_id, product_id)
#       -Remove a product from the user’s cart.
# view_cart(user_id)
#        -Display all items in the user’s cart.
# update_cart_item(user_id, product_id, quantity)
#        -Update the quantity of an item in the cart.
# checkout_cart(user_id)
#       -Convert cart items to an order and clear the cart.
# place_order(user_id, order_data)
#       -Create a new order with selected products.
# view_orders(user_id)
#       -Display all orders placed by the user.
# get_order_details(order_id)
#       -Retrieve specific order details, including products and total price.
# cancel_order(order_id)
#       -Cancel an order if it hasn’t been shipped.
# calculate_total_price(order_id)
#       -Calculate the total price of an order (fix the hybrid property).
# process_payment(order_id, payment_details)
#        Handle payment processing for an order.
# update_inventory(product_id, quantity)
#       Adjust product inventory after purchase.
# search_products(keyword)
#       Search for products by name or description.
# filter_products(price_range=None, category_id=None)
#       Filter products based on price range or category.
# generate_invoice(order_id)
#       Create an invoice for the completed order.
# send_order_confirmation(user_id, order_id)
#       Send confirmation email/message after order placement.
# track_order(order_id)
#       Track the current status of an order.
# add_product_review(user_id, product_id, review_data)
#       Allow users to submit reviews for purchased products.
# get_product_reviews(product_id)
#       Retrieve all reviews for a product.
# apply_discount(order_id, discount_code)
#       Apply discount codes to an order during checkout.
# admin_get_all_orders()
#       Admin functionality to view all user orders.
# admin_manage_users()
#       Admin functionality to manage user data.
# restock_product(product_id, quantity)
#       Add more stock to an existing product.
# This structure
