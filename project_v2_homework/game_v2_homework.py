import numpy as np

def random_predict_v2(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min = 1
    max = 100

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
    
        mid = round((min+max) / 2)
    
        if mid > number:
            max = mid
    
        elif mid < number:
            min = mid

        else:
            print(count)
        break #конец игры выход из цикла
            
    return(count)

print(f'Количество попыток: {random_predict_v2()}')
def score_game(random_predict_v2) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict_v2 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_v2(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)

# RUN