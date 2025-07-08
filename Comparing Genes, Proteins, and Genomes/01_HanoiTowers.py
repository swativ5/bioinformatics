'''
HanoiTowers(n, startPeg, destinationPeg)
    if n = 1
        Move top disk from startPeg to destinationPeg
        return
    transitPeg = 6 − startPeg − destinationPeg
    HanoiTowers(n − 1, startPeg, transitPeg)
    Move top disk from startPeg to destinationPeg
    HanoiTowers(n − 1, transitPeg, destinationPeg)
    return
'''

def HanoiTowers(n, startPeg, destinationPeg, order):
    if n == 1:
        order.append(startPeg + "->" + destinationPeg)
    
    transitPeg = 6 − startPeg − destinationPeg
    pass