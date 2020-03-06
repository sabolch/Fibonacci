def fibonacci(x):

    sequence = []
    result = 0
    n = 1

    for i in range(x):
        result = result + n
        n = result - n
        sequence.append(result)

    golden_ratio = sequence[-1] / sequence[-2]

    print(sequence)
    print(golden_ratio)


fibonacci(20)
