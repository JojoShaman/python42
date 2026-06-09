from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = None


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(station_id="ISS001",
                               name="International Space Station",
                               crew_size=6,
                               power_level=85.5,
                               oxygen_level=92.3,
                               last_maintenance="1970-01-01T00:00:01",
                               is_operational=True)
        print("Valid station created:")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Last maintenant: {station.last_maintenance}")
    print("Status: "
          f"{"Operational" if station.is_operational else "Off-nominal"}\n")
    print("========================================")
    try:
        invalid = SpaceStation(station_id="ISS001",
                               name="International Space Station",
                               crew_size=30,
                               power_level=85.5,
                               oxygen_level=92.3,
                               last_maintenance="1970-01-01T00:00:01",
                               is_operational=True)
        print("Valid station created:")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
