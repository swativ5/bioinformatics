'''
Code Challenge: Solve the Change Problem. The DPChange pseudocode is reproduced below for your convenience.
    Input: An integer money and an array Coins = (coin1, ..., coind).
    Output: The minimum number of coins with denominations Coins that changes money.

Sample Input:
40
50 25 20 10 5 1

Sample Output:
2

DPChange(money, Coins)
    MinNumCoins(0) ← 0
    for m ← 1 to money
        MinNumCoins(m) ← ∞
            for i ← 0 to |Coins| - 1
                if m ≥ coini
                    if MinNumCoins(m - coini) + 1 < MinNumCoins(m)
                        MinNumCoins(m) ← MinNumCoins(m - coini) + 1
    output MinNumCoins(money)
'''

def DPChange(money, Coins):
    MinNumCoins = [float('inf')] * (money + 1)
    MinNumCoins[0] = 0

    for m in range(1, money + 1):        
        for i in range(len(Coins)):
            if m >= Coins[i]:
                MinNumCoins[m] = min(MinNumCoins[m - Coins[i]] + 1, MinNumCoins[m])
        if m >= 13 and m <= 22:
            print(MinNumCoins[m], end=" ")
    return MinNumCoins[money]

if __name__ == "__main__":
    file_input = open("/home/swativ5/Downloads/dataset_30195_10.txt", "r")
    file_input_text = file_input.read()
#     file_input_text = '''40
# 50 25 20 10 5 1'''

    money, Coins = file_input_text.strip().split("\n")
    money = int(money)
    Coins = Coins.strip().split()
    Coins = [int(coin) for coin in Coins]
    
    f_output = DPChange(money, Coins)
    f = open("test.txt", "w")
    f.write(str(f_output))

    money = 22
    Coins = [5, 4, 1]
    DPChange(money, Coins)
    