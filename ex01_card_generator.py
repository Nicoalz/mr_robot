import random
import string

card_type = input("Visa or Mastercard ?").lower()

while card_type != "visa" and card_type != "mastercard":
    card_type = input("Please choose a card by typing Visa or Mastercard : ").lower()

def card_generator(card_type):

    card =""
    if card_type == "visa":
        card = "4"
    if card_type == "mastercard":
        card = "5"

    for i in range(15):
        card += ''.join(random.choice(string.digits))

    #Luhn check:
    total = 0
    card = card[::-1]
    for i in range(0, len(card)):
        if i % 2 != 0:
            result = int(card[i]) * 2
            if result > 9:
                result -= 9
            total += result
        else:
            total += int(card[i])

    if total % 10 == 0:
        card = card[::-1]
        return f"Here is your {card_type} card : {card}"
    return card_generator(card_type)

print(card_generator(card_type))

