"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска, каждый раз предполагая что искомое число среднее в группе.
    Изначально группа определяется как нижняя граница -1 от минимально возможного числа, верхняя граница 
    +1 от максимально возможного числа. Если после первой попытки загаданно число больше, то нижняя граница
    становится числом из первой группы, если меньше, то этим числом становиться верхняя граница.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    up_bond = 101
    low_bond = 0
    predict_number = up_bond//2
    while True:
        count += 1
        if predict_number > number:
            up_bond = predict_number
            predict_number = (up_bond+low_bond)//2
        elif predict_number < number:
            low_bond = predict_number
            predict_number = (up_bond+low_bond)//2
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:

        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN

    print(score_game(random_predict))
