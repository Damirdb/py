#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
# TODO здесь ваш код
x = set.update(garden_set,meadow_set)
print(x)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
y = set.union(garden_set,meadow_set)
print(y)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
z = garden_set ^ meadow_set
print(z)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
w = set.difference_update(meadow_set,garden_set)
print(w)
