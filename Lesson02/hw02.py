# Даны три множества a,b и с. Необходимо выполнить все изученные виды бинарных операций над всеми комбинациями множеств.

a = {0, 1, 1, 2, 3, 5, 8}
b = {2, 4, 6, 8, 10}
c = {1, 3, 5, 7, 9}

# Объединение: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
print("Объединение:")
print(a.union(b).union(c))
print()

# Пересечение: {};
print("Пересечение:")
print(a.intersection(b).intersection(c))
print()

# Разность (a - b - c): {0};
print("Разность:")
print(a.difference(b).difference(c))
print()

# Симметрическая разность: {0, 4, 6, 10}.
print("Симметрическая разность:")
print(a.symmetric_difference(b).symmetric_difference(c))
print()
