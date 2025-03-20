def powering(val, pow):
    res, v, c = 1, val, pow
    if c &1:
        res = v
    c >>= 1
    while c>0:
        v = v * v
        if c&1:
            res = v*res
        c = c>>1
    return res

if __name__ == "__main__":
    print(powering(2,10))