# Алгоритм Полига — Хеллмана

## Подробности и комментарии к коду:

1. **Импорт библиотеки `math`:** Мы используем функцию `math.ceil` для вычисления верхней границы корня из числа.

2. **Описание функции `baby_step_giant_step`:** Функция принимает три аргумента: основание $g$, значение $h$ и модуль $p$. Мы ищем $x$ такое, что $g^x \equiv h \pmod{p}$.

3. **Инициализация и вычисление малых шагов (baby steps):** Мы вычисляем значения $g^j \mod p$ для $j$ от 0 до $n-1$ и сохраняем их в словаре для быстрого доступа.

4. **Инициализация и вычисление больших шагов (giant steps):** Вычисляем $h \times (g^{-n})^i \mod p$ и сравниваем с таблицей малых шагов.

5. **Проверка и нахождение решения:** Если найдена соответствующая пара (giant step, baby step), вычисляем значение $x = i \times n + j$.

6. **Главная функция:** Запрашивает входные данные у пользователя и вызывает алгоритм. Выводит найденный дискретный логарифм либо указывает, что решение не найдено.

Этот код является учебной версией и использует функции стандартной библиотеки Python для возведения в степень с модулем и вычисления обратных элементов. Перед запуском убедитесь, что используемые числа соответствуют ограничениям алгоритма.

> https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm
