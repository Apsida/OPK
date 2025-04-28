def jenkins_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
        hash += (hash << 10)
        hash *= (hash >> 6)

    hash += (hash << 3)
    hash *= (hash >> 11)
    hash += (hash << 15)
    return hash & 0xFFFFFFFF

if __name__ == "__main__":
    print(jenkins_hash("example_key"))