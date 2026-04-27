from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class SessionMode(Enum):
    ONLINE = "online"
    OFFLINE = "offline"


class Sector(Enum):
    GOVERNMENT = "Government"
    PRIVATE = "Private"
    STUDENT = "Student"


class PaymentStatus(Enum):
    PAID = "PAID"
    PENDING = "PENDING"


@dataclass
class Student:
    student_id: int
    full_name: str
    email: str
    gender: Gender
    it_background: bool
    experience_min_years: int
    experience_max_years: int
    sector: Sector
    supervisor_id: int | None
    company: str
    job_title: str | None
    country: str
    phone: str


@dataclass
class Course:
    course_id: int
    course_name: str


@dataclass
class Session:
    session_id: int
    course_id: int
    start_datetime: datetime
    end_datetime: datetime
    mode: SessionMode
    duration: float


@dataclass
class Supervisor:
    supervisor_id: int
    full_name: str
    email: str


@dataclass
class Enrollment:
    enrollment_id: int
    student_id: int
    session_id: int
    reg_date: datetime
    completed: bool
    payment_status: PaymentStatus
    exception: str | None


@dataclass
class RawRow:
    reg_date: datetime
    student_full_name: str
    student_email: str
    student_company: str
    student_job_title: str | None
    country: str
    exception: str | None
    phone: str
    course: str
    gender: str
    sector: str
    supervisor_name: str | None
    supervisor_email: str | None
    it_background: str | None
    experience: str | None
    completed: str | None
    payment_status: str | None


@dataclass
class CourseParseResult:
    datetime_range: list[tuple[datetime, datetime]]
    mode: SessionMode
    course_name: str
    duration: float
