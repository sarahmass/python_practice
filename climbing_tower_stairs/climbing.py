import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 
import statistics 

# using random package with in numpy
np.random.seed(123)


def roll_dice():
    return np.random.randint(1,7)

def i_fall(fall_rate):
    # on each move i fall with a
    # fall_rate * 100% chance.
    random_chance = np.random.rand()
    do_i_fall =  random_chance <= fall_rate
    return (do_i_fall)

def move(roll):
    # rolls of 1 or 2 move down one step
    if roll in [1,2]:
        return -1
    
    # rolls of 3, 4, or 5 move up one step
    if roll in [3,4,5]:
        return 1
    
    # if roll is 6, roll again and move 
    # up the same number of steps as the 
    # new roll of the dice.
    return roll_dice()

def play_game(rolls_per_game, fall_rate):
    # starting at the bottom
    step = 0
    location = [0]
    for roll_num in range(rolls_per_game):
        dice_roll = roll_dice()
        step = max(step + move(dice_roll), 0)
        if i_fall(fall_rate): 
            #print(f"Aaahh! I have fallen from step {step} on roll {roll_num}")
            step = 0

        location.append(step)
    return location



if __name__ == "__main__":
    play_n_times = 10000
    rolls_per_game = 100
    clumsy_rate = 0.001 # clumsy_rate * 100% chances of falling
    
    
    all_games = []
    final_steps= []
    
    for n in range(play_n_times):
        game = play_game(rolls_per_game, clumsy_rate)
        final_steps.append(game[-1])
        all_games.append(game)
    plt.hist(final_steps)
    np_final_steps = np.array(final_steps)
    plt.clf()
    plt.plot(all_games[0])
    make_it = np_final_steps >=60
    print(f"I will make it to step 60, and win the bet {sum(make_it)/len(final_steps)*100:.2f}% of the time")
    
    plt.show() 

        
        

        
        