# Gym Tracking App

## Why I Created this App
As of February 2022, I started working out at the gym consistently, and I was manually tracking my workouts by entering them on a Google sheet. With time, this process has become very repetitive, and I found myself wasting much time on this process. Thus, I decided to automate it.

## How It Works

### Method 1: CSV File Output
In the `workouts.py` file, I defined some preset workout routines that I usually do at the gym, which can be split into three main categories; Push, Pull, and Legs. In `workouts.py`, each workout day has its own list of workouts.

These lists are then imported into the main file called `gym_tracking.py`. In that file, the program through each corresponding workout list depending on the input that the user entered.

It prompts the user to enter **for each exercise:**
- Number of sets
- Weights played
- Number of reps

Once that is complete, then it prompts the user to either **continue with a new workout** or simply type **end** to terminate the program.

Currently, the program is outputting these formatted fields onto CSV files using the csv library.

## Opportunities for Expansion
- Outputting directly onto the **Google Sheet** that I track my workouts on.
- Create a Front-end application (using React.js) to allow for more workout customization.