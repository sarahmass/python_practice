## Climbing Tower Game - a twist on the random walk.
The game goes like this: 
You roll a die, move up one stair, down one stair, or get a second roll and move up that many stairs. This makes it like a Chutes and Ladder game without the chutes until we add the clumsiness. You also have a probability of being clumsy and falling back to the bottom with every move. But, the roll of the die does not determine the falls. The clumsy probability is selected or set for the games. A random number, between 0 and 1, is generated from a uniform distribution for every move.  If the number falls at or below the clumsy probability value, you fall to the bottom, if it is above, you remain on the stair. The wining stair is stair 60. If you end the game of 100 rolls at or above stair 60 you win.

## The purpose of this code
The purpose of this code was to answer the question: What is the probability that I win the game? 

To answer this question we simulate the process of playing the game 10,000 times. We take note of the stair that was achieved at each game and then report the probability of winning the bet. 

## The code
Included are several helper functions
- `roll_dice()` returns a number between 1 and 6 inclusively and is selected from a random number generator with uniform probability. Each number has a probability of being returned equal to `1/6 ~ 16.67%`.
- `i_fall(fall_rate)` returns a boolean value. `True`, you fall. `False`, you don't fall.
- `move(roll)` based on the roll of the die this returns 1, -1, or the value of a second roll of the die.
    Moves are determined based on the die's face that is facing upwards.
    A roll of: 
    - 1 or 2 --> Move up 1
    - 3, 4, or 5 --> Move down 1
    - 6 -->
          - roll again
          -  move up 1, 2, 3, 4, 5, or six steps as determined by the roll. 
- `play_game(rolls_per_game, fall_rate)` returns the location after each of the rolls in a list.

The simulation is run by setting the number of times to play the game (`play_n_times`), the rolls per game (`rolls_per_game`), fall rate (clumsy_rate), winning stair (`winnning stair`) and then we collect all of the data, graph a few of the individual games and a histogram of all of the last steps. 

## Results
The game can be won with an approximate probability of `78.14%` with the following values set:
- clumsy rate = .001 = 0.1%
- rolls per game = 100
- winning stair = 60 
- number of game simulations = 10,000 

The probability of falling can be edited by editing the `clumsy_rate`.

![climbingGame2](https://github.com/sarahmass/python_practice/assets/54375901/943f256b-bfb1-4068-950c-38f6594fb3d7)

## Improvements
There are several ways that this can be improved. 
- We could look at how each of the variables changes the results.
- results can be viewed as an animation,
- add a graphical user interface to allow someone to change the variables without going into the code.
-  The list goes on...

## Acknolegements
I was going through evaluating the data science program on a few online learning platforms.  This problem was included in [DataCamp's](https://app.datacamp.com/) Intermediate Python course. The course walked through their code, but I decided to create my own first. The setup for the problem is the same as the assignment in the course, but our strategies for coding it were different. 


