import random

players = [
    'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
    'Gregory', 'john', 'kevin', 'Liam'
]

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    only_capitalized = [name for name in players
                        if name == name.capitalize()]
    capitalized = [name.capitalize() for name in players]
    score = {name: random.randint(0, 1000) for name in players}
    average_score = round(sum(score.values()) / len(score), 2)
    high_score = {name: points for name, points in score.items()
                  if points > 400}
    print(f"Initial list of players: {players}\n")
    print(f"New list with all names capitalized: {capitalized}\n")
    print(f"New list of capitalized names only: {only_capitalized}\n")
    print(f"Score dict: {score}")
    print(f"Score average is {average_score}")
    print(f"High scores: {high_score}")
