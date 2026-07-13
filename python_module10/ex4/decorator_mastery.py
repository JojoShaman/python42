from time import time, sleep
from collections.abc import Callable
from typing import Any
from functools import wraps


def spell_timer(
        func: Callable[..., str]) -> Callable[..., Any]:
    @wraps(func)
    def timer(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return timer


@spell_timer
def fireball() -> str:
    sleep(0.5)
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def power_check(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power', args[-1])
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return power_check
    return decorator


class CastError(Exception):
    pass


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def call_func(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                sleep(0.5)
                try:
                    result = func(*args, **kwargs)
                    return result
                except CastError:
                    if i != max_attempts:
                        print("Spell failed, retrying... ",
                              f"(attempt {i}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after "
                                f"{max_attempts} attempts")
        return call_func
    return decorator


@retry_spell(max_attempts=3)
def spell(error: bool = True) -> str:
    if error:
        raise CastError
    return "Waaaaaaagh spelled !"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            if all(c.isalpha() or c.isspace() for c in name):
                return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")
    print("\nTesting retrying spell...")
    print(spell(True))
    print(spell(False))
    print("\nTesting MageGuild...")
    sleep(1)
    print(MageGuild.validate_mage_name("Phoenix"))
    sleep(0.3)
    print(MageGuild.validate_mage_name("Alex123"))
    sleep(0.3)
    print(MageGuild().cast_spell('Lighting', 15))
    sleep(2)
    print(MageGuild().cast_spell('Lighting', 9))
