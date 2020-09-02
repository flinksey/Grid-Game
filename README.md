### Goal: Create a grid game that's sort of like Candy Crush
#### Start Date: Aug. 19, 2020
#### Projected End Date: Sept. 6, 2020

#### Ello! This is where I'm currently working on an old project (modified) from first semester of last year. It was a grid game implemented in Python. Last year, it took me four days of going to sleep and waking up still mentally debugging to get it to about 60% functionality. I know it'll take me longer to get it up and running this time around but, hey, it'll be fun!

#### How does this game work? \[note: subject to change\]
Based on user input, an MxN grid is created with each "cell" displaying a random number within the range (0,K). The user must input a set of coordinates (x,y) corresponding to a particular cell they think has at least 2 adjacent matches (ex. Cell A displays the integer 2. If at least 2 cells adjacent to Cell A also display 2, then the cell has matches). If there is a match, the selected cell and all adjacent cells (including those adjacent to the cells adjacent to the selected) will be removed and the grid fixes itself accordingly (remaining cells shift to adapt). Every time a match is cleared, the user is awarded points. 

User can choose to end the game at any point. Once the game ends, the accumulated score and the record of greatest match cleared are displayed. 
