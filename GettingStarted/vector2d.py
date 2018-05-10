import math


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return ("X: " + str(self.x) + ", Y: " + str(self.y))


def Main():
    vec = Vector2D(5, 6)
    vec2 = Vector2D(2, 3)
    print(vec)
    print(vec2)

    vec = vec + vec2
    print(vec)

    vec += vec2
    print(vec)


if __name__ == '__main__':
    Main()
