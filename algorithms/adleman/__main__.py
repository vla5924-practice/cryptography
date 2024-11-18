import math

def prime_factors(n):
    """Возвращает список простых множителей n с их кратностью."""
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def discrete_log_adleman(g, h, p):
    """
    Возвращает дискретный логарифм log_g(h) по модулю p, используя
    упрощенную версию алгоритма Адлемана.
    """
    # Находим факторизацию p-1
    fact_p_minus_1 = prime_factors(p - 1)

    # Создаем список уникальных простых множителей
    unique_factors = list(set(fact_p_minus_1))

    # Ищем решения для каждого простого множителя
    log_values = []
    for q in unique_factors:
        # Применяем метод китки младших индексов (Shanks' baby-step giant-step)
        # для нахождения логарифма относительно простого числа q
        m = int(math.ceil(math.sqrt(q)))
        
        # Создаем таблицу для малого шага
        baby_steps = {pow(g, j, p): j for j in range(m)}

        # Вычисляем инверсию огромного шага
        # g^(-m) mod p
        c = pow(g, m * (p - 2), p)

        # Ищем совпадение в большом шаге
        found = False
        for i in range(m):
            y = (h * pow(c, i, p)) % p
            if y in baby_steps:
                log_values.append(i * m + baby_steps[y])
                found = True
                break

        if not found:
            raise ValueError("Не удалось найти дискретный логарифм.")

    # Используем китайскую теорему об остатках для нахождения результата
    x = 0
    n = 1
    for q, log_value in zip(unique_factors, log_values):
        while x % q != log_value:
            x += n
        n *= q

    return x

if __name__ == "__main__":
    # Примеры ввода
    g = 5  # База логарифма
    h = 8  # Значение логарифма
    p = 23 # Модуль

    # Вычисление дискретного логарифма
    log_result = discrete_log_adleman(g, h, p)
    print(f"log_{g}({h}) mod {p} = {log_result}")
