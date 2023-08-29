from blackjack import PlayingCard


def run_blackjack():
    busts = 0
    total = 0

    while True:
        card1 = PlayingCard(random.choice(ranks), random.choice(suits))
        card2 = PlayingCard(random.choice(ranks), random.choice(suits))
        card3 = PlayingCard(random.choice(ranks), random.choice(suits))

        black_total = card1.blackjack_value() + card2.blackjack_value() + card3.blackjack_value()

        if black_total > 21:
            busts += 1
        total += 1
        yield busts / total

if __name__ == "__main__":
    sim = run_blackjack()
    for i in range(1000):
        next(sim)

    print(next(sim))
