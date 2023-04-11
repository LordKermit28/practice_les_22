# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def move(self, field, x: int, y: int, direction, is_fly: bool, crawl: bool, speed: int = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        """
        # Для начала проверим не установлены ли у нас два флага полета и подкрадывания в истину,
        # т.к. одновременно эти события не должны происходить
        if is_fly and crawl:  # если оба параметра установлены как True
            # выбросим ошибку
            raise ValueError('Рожденный ползать летать не должен!')
        # Если ошибку мы не выбросили, значит все у нас ок и в принципе мы можем переходить к дальнейшему выполнению кода

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)


