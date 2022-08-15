import os
from Google import Create_Service
from project_secrets import SPREADSHEET_ID
from workouts import *
from datetime import date

currentYear = date.today().strftime("%Y")
dayMonthOfWorkout = input("Enter date of workout (day month): ")
dateOfWorkout = dayMonthOfWorkout + " " + currentYear

workouts = []

def writeWorkouts(workoutType):
    if workoutType == "push":
        listOfWorkouts = pushWorkouts
    elif workoutType == "pull":
        listOfWorkouts = pullWorkouts
    else:
        listOfWorkouts = legWorkouts
    
    workouts.append(tuple([])) # Making space
    workouts.append(tuple([dateOfWorkout, "Weights", "Reps"]))
    for workout in listOfWorkouts:
            no_of_sets = input("Number of sets for " + workout + ": ")
            if no_of_sets == "s":
                continue
            weight_output = no_of_sets + " sets ("
            rep_output = ""
            weights_played = input("Enter your weights separated by a space: ")
            reps_played = input("Enter your reps separated by a space: ")
            if " " in weights_played:
                w = weights_played.split(" ")
                r = reps_played.split(" ")
                for j in range(len(w)):
                    if j != int(no_of_sets) - 1:
                        weight_output += w[j] + ", "
                        rep_output += r[j] + ", "
                    else:
                        weight_output += w[j] + ")"
                        rep_output += r[j]
            else:
                weight_output += weights_played + ")"
                r = reps_played.split(" ")
                for j in range(len(r)):
                    if j != int(no_of_sets) - 1:
                        rep_output += r[j] + ", "
                    else:
                        rep_output += r[j]

            workouts.append(tuple([workout, weight_output, rep_output]))
    return workouts

workout_type = input("Enter your workout (push, pull, legs):  ")

AUTH_JSON = 'client_secret.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = [
'https://www.googleapis.com/auth/spreadsheets'
]

service = Create_Service(AUTH_JSON, API_NAME, API_VERSION, SCOPES)

mySpreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute() # Getting our spreadsheet object

push_worksheet_name = 'Push!'
push_cell_range_insert = 'A364'
pull_worksheet_name = 'Pull!'
pull_cell_range_insert = 'A367'
legs_worksheet_name = 'Legs!'
legs_cell_range_insert = 'A238'
values = tuple(writeWorkouts(workout_type))

value_range_body = {
    'majorDimension': 'ROWS',
    'values': values
}

# Deciding which worksheet to append to
if (workout_type == "push"):
    workout_range = push_worksheet_name + push_cell_range_insert
elif (workout_type == "pull"):
    workout_range = pull_worksheet_name + pull_cell_range_insert
else:
    workout_range = legs_worksheet_name + legs_cell_range_insert

service.spreadsheets().values().append(
    spreadsheetId=SPREADSHEET_ID,
    valueInputOption='USER_ENTERED',
    range=workout_range,
    body=value_range_body
).execute()
