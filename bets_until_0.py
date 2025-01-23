import random

money = int(input('How much will you bet?: '))

coin_toss = (['Heads', 'Tails'])
bets = 0
while money > 0:

    if coin_toss == 'Heads':
        money += random.choice([-1, 1])
        bets += 1
    else:
        money -= random.choice([-1, 1])
        bets += 1
    


print(bets)