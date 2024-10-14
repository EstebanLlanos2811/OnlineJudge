from heapq import heappush, heappop
from sys import stdin

def stock(ask, bid, sPr):
    if (len(ask) != 0 and len(bid) != 0):
        if abs(bid[0][0]) >= ask[0][0]:
            if bid[0][1] == ask[0][1]:
                heappop(bid)
                sPr.append(ask[0][0])
                heappop(ask)
                return ask, bid, sPr
            elif bid[0][1] > ask[0][1]:
                bid[0][1] = bid[0][1] - ask[0][1]
                sPr.append(ask[0][0])
                heappop(ask)
                return stock(ask, bid, sPr)
            elif bid[0][1] < ask[0][1]:
                ask[0][1] = ask[0][1] - bid[0][1]
                heappop(bid)
                sPr.append(ask[0][0])
                return stock(ask, bid, sPr)
    return ask, bid, sPr

def imp(ask, bid, sPr):
    v = "-"
    if len(ask) == 0 and len(bid) != 0 and len(sPr) != 0:
        bidP = abs(bid[0][0])
        sPrP = sPr[-1]
        print(v, bidP, sPrP)
    elif len(ask) == 0 and len(bid) == 0 and len(sPr) != 0:
        sPrP = sPr[-1]
        print(v, v, sPrP)
    elif len(ask) != 0 and len(bid) == 0 and len(sPr) != 0:
        askP = ask[0][0]
        sPrP = sPr[-1]
        print(askP, v, sPrP)
    elif len(ask) == 0 and len(bid) != 0 and len(sPr) == 0:
        bidP = abs(bid[0][0])
        print(v, bidP, v)
    elif len(ask) != 0 and len(bid) == 0 and len(sPr) == 0:
        askP = ask[0][0]
        print(askP, v, v)
    elif len(ask) != 0 and len(bid) != 0 and len(sPr) == 0:
        askP = ask[0][0]
        bidP = abs(bid[0][0])
        print(askP, bidP, v)
    elif len(ask) != 0 and len(bid) != 0 and len(sPr) != 0:
        askP = ask[0][0]
        bidP = abs(bid[0][0])
        sPrP = sPr[-1]
        print(askP, bidP, sPrP)
    
def inp():
    nC = int(stdin.readline())
    ask, bid, sPr = [], [], []
    for _ in range(nC):
        nL = int(stdin.readline())
        for _ in range(nL):
            t = stdin.readline().split()
            p = int(t[-1])
            c = int(t[1])
            if t[0] == "buy":
                heappush(bid, [-p, c])
                ask, bid, sPr = stock(ask, bid, sPr)
                imp(ask, bid, sPr)
            elif t[0] == "sell":
                heappush(ask, [p, c])
                ask, bid, sPr = stock(ask, bid, sPr)
                imp(ask, bid, sPr)
        ask, bid, sPr = [], [], []
inp()