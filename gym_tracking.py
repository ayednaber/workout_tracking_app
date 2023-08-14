import csv
from workouts import *
from datetime import date

push = open("./ppl_spreadsheets/Push.csv", 'w', newline='')
writerPush = csv.writer(push)

pull = open("./ppl_spreadsheets/Pull.csv", 'w', newline='')
writerPull = csv.writer(pull)

legs = open("./ppl_spreadsheets/Legs.csv", 'w', newline='')
writerLegs = csv.writer(legs)

# currentYear = date.today().strftime("%Y")
currentYear = "2022"
dayMonthOfWorkout = input("Enter date of workout (day month): ")
dateOfWorkout = dayMonthOfWorkout + " " + currentYear
workoutType = input("Choose your workout: ")

def writeWorkouts(workoutType):
    writeDateHeader()
    for workout in workoutType:
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

            if (workoutType == pushWorkouts):
                writerPush.writerow([workout, weight_output, rep_output])
            elif (workoutType == pullWorkouts):
                writerPull.writerow([workout, weight_output, rep_output])
            else:
                writerLegs.writerow([workout, weight_output, rep_output])

def writeDateHeader():
    if (workoutType == "push"):
        writerPush.writerow([dateOfWorkout, "Weight", "Reps"])
    elif (workoutType == "pull"):
        writerPull.writerow([dateOfWorkout, "Weight", "Reps"])
    else:
        writerLegs.writerow([dateOfWorkout, "Weight", "Reps"])

while workoutType != "end":
    if workoutType == "push":
        writeWorkouts(pushWorkouts)
    elif workoutType == "pull":
        writeWorkouts(pullWorkouts)
    else:
        writeWorkouts(legWorkouts)
    workoutType = input("Enter another workout type or type `end` to finish: ")

