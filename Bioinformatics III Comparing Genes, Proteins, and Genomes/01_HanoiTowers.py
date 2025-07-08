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

def HanoiTowers(n, startPeg, destinationPeg):
    order = []
    
    def solve(n, start, dest, order):
        if n == 1:
            order.append(f"{start}->{dest}")
        else:
            transit = 6 - start - dest
            solve(n - 1, start, transit, order)
            order.append(f"{start}->{dest}")
            solve(n - 1, transit, dest, order)
    
    solve(n, startPeg, destinationPeg, order)
    return order

print(HanoiTowers(3, 1, 3))