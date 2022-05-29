import numpy as np

def random_predict_v2(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 1
    min_num = 1
    max_num = 1000
    
    while min_num <= max_num:
        predict_number = round((max_num + min_num)/2) #предполагаемое число
        if predict_number == number:
            break #выход из цикла, если угадаем, а если нет,
                  #то последовательно сужаем границы поиска вдвое 
        if number < predict_number:
            max_num = predict_number - 1
        else:
            min_num = predict_number + 1
        count+=1       
        
    return(count)

print(f'Количество попыток: {random_predict_v2()}')

def score_game_v2(random_predict_v2) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_v2(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    score_game_v2(random_predict_v2)
