class Figure:
    def __init__(self, color, *sides):
        self.__sides = [1] * self.sides_count if len(sides) != self.sides_count else list(sides)
        self.__color = list(color)
        self.filled =False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(s > 0 for s in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14)

    def get_square(self):
        return 3.14* self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        s = sum(self.get_sides()) / 2
        area = (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5
        return area

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides_length):
        super().__init__(color, *[sides_length] * 12)
        self.__sides = [sides_length] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
