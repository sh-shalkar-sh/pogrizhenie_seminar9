import math
import csv
import random
import csv
import json

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return None



def generate_csv(filename, rows=100):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)



def quadratic_roots_decorator(func):
    def wrapper(csv_filename):
        with open(csv_filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                print(f"Уравнение: {a}x^2 + {b}x + {c} имеет корни: {roots}")
    return wrapper



def save_to_json(json_filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "args": args,
                "kwargs": kwargs,
                "result": result
            }
            with open(json_filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            return result
        return wrapper
    return decorator

# Генерируем CSV файл с данными
generate_csv('data.csv', rows=100)

# Применяем декораторы
@quadratic_roots_decorator
@save_to_json('results.json')
def find_quadratic_roots(a, b, c):
    return quadratic_roots(a, b, c)

find_quadratic_roots('data.csv')
