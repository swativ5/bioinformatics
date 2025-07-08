'''
RecursiveChange(money, Coins)
    if money = 0
        return 0
    MinNumCoins ← ∞
    for i ← 0 to |Coins| - 1
        if money ≥ coini
            NumCoins ← RecursiveChange(money − coini, Coins)
            if NumCoins + 1 < MinNumCoins
                MinNumCoins ← NumCoins + 1
    return MinNumCoins
'''

def RecursiveChange(money, Coins):
    if money == 0:
        return 0
    if money < 0:
        return float('inf')
    
    MinNumCoins = float('inf')
    
    for i in range(0, len(Coins)):
        if money >= Coins[i]:
            NumCoins = RecursiveChange(money - Coins[i], Coins)

            if NumCoins != float('inf') and NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1

    return MinNumCoins

print(RecursiveChange(76, [5, 4, 1]))