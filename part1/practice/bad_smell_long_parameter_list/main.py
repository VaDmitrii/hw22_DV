# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, state: str, unit_field, speed: int = 1):
        self.state = state
        self.speed = speed
        self.unit_field = unit_field

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.unit_field.set_unit(x=self.x_coord, y=self.y_coord + speed, unit=self)
        elif direction == 'DOWN':
            self.unit_field.set_unit(x=self.x_coord, y=self.y_coord - speed, unit=self)
        elif direction == 'LEFT':
            self.unit_field.set_unit(x=self.x_coord - speed, y=self.y_coord, unit=self)
        elif direction == 'RIGTH':
            self.unit_field.set_unit(x=self.x_coord + speed, y=self.y_coord, unit=self)

    def _get_speed(self) -> float:

        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')

    ...
