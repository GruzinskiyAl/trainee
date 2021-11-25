# implement pattern Decorator by classes
# decorated object should return result of decorated component + 1


class BaseComponent:
    def operation(self, payload: int):
        pass


class Square(BaseComponent):
    def operation(self, payload: int):
        pass


class Qube(BaseComponent):
    def operation(self, payload: int):
        pass


class PlusOneDecorator(BaseComponent):
    def operation(self, payload: int):
        pass


# tests
square_plus_one = PlusOneDecorator(Square())
assert square_plus_one.operation(3) == 10

qube_plus_one = PlusOneDecorator(Qube())
assert qube_plus_one.operation(3) == 28

print('Success')
