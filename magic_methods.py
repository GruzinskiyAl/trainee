class MagicClass:
    def __init__(self, val):
        self.val = val


# tests
obj_27 = MagicClass(27)
obj_3 = MagicClass(3)
obj_9 = MagicClass(9)

assert obj_27 + obj_3 == '273'
assert obj_27 - obj_3 == 24
assert obj_27 == obj_3 * obj_9
assert obj_27 / obj_3 == '27/3'
assert obj_3 ** 2 == 9
assert str(obj_27) == 'object - 27'
assert str(obj_3) == 'object - 3'
assert obj_27 < obj_3
