import math

def baby_step_giant_step(g, h, p):
    """
    Алгоритм Полига — Хеллмана (англ. baby-step giant-step) для решения задачи
    дискретного логарифма: найти x, которое удовлетворяет уравнению g^x = h (mod p).
    """
    
    # Найдем значение n такое, что n^2 приблизительно равно p (n = m in context of Polig — Hellman)
    n = math.ceil(math.sqrt(p - 1))

    # Создание таблицы для малых шагов (baby steps)
    # {(g^j mod p): j}
    baby_table = {}
    for j in range(n):
        baby_step = pow(g, j, p)
        baby_table[baby_step] = j
        print(f"Baby Step {j}: g^{j} ≡ {baby_step} (mod {p})")

    # Вычисляем величину g^-n (обратный элемент для шага)
    g_inv_n = pow(g, -n, p)

    # Giant steps - проверяем совпадение с малым шагом
    for i in range(n):
        # Вычисление h * (g^-n)^i mod p
        giant_step = (h * pow(g_inv_n, i, p)) % p
        print(f"Giant Step {i}: h*g^{{-n*i}} ≡ {giant_step} (mod {p})")

        # Проверяем, если giant_step уже в таблице малых шагов
        if giant_step in baby_table:
            # Если нашли совпадение, находим решение
            j = baby_table[giant_step]
            x = i * n + j
            print(f"Решение найдено: x ≡ {x} (mod {p})")
            return x

    # Если не нашли комбинацию малых и больших шагов
    print("Решение не найдено.")
    return None

def main():
    print("Программа для решения задачи дискретного логарифма с помощью алгоритма Полига — Хеллмана.")
    g = int(input("Введите основание g: "))
    h = int(input("Введите значение h: "))
    p = int(input("Введите простое число p: "))

    result = baby_step_giant_step(g, h, p)
    if result is not None:
        print(f"Дискретный логарифм x найден: {result}")
    else:
        print("Не удалось найти решение.")

if __name__ == "__main__":
    main()
