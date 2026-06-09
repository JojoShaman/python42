import random

achievements = [
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer',
    ]


def gen_player_achievements() -> set[str]:
    random_number = random.randint(6, 10)
    player_achievements = random.sample(achievements, random_number)
    return set(player_achievements)


if __name__ == "__main__":
    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()
    all_achievements = Alice | Bob | Charlie | Dylan
    common = Alice & Bob & Charlie & Dylan
    print("=== Achievement Tracker System ===\n")

    print(f"Player Alice: {Alice}\n" +
          f"Player Bob: {Bob}\n" +
          f"Player Charlie: {Charlie}\n" +
          f"Player Dylan: {Dylan}\n")

    print(f"\nAll distinct achievements: {all_achievements}\n\n" +
          f"Common achievements: {common}\n\n" +
          f"Only Alice has: {Alice - (Bob | Charlie | Dylan)}\n" +
          f"Only Bob has: {Bob - (Alice | Charlie | Dylan)}\n" +
          f"Only Charlie has: {Charlie - (Alice | Bob | Dylan)}\n" +
          f"Only Dylan has: {Dylan - (Alice | Bob | Charlie)}\n\n" +
          f"Alice is missing: {set(achievements) - Alice}\n" +
          f"Bob is missing: {set(achievements) - Bob}\n" +
          f"Charlie is missing: {set(achievements) - Charlie}\n" +
          f"Dylan is missing: {set(achievements) - Dylan}\n")
