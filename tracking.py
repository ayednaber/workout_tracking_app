from workouts import *
from datetime import date

currentYear = date.today().strftime("%Y")
dayMonthOfWorkout = input("Enter date of workout (day month): ")
dateOfWorkout = dayMonthOfWorkout + " " + currentYear
# workoutType = input("Choose your workout: ")

workouts = []

def writeWorkouts(workoutType):
    if workoutType == "push":
        listOfWorkouts = pushWorkouts
    elif workoutType == "pull":
        listOfWorkouts = pullWorkouts
    else:
        listOfWorkouts = legWorkouts

    workouts.append(tuple([dateOfWorkout, "Weights", "Reps"]))
    for workout in listOfWorkouts:
            no_of_sets = input("Number of sets for " + workout + ": ")
            if no_of_sets == "s":
                continue
            weight_output = no_of_sets + " sets ("
            rep_output = ""
            weights_played = input("Enter your weights separated by a space: ")
            reps_played = input("Enter your reps separated by a space: ")
            w = weights_played.split(" ")
            r = reps_played.split(" ")
            for j in range(len(w)):
                if j != int(no_of_sets) - 1:
                    weight_output += w[j] + ", "
                    rep_output += r[j] + ", "
                else:
                    weight_output += w[j] + ")"
                    rep_output += r[j]

            workouts.append(tuple([workout, weight_output, rep_output]))
    return workouts

# def writeDateHeader():
#     if (workoutType == "push"):
#         writerPush.writerow([dateOfWorkout, "Weight", "Reps"])
#     elif (workoutType == "pull"):
#         writerPull.writerow([dateOfWorkout, "Weight", "Reps"])
#     else:
#         writerLegs.writerow([dateOfWorkout, "Weight", "Reps"])

while workoutType != "end":
    if workoutType == "push":
        writeWorkouts(pushWorkouts)
        print(workouts)
    elif workoutType == "pull":
        writeWorkouts(pullWorkouts)
    else:
        writeWorkouts(legWorkouts)
        print(workouts)
    workoutType = input("Enter another workout type or type `end` to finish: ")

