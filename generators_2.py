# implement generator by class which count fibonacci numbers
# be careful here, wrong implementation may cause memory leak

class FibonGenerator:
    def __init__(self, count: int):
        pass


# tests
fibon_generator = FibonGenerator(8)

assert list(fibon_generator) == [0, 1, 1, 2, 3, 5, 8, 13]

print('Success')
