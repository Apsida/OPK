def nod(a,b):
    if a == 0:
        return b
    div = nod(b%a, a)
    return div

def nok(a,b):
    if a > b:
        greater = a
    else:
        greater = b

    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            minim = greater
            break
        greater += 1

    return minim

if __name__ == "__main__":
    print(nod(35,5))
    print(nok(2,14))