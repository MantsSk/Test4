# 1. Create a list named `participants` with the names of five participants. For example: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
participants = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 2. Create a tuple named `games` with the names of three games. For example: ('Football', 'Tetris', 'Tennis')
games = ("Chess", "Mario Kart", "Basketball")

# 3. Create a dictionary named `scores` where keys are participants and values are dictionaries containing scores for each game. For example:
# {'Alice': {'Chess': 98, 'Mario Kart': 77, 'Basketball': 94}, 
# 'Bob': {'Chess': 69, 'Mario Kart': 77, 'Basketball': 81}, 
# 'Charlie': {'Chess': 78, 'Mario Kart': 77, 'Basketball': 82}, 
# 'David': {'Chess': 52, 'Mario Kart': 78, 'Basketball': 77}, 
# 'Eve': {'Chess': 93, 'Mario Kart': 89, 'Basketball': 86}}

import random

scores = {}

for participant in participants:
    game_dict = {}
    
    for game in games:
        game_dict[game] = random.randint(50, 100)

    scores[participant] = game_dict

# 4. Create a set named `winners` to store the winners of each game.
winners = set()

# 5. Calculate and print the average score for each participant across all games. Example output to terminal: 'Average score for Alice: 89.66666666667'
average_scores = {}
for participant in participants:
    total_score = sum(scores[participant].values())
    average_score = total_score / len(games)
    average_scores[participant] = average_score
    print(f"Average score for {participant}: {average_score}")

# 6. Determine and print the winner for each game based on the highest average score. Add the winner to your winners' set. Example output to terminal: 'Winner for Chess: Alice'
game_scores = {}
for game in games:
    for participant in participants:
        game_scores[participant] = scores[participant][game]
    
    winner = max(game_scores, key=game_scores.get)
    winners.add(winner)
    print(f"Winner for {game}: {winner}")    

# 7. Create a variable named `new_participant` with the information for a new participant. For example: 
#{ 
# 'name': 'Jonas',
# 'scores': {
#   'Chess': 12,
#   'Mario Kart': 11,
#   'Basketball": 44
#   }
# }

new_participant_name = 'Jonas'

game_dict = {}
for game in games:
        game_dict[game] = random.randint(50, 100)

new_participant = {
    'name': new_participant_name,
    'scores': game_dict
} 

# 8. Add the new participant's name to `participants`, and scores to the `scores` dictionary.
participants.append(new_participant["name"])
scores[new_participant["name"]] = new_participant["scores"]

# 9. Print the final scores of all participants of each game. Example output to terminal: 
# Final scores:
# Alice: {'Chess': 98, 'Mario Kart': 77, 'Basketball': 99}
# ...
print("\nFinal Scores:")
for participant, participant_scores in scores.items():
    print(f"{participant}: {participant_scores}")

# 10.  Print all the winners. Example output to terminal: 
# Winners:
# Alice
# Eve
print("\nWinners:")
for winner in winners:
    print(f"{winner}")