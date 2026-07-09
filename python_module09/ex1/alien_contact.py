from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from typing_extensions import Self
from enum import Enum


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1400)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact_id(self) -> Self:
        errors = []
        if not self.contact_id.startswith('AC'):
            errors.append('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.physical and not self.is_verified:
            errors.append("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic and
                self.witness_count < 3):
            errors.append("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            errors.append(
                "Strong signals (> 7.0) should include received messages")
        if errors:
            raise ValueError('\n'.join(errors))
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        contact_one = AlienContact(
            contact_id='AC_2024_001',
            timestamp=datetime.fromisoformat('1970-01-01T00:00:01'),
            location='Area 51, Nevada',
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received='Greetings from Zeta Reticuli'
        )
        print("Valid contact report:")
        print(f"ID: {contact_one.contact_id}")
        print(f"Type: {contact_one.contact_type.name}")
        print(f"Location: {contact_one.location}")
        print(f"Signal: {contact_one.signal_strength}/10")
        print(f"Duration: {contact_one.duration_minutes} minutes")
        print(f"Witnesses: {contact_one.witness_count}")
        print(f"Message: '{contact_one.message_received}'")
    except ValidationError as e:
        print("\n======================================")
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
    try:
        contact_two = AlienContact(
            contact_id='2024_001',
            timestamp=datetime.fromisoformat('1970-01-01T00:00:02'),
            location='Area 51, Nevada',
            contact_type=ContactType.telepathic,
            signal_strength=15,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli'
        )
    except ValidationError as e:
        print("\n======================================")
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))
