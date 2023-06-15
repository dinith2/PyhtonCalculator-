import random


symbols = ["Cow", "Rabbit", "Duck", "Crab", "Pig", "Turkey", "seven"]

payouts = {
    ("Cow", "Cow", "Cow"): 50,
    ("Rabbit", "Rabbit", "Rabbit"): 20,
    ("Duck", "Duck", "Duck"): 20,
    ("plum", "plum", "plum"): 20,
    ("Crab", "Crab", "Crab"): 10,
    ("Turkey", "Turkey", "Turkey"): 5,
    ("seven", "seven", "seven"): 100,
    ("seven", "seven", "*"): 10,
    ("*", "*", "*"): 2
}

def spin():
    return [random.choice(symbols) for _ in range(3)]

def get_payout(symbols):
    for combo, payout in payouts.items():
        if symbols == combo:
            return payout
    return 0

def play():
        coin=0
        if(coin<5):
            input("Press enter to spin the slot machine...")
            symbols = spin()
            payout = get_payout(symbols)
            print(f"{' '.join(symbols)} - Payout: {payout}\n")

play()