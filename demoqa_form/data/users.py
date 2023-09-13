from dataclasses import dataclass
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str
