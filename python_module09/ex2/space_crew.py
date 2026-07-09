from pydantic import BaseModel, ValidationError, Field, model_validator
from enum import Enum
from typing_extensions import Self
from datetime import datetime


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_rules(self) -> Self:
        errors = []
        member_check = False
        if not self.mission_id.startswith('M'):
            errors.append('Mission ID must start with "M"')
        for member in self.crew:
            if member.rank == Rank.captain or member.rank == Rank.commander:
                member_check = True
        if not member_check:
            errors.append('Must have at least one Commander or Captain')
        if self.duration_days > 365:
            above_5 = 0
            for member in self.crew:
                if member.years_experience > 5:
                    above_5 += 1
            if above_5 < len(self.crew) / 2:
                errors.append("Long missions (> 365 days) "
                              "need 50%% experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                errors.append("All crew members must be active")
        if errors:
            raise ValueError('\n'.join(errors))
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        Connor = CrewMember(
            member_id='CM041',
            name='Sarah Connor',
            rank=Rank.commander,
            age=50,
            specialization='Mission Command',
            years_experience=25,
            is_active=True
        )
        Smith = CrewMember(
            member_id='CM042',
            name='John Smith',
            rank=Rank.lieutenant,
            age=47,
            specialization='Navigation',
            years_experience=18,
            is_active=True
        )
        Johnson = CrewMember(
            member_id='CM043',
            name='Alice Johnson',
            rank=Rank.officer,
            age=55,
            specialization='Engineering',
            years_experience=22,
            is_active=True
        )

        MISSION_1 = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date=datetime.fromisoformat('2024-09-18T00:00:00'),
            duration_days=900,
            crew=[
                Connor,
                Smith,
                Johnson,
            ],
            mission_status='planned',
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {MISSION_1.mission_name}")
        print(f"ID: {MISSION_1.mission_id}")
        print(f"Destination: {MISSION_1.destination}")
        print(f"Duration: {MISSION_1.duration_days} days")
        print(f"Budget: ${MISSION_1.budget_millions}M")
        print(f"Crew size: {len(MISSION_1.crew)}")
        print("Crew members:")
        for member in MISSION_1.crew:
            print(f"{member.name} ({member.rank}) - {member.specialization}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
    print("\n=========================================")
    try:
        Connor = CrewMember(
            member_id='CM041',
            name='Sarah Connor',
            rank=Rank.officer,
            age=50,
            specialization='Mission Command',
            years_experience=25,
            is_active=True
        )
        Smith = CrewMember(
            member_id='CM042',
            name='John Smith',
            rank=Rank.lieutenant,
            age=47,
            specialization='Navigation',
            years_experience=18,
            is_active=True
        )
        Johnson = CrewMember(
            member_id='CM043',
            name='Alice Johnson',
            rank=Rank.officer,
            age=55,
            specialization='Engineering',
            years_experience=22,
            is_active=True
        )

        MISSION_2 = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date=datetime.fromisoformat('2024-09-18T00:00:00'),
            duration_days=900,
            crew=[
                Connor,
                Smith,
                Johnson,
            ],
            mission_status='planned',
            budget_millions=2500.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
