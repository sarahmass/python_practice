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
    winning_stair = 60 # win if higher than 60 steps after 100 rolls
    
    all_games = []
    final_steps= []
    fig, ax = plt.subplots(2,1)
    
    
    
    for n in range(play_n_times):
        game = play_game(rolls_per_game, clumsy_rate)

        # Sample a few of the random stair falls
        if n in range(1,play_n_times,500):
            ax[0].plot(game)
        
        # collect final step value
        final_steps.append(game[-1])

        # collect full game details
        all_games.append(game)
    
    np_all_games = np.array(all_games)
    
    #plt.clf()
    # add line at winning_stair to view successful and unsuccessful climbs    
    ax[0].plot(list(range(101)),[winning_stair]*101, "k-")
    ax[0].set_title("Sample of Games Played", fontsize=10)
    ax[0].set_xlabel("roll number",fontsize=8)
    ax[0].set_ylabel("stair number", fontsize=8)
        

    # Plot the histogram of all final steps to visualize distribution
    np_final_steps = np.array(final_steps)
    
    ax[1].hist(final_steps)
    ax[1].set_xlabel("final stair value",fontsize=8)
    ax[1].set_ylabel("number of games", fontsize=8 )
    ax[1].set_title(f"Distribution of Final Stair of {play_n_times} Games",fontsize=10  )

    
    make_it = np_final_steps >=60
    print(f"{sum(make_it)/len(final_steps)*100:.2f}% of the time the games makes it to/past the {winning_stair}th stair")
    ax[1].plot([winning_stair]*3200, list(range(0,3200)),'r-' )
    ax[1].text(62,300,f"     {sum(make_it)/len(final_steps)*100:.2f}% \nmake it to stair {winning_stair}")
    plt.show() 

        
        

        
        