from dataclasses import dataclass
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
    id: int = uuid4().int
    date: str = datetime.now().strftime("%Y-%m-%d")
    entry_type: EntryType

    def __init__(self, date: str = None):
        if date:
            self.date = date

    def add_notes(self, notes: str):
        self.notes = notes

    @abstractmethod
    def description(self):
        """Return a description of the entry."""

    @abstractmethod
    def adapt(self) -> str:
        """Return a string representation of the entry."""


@dataclass
class MedicationEntry(Entry):
    id: str = str(uuid4())
    date: str = datetime.now().strftime("%Y-%m-%d")
    entry_type: EntryType = EntryType.MEDICATION
    medication_name: str = ""
    dosage: str = ""
    frequency: str = ""
    duration: str = ""
    route: str = ""
    reason: str = ""

    def description(self):
        attr_list = [self.medication_name, self.dosage,
                     self.frequency, self.duration, self.route, self.reason]
        attr_list = [attr for attr in attr_list if attr]
        return ", ".join(attr_list)

    def adapt(self):
        return f"({self.id};{self.date};{self.entry_type.name};{self.medication_name};{self.dosage};{self.frequency};{self.duration};{self.route};{self.reason})"


@dataclass
class HealthDataEntry(Entry):
    id: str = str(uuid4())
    date: str = datetime.now().strftime("%Y-%m-%d")
    entry_type: EntryType = EntryType.HEALTH_DATA
    weight: str = ""
    height: str = ""
    blood_pressure: str = ""
    heart_rate: str = ""
    respiratory_rate: str = ""
    temperature: str = ""

    def description(self):
        attr_list = [self.weight, self.height,
                     self.blood_pressure, self.heart_rate, self.respiratory_rate, self.temperature]
        attr_list = [attr for attr in attr_list if attr]
        return ", ".join(attr_list)

    def adapt(self):
        return f"({self.id};{self.date};{self.entry_type.name};{self.weight};{self.height};{self.blood_pressure};{self.heart_rate};{self.respiratory_rate};{self.temperature})"


@dataclass
class DoctorVisitEntry(Entry):
    id: str = str(uuid4())
    date: str = datetime.now().strftime("%Y-%m-%d")
    entry_type: EntryType = EntryType.DOCTOR_VISIT
    reason: str = ""
    diagnosis: str = ""
    treatment: str = ""

    def description(self):
        attr_list = [self.reason, self.diagnosis, self.treatment]
        attr_list = [attr for attr in attr_list if attr]
        return ", ".join(attr_list)

    def adapt(self):
        return f"({self.id};{self.date};{self.entry_type.name};{self.reason};{self.diagnosis},{self.treatment})"


class HealthcareWorker():
    def __init__(self, name, role, address, phone_number, email):
        self.name = name
        self.role = role
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} {self.role}"
