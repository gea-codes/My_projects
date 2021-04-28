import numpy as np

count = 0                           # счетчик попыток
number = np.random.randint(1, 101)   # загадали число
print(" Загадано число от 1 до 100 ")


def game_core(number):
    count = 1
    min = 1  # нижняя граница интервала для отгадывания
    max = 101   # верхняя граница интервала для отгадывания

    while count < 30:
        count += 1
        mid = int(min + (max - min)/2)
        if mid > number:
            max = mid
            print(f"Загаданное число в интервале {min} - {max}")
        elif mid < number:
            min = mid
            print(f"Загаданное число в интервале {min} - {max}")
        else:
            print(f"Вы угадали число {number} за {count} попыток")
            return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)