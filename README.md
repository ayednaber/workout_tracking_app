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

### Method 2: Outputting Directly to Google Sheets
Also in this repository, you can see the `workout_tracking.py` file, in which I implemented this method.

I import my project secrets (spreadsheet ID, and client secret for OAuth 2.0 authentication), and then I also have the same `writeWorkouts` method in this file as well.

I have made some differences to how this version of the program behaves, where it prompts the user for the date and type of the workout they want to track.
Next, depending on the type of workout entered, it would start cycling through all of the appropriate workouts and asks **for each exercise:**
- Number of sets
- Weights played
- Number of reps

Once the list of workouts is completed, then it will output to the Google sheet directly, and which worksheet in particular would depend on the user entered value.

#### Cycling through Workouts
If there is a workout that you skipped, when prompted for the number of sets, enter `s`, and it will go to the next workout.

## Opportunities for Expansion
- Create a Front-end application to allow for more workout customization.