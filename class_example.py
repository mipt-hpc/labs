# -*- coding: utf-8 -*-
# создаём первый супер-класс
class mainClass:
        arg1 = 'This is argument 1 from class mainClass;'
        arg2 = 'This is argument 2 from class mainClass;'
        def ext_1(self):
                return 'This if method ext_1 from class mainClass.'

# создаём объект суперкласса
main_class = mainClass()

# создаём сабкласс
# который наследует атрибуты суперкласса mainClass
class firstInherit(mainClass):
        arg3 = 'This is argument 3 from class firstInherit;'
        arg4 = 'This is argument 4 from class firstInherit;'
        def ext_2(self):
                return 'This if method ext_2 from class firstInherit.'

first_inherit = firstInherit()

# создаём второй сабкласс
# который наследует атрибуты классов mainClass и firstInherit
class secondInherit(mainClass, firstInherit):
        arg5 = 'This is argument 5 from class firstInherit;'
        arg6 = 'This is argument 6 from class firstInherit;'
        def ext_3(self):
                return 'This if method ext_3 from class secondInherit.'

second_inherit = secondInherit()
