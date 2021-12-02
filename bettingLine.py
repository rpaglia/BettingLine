# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:45:52 2021
@author: Richard Paglia

How good is the betting line?

attached is a file of the first 8 weeks of the NFL season.  Columns are week, visit team, home team, the line (first entry is DAL at TB the betting line is -7.5, that means bookmakers expect if a large number of games were played between DAL and TB, at TB, the average difference in scores would be Tampa Bay to win by 7.5.  The last column is the actual difference; in this case TB actually won by 2.   

Line 12  CLE at KC- the betting line is -8.  That means that the bookmakers expect, on average, KC would win by 8   The average difference in score CLE - KC would be 8.  So the betting line is KC-8.  And it turned out that KC LOST the game by 4.

Using the data in the .csv file, construct a linear model:  actual score = b0 + b1* line

If the bookmakers were perfect, b0 would be 0 and b1 would be 1.             lineVSactual.csv 

Interpret the results.  Is b0 significantly different from 0?    Is b1 significantly different from 1?

What does this mean about betting line in the NFL?

"""
import matplotlib.pyplot as plt
import numpy as np
input_file = "P:\AVC Python Class\Working Directory\lineVSactual-1.csv"

def get_data(input_file):    
    with open(input_file, 'r') as data_file:
        betLine = []
        homeVictory = []  
        data_file.readline()      
        count = 0
        for line in data_file:
            __, __, __, bL, actS = line.split(',')
            betLine.append(float(bL))
            homeVictory.append(float(actS))
            count +=1
            if count > 16: break
    return (betLine, homeVictory)

plt.clf()
plt.figure(1)
betLine, homeVictory = get_data(input_file)

lineSB = [-x for x in homeVictory]
diffLineScore = np.array(betLine) - np.array(lineSB)

plt.plot(betLine, lineSB, 'kx', label='Week 1 NFL line vs score')
plt.title('Sucker\'s Bet!')
plt.xlabel('bet line')
plt.ylabel('home victory')
plt.grid()
plt.legend()
plt.show()

plt.figure(2)
plt.hist(diffLineScore)
plt.show()

plt.figure(3)
plt.hist(betLine, color = 'red', alpha = 0.3)
plt.hist(homeVictory, color = 'blue', alpha = 0.3)

print(np.mean(diffLineScore))
print(np.std(diffLineScore))

