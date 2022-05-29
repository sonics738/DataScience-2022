
"""Game: Guess the number"""
import numpy as np

def random_predict_v2(number:int=1) -> int:
    """ Randomly guessing the number

    Args:
        number (int, optional): Random number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    count = 1
    min_num = 1
    max_num = 100
    
    while min_num <= max_num:
        predict_number = round((max_num + min_num)/2) #First guessed number
        if predict_number == number:
            break #Exit from the cycle if succesful, otherwise,
                  #sequentially reducing the searching area by half 
        if number < predict_number:
            max_num = predict_number - 1
        else:
            min_num = predict_number + 1
        count+=1       
        
    return(count)
print(f'Number of attempts: {random_predict_v2()}')

def score_game_v2(random_predict) -> int:
    """Code of average number of attempts out of 1000 guesses

    Args:
        random_predict ([type]): Guessing function

    Returns:
        int: Average number of attempts
    """

    count_ls = [] # List of number of attempts
    np.random.seed(1) # Fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # Produce list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # Average number of attempts

    print(f'Your code is guessing the random number in average for: {score} attempts')
    return(score)


# RUN
if __name__ == '__main__':
    score_game_v2(random_predict_v2)
