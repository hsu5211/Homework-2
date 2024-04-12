liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

Tok = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]

def Swap(Amt, From, To) :
    if (From, To) not in liquidity:
        F,T = liquidity[(To, From)]
        return F-T*F/(T+Amt)
    else:
        F,T = liquidity[(From, To)]
        return T-T*F/(F+Amt)

def FindPath(CurTok, CurAmt, Path, Visited, MaxAmt) :
    if len(Path) > 1 and Path[-1] == "tokenB" and CurAmt > MaxAmt["amount"]:
        MaxAmt["amount"] = CurAmt
        MaxAmt["path"] = Path.copy()
    for Token in Tok:
        if Token != CurTok:
            if (CurTok, Token) in liquidity :
                edge = (CurTok, Token)
            else :
                edge = (Token, CurTok)
            if edge not in Visited:
                NewAmt = Swap(CurAmt, CurTok, Token)
                Visited.add(edge)
                Path.append(Token)
                FindPath(Token, NewAmt, Path, Visited, MaxAmt)
                Path.pop()
                Visited.remove(edge)
    return

MaxAmt = {"amount": 0, "path": []}
FindPath("tokenB", 5, ["tokenB"], set(), MaxAmt)
print("path: ", "->".join(MaxAmt['path']), ", ", f"tokenB balance={MaxAmt['amount']:.6f}", sep="")
