################################
# Pema Kinzang Choden
# 1ICE
# Student ID: 02230220
################################
# REFERENCES
# https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/
# https://realpython.com/python-rock-paper-scissors/
# https://youtu.be/Qcefu1jVPds?si=8tDDouZNdum88OL-
################################
# SOLUTION
# Your Solution Score:
# 49894
################################

# Read the input.txt file
def read_input(input_file):
    rounds = []
    with open(input_file,'r') as file:
        for i in file: 
            opponent_choice, outcome = i.split()
            rounds.append((opponent_choice, outcome))
    return rounds

# Calculate the total score
def calculate_score(rounds):
    total_score = 0
    for opponent_choice, outcome in rounds:
        if outcome == 'X': 
            # Need to lose(0)
            if opponent_choice == 'A': #(rock)
                total_score += 3  # Choose Scissors(3) # total score (0+3)
            elif opponent_choice == 'B':
                total_score += 1  # Choose Rock(1) #total score (0+1)
            elif opponent_choice == 'C':
                total_score += 2  # Choose Paper(2) # total score (0+2)
        elif outcome == 'Y': 
            # Need to draw (3)
            if opponent_choice == 'A':
                total_score += 4  # Choose Rock(1) #total score (3+1)
            elif opponent_choice == 'B':
                total_score += 5  # Choose Paper(2) # total score (3+2)
            elif opponent_choice == 'C':
                total_score += 6  # Choose Scissors(3) #total score (3+3)
        elif outcome == 'Z':
            # Need to win (6)
            if opponent_choice == 'A':
                total_score += 8  # Choose Paper(2) #total score (6+2)
            elif opponent_choice == 'B':
                total_score += 9  # Choose Scissors(3) #total score (6+3)
            elif opponent_choice == 'C':
                total_score += 7  # Choose Rock(1) # total score (6+1)
    print(f"The total score is : {total_score} ")

input_file= "CSF101-CAP/input_0_cap1.txt"
calculate_score(read_input(input_file))

