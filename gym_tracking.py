import csv
from workouts import *

push = open("../../Desktop/Online Work/Gym_Tracking/Push.csv", 'w', newline='')
writerPush = csv.writer(push)

pull = open("../../Desktop/Online Work/Gym_Tracking/Pull.csv", 'w', newline='')
writerPull = csv.writer(pull)

legs = open("../../Desktop/Online Work/Gym_Tracking/Legs.csv", 'w', newline='')
writerLegs = csv.writer(legs)

workoutType = input("Choose your workout: ")

while workoutType != "end":
    if workoutType == "push":
        for workout in pushWorkouts:
            no_of_sets = input("Number of sets for " + workout + ": ")
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

            writerPush.writerow([workout, weight_output, rep_output])

    elif workoutType == "pull":
        for workout in pullWorkouts:
            no_of_sets = input("Number of sets for " + workout + ": ")
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

            writerPull.writerow([workout, weight_output, rep_output])
    else:
        for workout in legWorkouts:
            no_of_sets = input("Number of sets for " + workout + ": ")
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

            writerLegs.writerow([workout, weight_output, rep_output])
    workoutType = input("Enter another workout type or type `end` to finish: ")
