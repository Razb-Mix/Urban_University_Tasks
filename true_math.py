from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

if __name__ == "__main__":
    print(divide(5, 0))