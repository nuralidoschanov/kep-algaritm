# def map_square(sequence):
#     new = []
#     for n in sequence:
#         new.append(n ** 2)
#     return new

def map_square(sequence):
    return map(lambda x:x ** 2, sequence)

print(map_square([5, -8, 12]))
    