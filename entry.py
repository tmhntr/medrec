from enum import Enum, auto
# import library for dates
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4
from abc import ABC, abstractmethod

# an enum class for the different types of entries
class EntryType(Enum):
    MEDICATION = auto()
    HEALTH_DATA = auto()
    DOCTOR_VISIT = auto()


class Entry(ABC):
    id: UUID = uuid4()
    date: str = datetime.now().strftime("%Y-%m-%d")
    description: str = ""
    entry_type: EntryType
    attachments: str = None
    healthcare_workers = []
    notes: str = None

    def add_notes(self, notes: str):
        self.notes = notes


class MedicationEntry(Entry):
    entry_type: str = EntryType.MEDICATION

    def __init__(self, name, dosage, frequency, duration, route, reason):
        super().__init__()
        self.medication_name = name
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration
        self.route = route
        self.reason = reason
        self.notes = None
        self.description = ", ".join([self.medication_name, self.dosage, self.frequency, self.duration, self.route, self.reason])



    def __str__(self):
        return f"{self.medication_name} {self.dosage} {self.frequency} {self.duration} {self.route} {self.reason}"

class HealthDataEntry(Entry):
    def __init__(self, weight, height, blood_pressure, heart_rate, respiratory_rate, temperature):
        super().__init__()
        self.weight = weight
        self.height = height
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.respiratory_rate = respiratory_rate
        self.temperature = temperature

    def __str__(self):
        return f"{self.weight} {self.height} {self.blood_pressure} {self.heart_rate} {self.respiratory_rate} {self.temperature}"

class DoctorVisitEntry(Entry):
    def __init__(self, reason, diagnosis, treatment):
        super().__init__()
        self.reason = reason
        self.diagnosis = diagnosis
        self.treatment = treatment

    def __str__(self):
        return f"{self.reason} {self.diagnosis} {self.treatment}"

class HealthcareWorker():
    def __init__(self, name, role, address, phone_number, email):
        self.name = name
        self.role = role
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} {self.role}"
    