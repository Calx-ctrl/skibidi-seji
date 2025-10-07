# Lab2c.py
# 1. String Manipulation
phone_input = input("Enter phone number: ")

cleaned = phone_input.replace(" ", "").replace("-", "")

formatted_phone = f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
print("Formatted Phone Number:", formatted_phone)


# 2. Formatting
item = "Book"
price = 15.99
quantity = 2
total = price * quantity

print(f"\n{quantity} x {item} @ ${price:.2f} ea. = ${total:.2f}")


# 3. Validation & Search 
def is_valid_username(username):
    """Checks if the username is alphanumeric and 5–12 characters long."""
    return username.isalnum() and 5 <= len(username) <= 12

username_input = input("\nEnter a username to validate: ")
print("Valid username?" , is_valid_username(username_input))


# 4. Credit Card Masking
def mask_credit_card(card_number):
    return "*" * (len(card_number) - 4) + card_number[-4:]


# Example test 
card_input = input("\nEnter credit card number: ")
print("Masked Credit Card:", mask_credit_card(card_input))
