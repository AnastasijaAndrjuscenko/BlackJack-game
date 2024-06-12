import random
# import os

game = "y"
while game == "y":
    # os.system('clear')
    import art

    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_cards = []
    user_cards = []


    def counting_blackjack():
        comp = 0
        user = 0
        # TYPO: checking for blackjack and for ace, and for being over 21
        for a in computer_cards:
            comp += a
        for b in user_cards:
            user += b
        if comp == 21:
            return print("Computer has blackjack")
        if user == 21:
            return print("You have blackjack.You win.")
        if comp > 21:
            for ace_comp in computer_cards:
                if ace_comp == 11:
                    computer_cards[computer_cards.index(ace_comp)] = 1
                    comp = comp - 10

        if user > 21:
            for num in user_cards:
                if num == 11:
                    user_cards[user_cards.index(num)] = 1
                    user = user - 10
            if user > 21:
                return print(f"You have {user} and its over 21. You lose")
        return "not"


    for i in range(2):
        computer_cards.append(cards[random.randint(0, len(cards) - 1)])
        user_cards.append(cards[random.randint(0, len(cards) - 1)])

    cont = counting_blackjack()
    if cont == "not":
        sum_cards = 0
        for i in user_cards:
            sum_cards += i
        print(f"You have {user_cards}. Your total is {sum_cards}.")
        print(f"Computer first cards is {computer_cards[0]}")
        answer = input("Print 'y' to get another card, or 'n' to stop. ")
        while cont == "not":
            if answer == "y":
                user_cards.append(cards[random.randint(0, len(cards) - 1)])
                cont = counting_blackjack()
                if cont == "not":
                    answer = input(f"You have {user_cards}. Print 'y' to get another card, or 'n' to stop. ")
            if answer == "n":
                summary = 0
                while summary < 17:
                    summary = 0
                    for i in computer_cards:
                        summary += i
                    if summary < 17:
                        computer_cards.append(cards[random.randint(0, len(cards) - 1)])

                counting_blackjack()
                break
    sum1 = 0
    sum2 = 0
    for i in computer_cards:
        sum1 += i
    if sum1 < 21:
        for i in user_cards:
            sum2 += i
        if sum2 < 21:
            if sum1 > sum2:
                print(f"Computer has {sum1}. Computer wins")
            if sum1 < sum2:
                print(f"You have {sum2}. You win")
            if sum1 == sum2:
                print("Its a draw")

    game = input("Do you want to play again? Print 'y' for yes and 'n' for no. ")
