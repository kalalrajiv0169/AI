#11
    import random

def toss_coin():
    return "heads" if random.choice([0,1]) == 0 else "Tails"

print("Toss Result:", toss_coin())

