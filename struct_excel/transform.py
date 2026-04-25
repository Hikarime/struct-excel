# TODO: Add transformation for `student`,
# `course`, `session`, `supervisor`,
# and `enrollment`.

from models import Course, Enrollment, RawRow, Session, Student, Supervisor


def to_supervisor(raw: list[RawRow]) -> list[Supervisor]:
    return []


def to_course(raw: list[RawRow]) -> list[Course]:
    return []


def to_student(raw: list[RawRow], supervisors: list[Supervisor]) -> list[Student]:
    return []


def to_session(raw: list[RawRow], courses: list[Course]) -> list[Session]:
    return []


def to_enrollment(
    raw: list[RawRow], students: list[Student], sessions: list[Session]
) -> list[Enrollment]:
    return []
