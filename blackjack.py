"""
Blackjack

Version 1.0.0
"""
import os
import time
import random
import common_utils

cards = {}


def print_header():
    os.system("cls")
    header = f"Blackjack"
    common_utils.print_header(header)


def decks(n):
    rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit = ["Spade", "Heart", "Diamond", "Club"]
    deck = [i + " " + j for i in suit for j in rank]
    decks = ["D" + str(i) + "-" + j for i in range(1, n + 1) for j in deck]
    return decks


def value_of_card(card):
    face = card.split(" ")[1]
    if face == "A":
        return 11
    elif face in ("10", "J", "Q", "K"):
        return 10
    else:
        return int(face)


def generate_dict_cards(n):
    for i in decks(n):
        cards[i] = value_of_card(i)


def count_of_decks():
    checkpoint = True
    while checkpoint:
        try:
            count_of_decks = int(input("How many decks? (1-10) "))
            if count_of_decks > 0 and count_of_decks < 11:
                checkpoint = False
            else:
                print("Invalid input!")
                time.sleep(2)
        except Exception as e:
            print("Invalid input!")
            time.sleep(2)
            print_header()
    return count_of_decks


def pick_a_card():
    card, value = random.choice(list(cards.items()))
    cards.pop(card)
    return card[3:], value


def main():
    print_header()
    generate_dict_cards(count_of_decks())

    dealer_cards = []
    dealer_count = 0
    dealer_A_flag = False
    dealer_second_card = False
    player_cards = []
    player_count = 0
    player_A_flag = False

    print_header()
    # Auto Dealer's turn
    card, value = pick_a_card()
    dealer_cards.append(card)
    dealer_count += value
    print(f"Dealer: {dealer_cards} Count: {dealer_count}")

    # Auto Player's turn
    card, value = pick_a_card()
    player_cards.append(card)
    player_count += value
    print(f"Player: {player_cards} Count: {player_count}")

    # Players turn
    checkpoint = True
    while checkpoint:
        if player_count >= 21 or (input("Deal? (y/n)").lower() == "n"):
            checkpoint = False
        else:
            card, value = pick_a_card()
            if value == 11:
                player_A_flag = True
            player_cards.append(card)
            player_count += value
            if player_A_flag and player_count > 21:
                player_count -= 10
                player_A_flag = False
            print_header()
            print(f"Dealer: {dealer_cards} Count: {dealer_count}")
            print(f"Player: {player_cards} Count: {player_count}")

    # Dealers turn
    checkpoint = True
    while checkpoint:
        if dealer_count > 16 or (dealer_second_card and player_count > 21):
            checkpoint = False
        else:
            dealer_second_card = True
            card, value = pick_a_card()
            if value == 11:
                dealer_A_flag = True
            dealer_cards.append(card)
            dealer_count += value
            if dealer_A_flag and dealer_count > 21:
                dealer_count -= 10
                dealer_A_flag = False
            print_header()
            print(f"Dealer: {dealer_cards} Count: {dealer_count}")
            print(f"Player: {player_cards} Count: {player_count}")

    if player_count == 21:
        print("Blackjack!")
    elif player_count > 21:
        print("Game lost!")
    elif dealer_count > 21:
        print("Game won!")
    elif dealer_count == player_count:
        print("Game draw!")
    elif player_count > dealer_count:
        print("Game won!")
    else:
        print("Game lost!")


if __name__ == "__main__":
    main()
