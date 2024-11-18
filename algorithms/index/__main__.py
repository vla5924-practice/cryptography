import random
import math
from sympy import isprime, primerange
from sympy.ntheory import factorint
from sympy import Matrix

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Функция для генерации факторабельной базы
def generate_factor_base(p, bound):
    return [prime for prime in primerange(2, bound) if isprime(prime)]

# Функция для вычисления дискретного логарифма
def index_calculus(p, g, h, B):
    factor_base = generate_factor_base(p, B)
    
    # Генерируем систему уравнений
    relations = []
    exponents = []
    while len(relations) < len(factor_base):
        exponent = random.randint(1, p - 1)
        value = pow(g, exponent, p)
        
        # Пытаемся факторизовать число по базе
        factors = factorint(value)
        
        # Проверяем, можно ли факторизовать целиком на базе
        if all(prime in factor_base for prime in factors):
            relations.append(factors)
            exponents.append(exponent)
        
    # Создаем матрицу и решаем систему уравнений
    num_relations = len(relations)
    num_factors = len(factor_base)
    
    matrix = []
    for i in range(num_relations):
        row = [0] * num_factors
        for j, prime in enumerate(factor_base):
            if prime in relations[i].keys():
                row[j] = relations[i][prime]
        matrix.append(row)

    # Приводим матрицу к ф2, добавляем вектора
    matrix = Matrix(matrix)
    matrix = matrix.row_insert(Matrix([exponents]).T, num_factors)
    
    solution = matrix.rref(iszerofunc=lambda x: x % (p - 1) == 0, simplify=True)[0]
    
    # Используем решение для нахождения дискретного логарифма
    exponent = random.randint(1, p - 1)
    lhs = (h * pow(g, exponent, p)) % p
    
    while True:
        known_factors = factorint(lhs)
        if all(prime in factor_base for prime in known_factors):
            result = exponent
            for prime, power in known_factors.items():
                index = factor_base.index(prime)
                result = (result - solution.row(index)[-1] * power) % (p - 1)
            return result
        exponent = random.randint(1, p - 1)
        lhs = (h * pow(g, exponent, p)) % p

# Пример использования
if __name__ == "__main__":
    # Параметры задачи
    p = 101
    g = 2
    h = 54
    B = 30

    dlog = index_calculus(p, g, h, B)
    print(f"Дискретный логарифм {h} по основанию {g} в поле GF({p}) равен: {dlog}")
