import array as arr
from models.Order import *

order1 = Order("Birthday1", arr.array('i', (3, 21, 5, 2020)), arr.array('i', (7, 20, 7, 2020)), 2, "red", "started",
               1000)
order2 = Order("Vanilla Cupcakes (25)", arr.array('i', (1, 11, 5, 2020)), arr.array('i', (7, 20, 7, 2020)), 1, "yellow",
               "started", 1000)
order3 = Order("Triple Chocolate Cake", arr.array('i', (7, 30, 5, 2020)), arr.array('i', (7, 20, 7, 2020)), 2, "red",
               "started", 20000)
order4 = Order("Strawberry Pie", arr.array('i', (2, 1, 5, 2020)), arr.array('i', (7, 20, 7, 2020)), 2, "red", "started",
               32000)
order5 = Order("Vegan Cake", arr.array('i', (5, 12, 5, 2020)), arr.array('i', (7, 20, 7, 2020)), 1, "green", "started",
               25000)
order6 = Order("Marble cake", arr.array('i', (6, 2, 5, 2020)), arr.array('i', (6, 17, 5, 2020)), 1, "yellow",
               "started", 15000)
order7 = Order("Carrot Cake", arr.array('i', (1, 25, 5, 2020)), arr.array('i', (1, 25, 5, 2020)), 2, "red",
               "started", 20000)
order8 = Order("Chocolate Croissant (10)", arr.array('i', (1, 4, 5, 2020)), arr.array('i', (2, 12, 5, 2020)), 2, "red",
               "started", 32000)
order9 = Order("Macaroons (25)", arr.array('i', (5, 28, 4, 2020)), arr.array('i', (5, 15, 5, 2020)), 1, "green",
               "started", 25000)
order10 = Order("Chocolate Chip Cookie", arr.array('i', (1, 4, 5, 2020)), arr.array('i', (6, 22, 5, 2020)), 1, "yellow",
                "started", 15000)