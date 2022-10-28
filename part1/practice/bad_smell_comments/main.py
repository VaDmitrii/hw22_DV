# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def move(self, unit_field, x_coor: int, y_coor: int, direction, is_fly: bool, crowl: bool, speed: int = 1):

        if is_fly and crowl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coor + speed
                new_x = x_coor
            elif direction == 'DOWN':
                new_y = y_coor - speed
                new_x = x_coor
            elif direction == 'LEFT':
                new_y = y_coor
                new_x = x_coor - speed
            elif direction == 'RIGHT':
                new_y = y_coor
                new_x = x_coor + speed
        if crowl:
            speed *= 0.5
            if direction == 'UP':  
                new_y = y_coor + speed
                new_x = x_coor
            elif direction == 'DOWN':
                new_y = y_coor - speed
                new_x = x_coor
            elif direction == 'LEFT':
                new_y = y_coor
                new_x = x_coor - speed
            elif direction == 'RIGHT':
                new_y = y_coor
                new_x = x_coor + speed

            unit_field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
