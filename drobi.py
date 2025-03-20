import deliteli
from force_power import powering

class Rational:
    def __init__(self, numer: int, denom: int):
        self.numer = numer
        self.denom = denom
    def __copy__(self):
        return type(self)(self.numer, self.denom)

def creat(number, denom):
    if denom == 0:
        return "inf"
    r = Rational(number, denom)
    return r

def add(n, d):
    a = n.__copy__()
    b = d.__copy__()
    if a.denom == b.denom:
        a.numer += b.numer
    else:
        min_delit = deliteli.nok(a.denom, b.denom)
        a.numer *= min_delit // a.denom
        b.numer *= min_delit// b.denom
        a.denom = min_delit
        a.numer += b.numer
    return a

def sub(n, d):
    a = n.__copy__()
    b = d.__copy__()
    if a.denom == b.denom:
        a.numer -= b.numer
    else:
        min_delit = deliteli.nok(a.denom, b.denom)
        a.numer *= min_delit // a.denom
        b.numer *= min_delit // b.denom
        a.denom = min_delit
        a.numer -= b.numer
    return a

def mul(n, d):
    a = n.__copy__()
    b = d.__copy__()
    a.numer *= b.numer
    a.denom *= b.denom
    return a

def div(n,d):
    a = n.__copy__()
    b = d.__copy__()
    a.numer *= b.denom
    a.denom *= b.numer
    if a.denom == 0:
        return "inf"
    return a


def power(n, power):
    r = n.__copy__()
    if power > 0:
        r.numer = powering(r.numer, power)
        r.denom = powering(r.denom, power)
    elif power < 0:
        r.numer, r.denom = r.denom, r.numer
        r.numer = powering(r.numer, abs(power))
        r.denom = powering(r.denom, abs(power))
    else:
        r.numer = 1
        r.denom = 1
    return r

def simplify(r):
    if r.numer >= r.denom or r.numer % r.denom == 0 or r.numer == 0:
        return _to_int(r)
    else:
        return _to_float(r)

def _to_int(r):
    if r.numer == 0:
        return 0
    max_delit = deliteli.nod(r.numer, r.denom)
    return r.numer // max_delit

def _to_float(r):
    max_delit = deliteli.nod(r.numer, r.denom)
    r.denom /= max_delit
    r.numer /= max_delit
    r.int_part = 0
    if r.numer > r.denom:
        r.int_part = max_delit
        r.numer = r.numer - (r.denom * max_delit)
    a = r.int_part + round(r.numer/r.denom, 2)
    return a

def to_str(r):
    max_delit = deliteli.nod(r.numer, r.denom)
    answer = str(r.numer//max_delit) + "/" + str(r.denom//max_delit)
    return answer

def output(answer):
    print("Answer is:", to_str(answer), "or", simplify(result))

def input_drob():
    a, b = map(int, input().split())
    drob = creat(a,b)
    return drob

if __name__ == "__main__":
    drob = input_drob()
    adder = input_drob()
    result = add(drob, adder)
    output(result)
    result = sub(drob, adder)
    output(result)
    result = mul(drob, adder)
    output(result)
    result = div(drob, adder)
    output(result)
    result = power(drob, -2)
    output(result)