from sympy import symbols, Matrix
from sympy.polys import Poly
from Crypto.Util.number import inverse, long_to_bytes
import numpy as np

# Ввод многочлена
x = symbols('x')
# f(x) = x^3 + 2x + 1, например
f = Poly(x**3 + 2*x + 1, x)

# Параметры
N = 97  # модуль
X = N**(1/3)  # граница для малых корней

def construct_lattice(f, N, X):
    # Построение решетки
    n = f.degree()
    # Рассчитываем размер решетки
    size = n*n
    # Инициализируем решетку нулями
    B = np.zeros((size, size))
    
    # Меняем степень i и j для заполнения решетки
    for i in range(n):
        for j in range(n):
            B[i*n+j][j] = N**(i) * X**(n-j)
    
    # Заполняем предотвращающую строку
    coeffs = [c % N for c in f.all_coeffs()]
    for j in range(n):
        B[n*n-1][j] = coeffs[j] * X**(n-j)
    
    return B

def find_roots(f, N, X):
    # Построение матрицы решетки
    B = construct_lattice(f, N, X)
    # Преобразуем в объект sympy Matrix
    B = Matrix(B)
    # Применяем LLL редукцию
    B_reduced = B.LLL()
    # Находим первые вектор-кандидаты
    candidates = B_reduced[:, 0].tolist()
    roots = []
    # Проверка на истинные корни
    for candidate in candidates:
        root = sum(candidate[i]*X**i for i in range(f.degree()))
        if f.subs(x, root) % N == 0:
            roots.append(root)
    return roots

# Поиск малых корней
roots = find_roots(f, N, X)
# Вывод найденных корней
print("Найденные малые корни:", roots)
