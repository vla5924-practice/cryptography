# Алгоритм Шенкса

Алгоритм Шенкса, также известный как метод шагов младшего и старшего (Baby-step giant-step), используется для вычисления дискретного логарифма. Это задача: найти $x$ в уравнении $g^x \equiv h \pmod{p}$, где $g$ и $h$ известны, а $p$ — простое число.

## Объяснение кода:

1. **Определение размера таблицы `m`.**
   Мы вычисляем $m$ как $\sqrt{p - 1} + 1$ для обеспечения перекрытия между младшими и старшими шагами.

2. **Создание таблицы "младших шагов".**
   Мы создаем словарь с ключами в виде значений $g^j \mod p$ и значениями как сами $j$.

3. **Вычисление $g^{-m} \mod p$.**
   Используем малую теорему Ферма для вычисления обратного элемента $g^m$. Это ускоряет вычисление гигантских шагов.

4. **Проведение "гигантских шагов".**
   Последовательно проверяем, существует ли текущее значение в таблице младших шагов. Если найдено, то вычисляем и возвращаем $i \cdot m + j$.

## Запуск приложения:
Для запуска скрипта просто сохраните его в файл с расширением `.py` (например, `baby_step_giant_step.py`) и выполните через командную строку при помощи Python. Подставьте значения $g$, $h$ и $p$ по вашему усмотрению.

> https://en.wikipedia.org/wiki/Baby-step_giant-step