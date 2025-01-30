import random

#version 1
def greater_than_21():
    iterations = 0
    sum_of_numbers = 0
    while sum_of_numbers < 21:
        iterations += 1
        sum_of_numbers = sum_of_numbers + iterations
    return  iterations + 1

#version 2
def random_card():
    card = random.randint(1,13)
    return card

#beräknar kortsumman i en hand. 10 för knekt, dam, kung
def total_hand(hand_of_cards):
    cardsum = 0
    for card in hand_of_cards:
        if card >= 10:
            card = 10
        cardsum = cardsum + card
    return cardsum


def play_21():
    dealer_hand = [random_card(), random_card()]
    player_hand = [random_card(), random_card()]

    while 1:
        print (f"Du har {player_hand}. Dealern har {dealer_hand}.")
        new_card = input("Vill du ha ett kort till? (ja/nej)")
        if new_card == "ja":
            player_hand.append(random_card())
            if total_hand(player_hand) > 21:
                print(f"Du blev tjock: {total_hand(player_hand)}")
                break
            else:
                print(f"Du har nu: {player_hand}")

        else:
            while total_hand(dealer_hand) < 17:
                dealer_hand.append(random_card())
            break
    player_sum = total_hand(player_hand)
    dealer_sum = total_hand(dealer_hand)
    if player_sum > dealer_sum:
        print("grattis du vann")
    else:
        print("Banken tar dina pengar!")
    print(f"Du hade: {player_hand}")
    print(f"Dealern hade: {dealer_hand}")


#Version 1
print(greater_than_21())

#version 2
print (random_card())

#version 3
play_21()