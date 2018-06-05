def is_armstrong(number):
    s = str(number)

    return sum(map(lambda n: int(n) ** len(s), s)) == number
