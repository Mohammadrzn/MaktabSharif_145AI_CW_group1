from functools import reduce

def flatten_reduce_lambda(matrix):
    return list(reduce(lambda x, y: x + y, matrix, []))

with open("q18.txt") as f:
    lines = f.read()
    print(flatten_reduce_lambda([line.split(" - ") for line in lines.split("\n")]))