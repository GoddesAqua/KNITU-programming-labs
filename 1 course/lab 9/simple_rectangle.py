class Rectangle:
    width = 1
    length = 1

    def edit_width(self, width):
        if 0 <= width <= 20 and type(width) is float:
            self.width = width
        else:
            print('Ошибка, число должно быть типа float'
                  'и находится между 0 и 20')

    def edit_length(self, length):
        if 0 <= length <= 20 and type(length) is float:
            self.length = length
        else:
            print('Ошибка, число должно быть типа float'
                  'и находится между 0 и 20')

    def perimetr(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length


if __name__ == '__main__':
    user_rectangle = Rectangle()
    user_rectangle.edit_length(float(input()))
    user_rectangle.edit_width(float(input()))
    print(user_rectangle.width, user_rectangle.length,
          user_rectangle.perimetr(), user_rectangle.area())
