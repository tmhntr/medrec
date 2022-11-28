from dataclasses import dataclass
from enum import Enum, auto
# import library for dates
from datetime import datetime


# an enum class for the different types of entries
class EntryType(Enum):
    # a normal entry
    NORMAL = auto()
    # an entry that is a subtask of another entry
    SUBTASK = auto()
    # an entry that is a subtask of another entry that is a subtask of another entry
    SUBSUBTASK = auto()

# an enum class for the different types of healthcare workers
class HealthcareWorkerType(Enum):
    # a doctor
    DOCTOR = auto()
    # a nurse
    NURSE = auto()
    # a technician
    TECHNICIAN = auto()
    # a pharmacist
    PHARMACIST = auto()

# a dataclass for medication entries
@dataclass
class MedicationEntry:
    # the name of the medication
    name: str
    # the dosage of the medication
    dosage: str
    # the frequency of the medication
    frequency: str
    # the duration of the medication
    duration: str
    # the route of the medication
    route: str
    # the reason for the medication
    reason: str

@dataclass
class HealthcareWorkers:
    name: str
    role: HealthcareWorkerType

# a dataclass for health data
@dataclass
class HealthData:
    weight: float = None
    height: float = None
    blood_pressure: str = None
    heart_rate: int = None
    respiratory_rate: int = None
    temperature: float = None

# a function to get todays date as a string
def get_date() -> str:
    return datetime.now().strftime("%m/%d/%Y")

@dataclass
class Entry:
    date: str = get_date()
    description: str = ""
    entry_type: str = EntryType.NORMAL
    attachments: list[str] = None
    healthcare_workers: list[HealthcareWorkers] = None
    medications: list[MedicationEntry] = None
    health_data: HealthData = None


    def __str__(self):
        return f"Date: {self.date}\nDescription: {self.description}\nEntry Type: {self.entry_type}\nAttachments: {self.attachments}\nHealthcare Workers: {self.healthcare_workers}\nMedications: {self.medications}\nHealth Data: {self.health_data}"

