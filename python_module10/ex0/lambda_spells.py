def artifact_sorter(
        artifacts: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(
        mages: list[dict[str, int]],
        min_power: int) -> list[dict[str, int]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: '* ' + spell + ' *', spells))


def mage_stats(mages: list[dict[str, int]]) -> dict[str, int | float]:
    return {
            "max_power": max(mages, key=lambda mage: mage['power'])['power'],
            "min_power": min(mages, key=lambda mage: mage['power'])['power'],
            "avg_power": round(sum(map(lambda mage: mage['power'], mages)) /
                               len(mages), 2)
            }


if __name__ == "__main__":
    artifacts: list[dict[str, str | int]] = [
        {'name': 'Crystal Orb', 'power': 85},
        {'name': 'Fire Staff', 'power': 92}]
    spells = ['fireball', 'heal', 'shield']
    print("\nTesting artifact sorter...")
    fire_staff, crystal_orb = artifact_sorter(artifacts)
    print(f"{fire_staff['name']} ({fire_staff['power']} power) comes before ",
          f"{crystal_orb['name']} ({crystal_orb['power']} power)")
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))
