from typing import Generator
import random


players = [
    "Alice", "Bob", "Charlie", "Dylan", "Emma",
    "Felix", "John", "Hugo", "Iris", "Jules",
    "Karim", "Léa", "Marc", "Nina"
]


events = [
    "run", "eat", "sleep", "grab", "move", "swim",
    "release", "jump", "climb", "throw", "catch",
    "hide", "fight", "heal", "build"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(events))


def consume_event(
        event_tuple: list[tuple[str, str]]) -> Generator[tuple[str, str]]:
    while event_tuple:
        event = random.choice(event_tuple)
        event_tuple.remove(event)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    ten_tuples = []
    for x in range(1000):
        result = next(event_generator)
        print(f"Event {x}: Player {result[0]} did action {result[1]}")
    for x in range(10):
        result = next(event_generator)
        ten_tuples.append((result[0], result[1]))
    print("Built list of 10 events: ", ten_tuples)
    for element in consume_event(ten_tuples):
        print("Got event from list:", element)
        print("Remains in list: ", ten_tuples)
