import sys

if __name__ == "__main__":
    scores_processed = []
    total_player = len(sys.argv) - 1
    print("=== Player Score Analytics ===")
    for i in sys.argv[1:]:
        try:
            scores_processed.append(int(i))
        except ValueError:
            print(f"Invalid parameter: '{i}'")
            total_player = 0

    if total_player > 0:
        print(f"Scores processed: {scores_processed}",
              f"Total players: {total_player}",
              f"Total score: {sum(scores_processed)}",
              f"Average score: {round(sum(scores_processed)/total_player, 1)}",
              f"High score: {max(scores_processed)}",
              f"Low score: {min(scores_processed)}",
              f"Score range: {max(scores_processed) - min(scores_processed)}")

    else:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
