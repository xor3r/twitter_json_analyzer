# twitter_json_analyzer   :sparkles:
Analyzes Twitter's JSON file and its structure using pandas

## Getting started   :unlock:
To work with my project you need to:
1. Download all the files or clone this repo into chosen directory.
2. Create text file __KEYS.txt__ and put your Twitter's API keys into it, separating each of them with a newline.

### Prerequisites   :mag_right:
For python 3.x: `pip3 install -r requirements.txt`\
For python 2.x `pip install -r requirements.txt`

### Usage   :computer_mouse:
1. In the downloaded/cloned directory, open the terminal and hit: `python analyze.py`\
2. Follow the instructions on the screen. To quit - type _q_ in any prompt.\
   * Enter a valid Twitter user's username.
   * Choose how many friends to include into JSON file (between 1 and 20).
   * Choose whether to show the JSON file's structure (hit _y_ or _n_).
   * Then, to show available columns' names, hit _y_ (_n_ otherwise).
   * Choose which columns to include into generated DataFrame (hit _Enter_ when finished).
#### Workflow   :hourglass_flowing_sand:
A process starts as shown below:\
![1](/screenshots/workflow.gif)\
Then you can display all columns' names:\
![2](/screenshots/columnnames.gif)\
Now you can specify the names and get a desired result.\
![3](/screenshots/Inked.jpg)\
It depends on how many friends and columns you've chosen to display:\
![4](/screenshots/choice.png)

## Built With   :fuelpump:
* [Pandas](https://pandas.pydata.org/)

## Warning   :warning:
This app was tested only in main cases, so some problems may occur.\
In case of problems, write comments underneath this projects of send a message to me directly: `mishanya@protonmail.com`\
