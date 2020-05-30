
# Payment Choices
# ------------------------------
PAYMENT_BIZUM = "BIZUM"
PAYMENT_TRANSFER = "TRANSFER"
PAYMENT_CASH = "CASH"
PAYMENT_CARD = "CARD"
PAYMENT_WEB = "WEB"

PAYMENT_TYPES_CHOICE = [
    (PAYMENT_BIZUM, 'Bizum'),
    (PAYMENT_TRANSFER, 'Transferencia'),
    (PAYMENT_CASH, 'Efectivo'),
    (PAYMENT_CARD, 'Tarjeta'),
    (PAYMENT_WEB, 'Web'),
]

# Shop Choices
# ------------------------------
SHOP_FRUIT = "FRUIT"
SHOP_BAKERY = "BAKERY"
SHOP_BUTCHER = "BUTCHER"
SHOP_FISH = "FISH"

SHOP_TYPES_CHOICES = [
    (SHOP_FRUIT, 'Frutería'),
    (SHOP_BAKERY, 'Panadería'),
    (SHOP_BUTCHER, 'Carnicería'),
    (SHOP_FISH, 'Pescadería'),
]
