#Program rozpoczyna się od zdefiniowania słownika ekwipunek. Słownik ten:
# posiada klucz pieniądze, który przechowuje wartość typu float
# posiada klucz sprzęt, który przechowuje listę przedmiotów. Każdy przedmiot jest typu str.
# posiada klucz prowiant, który przechowuje listę jadalnych rzeczy.


equipment = {
    'money': 150.40,
    'equipment': ['flashlight', 'flint', 'socks', 'compass'],
    'food': ['water', 'apple', 'sandwich', 'bar']
}

print(equipment)
print(equipment['money'])
