from datetime import datetime
from sqlmodel import select, func, distinct
import sqlmodel
from struct_excel.models import Enrollment, Student, Session, Course, Sector


class ReportService:
    def __init__(self, db: sqlmodel.Session) -> None:
        self.db = db

    def get_organizations(self) -> list[str]:
        rows = self.db.exec(
            select(distinct(Student.company))
            .where(Student.company != None, Student.company != "")
            .order_by(Student.company)
        ).all()
        return list(rows)

    def total_registered_participants(
        self, start: datetime, end: datetime, organizations: list[str] | None = None
    ) -> int:
        q = select(func.count(Enrollment.enrollment_id)).where(
            Enrollment.reg_date >= start, Enrollment.reg_date <= end
        )
        if organizations:
            q = q.join(Student, Enrollment.student_id == Student.student_id).where(
                Student.company.in_(organizations)
            )
        return self.db.exec(q).one()

    def total_attended_participants(
        self, start: datetime, end: datetime, organizations: list[str] | None = None
    ) -> int:
        q = select(func.count(Enrollment.enrollment_id)).where(
            Enrollment.reg_date >= start,
            Enrollment.reg_date <= end,
            Enrollment.completed == True,
        )
        if organizations:
            q = q.join(Student, Enrollment.student_id == Student.student_id).where(
                Student.company.in_(organizations)
            )
        return self.db.exec(q).one()

    def total_training_hours(
        self, start: datetime, end: datetime, organizations: list[str] | None = None
    ) -> float:
        q = (
            select(func.sum(Session.duration))
            .select_from(Enrollment)
            .join(Session, Enrollment.session_id == Session.session_id)
            .where(Enrollment.reg_date >= start, Enrollment.reg_date <= end)
        )
        if organizations:
            q = q.join(Student, Enrollment.student_id == Student.student_id).where(
                Student.company.in_(organizations)
            )
        result = self.db.exec(q).one()
        return float(result) if result else 0.0

    def gender_distribution(
        self, start: datetime, end: datetime, organizations: list[str] | None = None
    ) -> dict[str, float]:
        q = (
            select(Student.gender, func.count(func.distinct(Student.student_id)))
            .select_from(Enrollment)
            .join(Student, Enrollment.student_id == Student.student_id)
            .where(Enrollment.reg_date >= start, Enrollment.reg_date <= end)
        )
        if organizations:
            q = q.where(Student.company.in_(organizations))
        q = q.group_by(Student.gender)
        rows = self.db.exec(q).all()
        total = sum(r[1] for r in rows)
        if total == 0:
            return {}
        return {r[0].value: round(r[1] * 100 / total, 1) for r in rows}

    def government_percentage(
        self, start: datetime, end: datetime, organizations: list[str] | None = None
    ) -> float:
        base = (
            select(func.count(func.distinct(Student.student_id)))
            .select_from(Enrollment)
            .join(Student, Enrollment.student_id == Student.student_id)
            .where(Enrollment.reg_date >= start, Enrollment.reg_date <= end)
        )
        total_q = base
        gov_q = base.where(Student.sector == Sector.GOVERNMENT)
        if organizations:
            total_q = total_q.where(Student.company.in_(organizations))
            gov_q = gov_q.where(Student.company.in_(organizations))
        total = self.db.exec(total_q).one()
        if total == 0:
            return 0.0
        gov = self.db.exec(gov_q).one()
        return round(gov * 100 / total, 1)

    def total_courses_conducted(self, start: datetime, end: datetime) -> int:
        return self.db.exec(
            select(func.count(distinct(Session.session_id)))
            .select_from(Enrollment)
            .join(Session, Enrollment.session_id == Session.session_id)
            .where(Enrollment.reg_date >= start, Enrollment.reg_date <= end)
        ).one()

    def course_level_distribution(
        self, start: datetime, end: datetime
    ) -> dict[str, float]:
        rows = self.db.exec(
            select(Course.level, func.count(distinct(Session.session_id)))
            .select_from(Enrollment)
            .join(Session, Enrollment.session_id == Session.session_id)
            .join(Course, Session.course_id == Course.course_id)
            .where(Enrollment.reg_date >= start, Enrollment.reg_date <= end)
            .group_by(Course.level)
        ).all()
        total = sum(r[1] for r in rows)
        if total == 0:
            return {}
        return {r[0].value: round(r[1] * 100 / total, 1) for r in rows}

    def total_individual_participants(
        self, start: datetime, end: datetime, organizations: list[str] | None = None
    ) -> int:
        q = (
            select(func.count(func.distinct(Student.student_id)))
            .select_from(Enrollment)
            .join(Student, Enrollment.student_id == Student.student_id)
            .where(Enrollment.reg_date >= start, Enrollment.reg_date <= end)
        )
        if organizations:
            q = q.where(Student.company.in_(organizations))
        return self.db.exec(q).one()

    def participants_by_organization(
        self, start: datetime, end: datetime, organizations: list[str] | None = None
    ) -> dict[str, int]:
        q = (
            select(Student.company, func.count(func.distinct(Student.student_id)))
            .select_from(Enrollment)
            .join(Student, Enrollment.student_id == Student.student_id)
            .where(Enrollment.reg_date >= start, Enrollment.reg_date <= end)
        )
        if organizations:
            q = q.where(Student.company.in_(organizations))
        q = q.group_by(Student.company).order_by(Student.company)
        rows = self.db.exec(q).all()
        return {r[0]: r[1] for r in rows}
