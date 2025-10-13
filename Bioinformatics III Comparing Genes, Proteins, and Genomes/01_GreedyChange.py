'''
GreedyChange(money)
    change ← empty collection of coins)
    while money > 0
        coin ← largest denomination that is less than or equal to money
        add a coin with denomination coin to the collection of coins change
        money ← money − coin
    return change
'''

def GreedyChange(money, coins):
    coins = sorted(coins, reverse = True)
    change = {}

    coin = 0
    while money > 0 and coin < len(coins):
        if coins[coin] > money:
            coin += 1
            continue

        change[coins[coin]] = change.get(coins[coin], 0) + 1
        money -= coins[coin]

    return change


print(GreedyChange(22, [25, 10, 5, 1]))
