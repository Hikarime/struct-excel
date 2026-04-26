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
    supervisor_id: int


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
    payment_status: str
    exception: str


@dataclass
class RawRow:
    reg_date: datetime
    student_full_name: str
    student_email: str
    student_company: str
    student_job_title: str
    country: str
    exception: str
    phone: str
    course: str
    gender: str
    sector: str
    supervisor_name: str
    supervisor_email: str
    it_background: str
    experience: str
    completed: str
    payment_status: str


@dataclass
class CourseParseResult:
    datetime_range: list[tuple[datetime, datetime]]
    mode: SessionMode
    course_name: str
    duration: float
