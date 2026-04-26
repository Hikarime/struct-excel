# TODO: Add transformation for `student`,
# `course`, `session`, `supervisor`,
# and `enrollment`.

import logging
from models import Course, Enrollment, RawRow, Session, Student, Supervisor
from parser import parse_course_session

logger = logging.getLogger(__name__)


def to_supervisor(raw: list[RawRow]) -> list[Supervisor]:
    return []


def to_course(raw: list[RawRow]) -> list[Course]:
    courses: list[Course] = []
    duplicate = set()

    for row in raw:
        parsed = parse_course_session(row.course)
        course_name = parsed.course_name
        if course_name in duplicate:
            continue
        duplicate.add(course_name)

        courses.append(
            Course(
                course_id=len(courses) + 1,
                course_name=course_name,
            )
        )

    return courses


def to_student(raw: list[RawRow], supervisors: list[Supervisor]) -> list[Student]:
    return []


def to_session(raw: list[RawRow], courses: list[Course]) -> list[Session]:
    sessions: list[Session] = []
    session_id = 1
    seen = set()

    for entry in raw:
        try:
            course_session = parse_course_session(entry.course)
            existed_course = _select_course_by_name(courses, course_session.course_name)
        except ValueError as e:
            logger.warning(f"skip invalid session: {entry.course}, err: {e}")
            continue

        for start, end in course_session.datetime_range:
            dedup_key = (
                existed_course.course_id,
                start,
                end,
                course_session.duration,
            )
            if dedup_key in seen:
                continue
            seen.add(dedup_key)

            sessions.append(
                Session(
                    session_id=session_id,
                    course_id=existed_course.course_id,
                    start_datetime=start,
                    end_datetime=end,
                    mode=course_session.mode,
                    duration=course_session.duration,
                )
            )
            session_id += 1

    return sessions


def to_enrollment(
    raw: list[RawRow], students: list[Student], sessions: list[Session]
) -> list[Enrollment]:
    return []


def _select_course_by_name(courses: list[Course], name: str) -> Course:
    for course in courses:
        if course.course_name == name:
            return course
    raise ValueError(f"course={name} not found")
