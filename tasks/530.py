def map(func, sequene):
    lst = []
    for i in sequene:
        lst.append(func(i))
    return lst