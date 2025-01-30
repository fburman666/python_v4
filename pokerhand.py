from random import randint
def random_card():
    card_value = randint(2,14)
    colour = randint(1,4)
    if colour == 1:
        colour = "hjärter"
    elif colour == 2:
        colour = "spader"
    elif colour == 3:
        colour = "ruter"
    else:
        colour = "klöver"
    card = [colour, card_value]
    return card

def same_value(card1, card2):
    value1 = card1[1]
    value2 = card2[1]
    if value1 == value2:
        return True
    else:
        return False


print("1:")
print(random_card())

print("2:")
poker1 = random_card()
poker2 = random_card()
print(f"kort no 1 {poker1}")
print(f"kort no 2 {poker2}")
print(f"Har de samma valör? {same_value(poker1, poker2)}")

print("3:")

def same_value_5cards(card1, card2, card3, card4, card5):
    value1 = card1[1]
    value2 = card2[1]
    value3 = card3[1]
    value4 = card4[1]
    value5 = card5[1]
    if value1 == value2 or value1 == value3 or value1 == value4 or value1 == value5:
        return True
    elif value2 == value3 or value2 == value4 or value2 == value5:
        return True
    elif value3 == value4 or value3 == value5:
        return True
    elif value4 == value5:
        return True
    else:
        return False

def poker_hand(cards):
    print(f"Här är din pokerhand: {cards}" )
    if same_value_5cards(cards[0], cards[1], cards[2], cards[3], cards[4]):
        print("Du har minst ett par. Grattis!")
    else:
        print("Du har inget par. Bamnken tar dina pengar!")


poker1 = random_card()
poker2 = random_card()
poker3 = random_card()
poker4 = random_card()
poker5 = random_card()
hand = [poker1,poker2,poker3,poker4,poker5]
poker_hand(hand)