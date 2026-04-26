import pytest
from datetime import datetime
from struct_excel.models import SessionMode
from struct_excel.parser import parse_course_session


class TestParseCourseSession:
    def test_parse_simple_date(self):
        result = parse_course_session("Feb 10 2026 | Python Basics [2hr]")

        assert result.course_name == "Python Basics"
        assert result.duration == 2.0
        assert result.mode == SessionMode.OFFLINE
        assert result.datetime_range == [(datetime(2026, 2, 10), datetime(2026, 2, 10))]

    def test_parse_with_online(self):
        result = parse_course_session("Feb 10 2026 | [Online] Python Basics [2hr]")

        assert result.course_name == "Python Basics"
        assert result.duration == 2.0
        assert result.mode == SessionMode.ONLINE

    def test_parse_with_offline(self):
        result = parse_course_session("Feb 10 2026 | [Offline] Python Basics [2hr]")

        assert result.course_name == "[Offline] Python Basics"
        assert result.duration == 2.0
        assert result.mode == SessionMode.OFFLINE

    def test_parse_date_range(self):
        result = parse_course_session(
            "Feb 21 2026 (to Feb 26 2026) | Python Basics [30hr]"
        )

        assert result.course_name == "Python Basics"
        assert result.duration == 30.0
        assert result.datetime_range == [(datetime(2026, 2, 21), datetime(2026, 2, 26))]

    def test_parse_with_time(self):
        result = parse_course_session("Feb 21 2026 @ 9.30am | Python Basics [2hr]")

        assert result.course_name == "Python Basics"
        assert result.duration == 2.0
        assert result.datetime_range == [
            (datetime(2026, 2, 21, 9, 30), datetime(2026, 2, 21, 9, 30))
        ]

    def test_parse_with_time_pm(self):
        result = parse_course_session("Feb 21 2026 @ 2.00pm | Python Basics [2hr]")

        assert result.datetime_range[0][0].hour == 14

    def test_parse_no_duration(self):
        result = parse_course_session("Feb 10 2026 | Python Basics")

        assert result.course_name == "Python Basics"
        assert result.duration == 0.0

    def test_parse_no_pipe_raises(self):
        with pytest.raises(ValueError):
            parse_course_session("Invalid Course")

    def test_parse_malaysia_time(self):
        result = parse_course_session(
            "Feb 19 2026 (to Feb 20 2026) @ 9.30am MYT | [Online] Cybersecurity Tools [3h]"
        )

        assert result.course_name == "Cybersecurity Tools"
        assert result.duration == 3.0
        assert result.mode == SessionMode.ONLINE

    def test_parse_hour_format_no_hr(self):
        result = parse_course_session("Feb 10 2026 | Python Basics [2]")

        assert result.duration == 0.0

    def test_parse_hour_format_with_hr(self):
        result = parse_course_session("Feb 10 2026 | Python Basics [2hr]")

        assert result.duration == 2.0

    def test_parse_hour_format_hours(self):
        result = parse_course_session("Feb 10 2026 | Python Basics [2 hours]")

        assert result.duration == 0.0

    def test_multiple_time_range(self):
        result = parse_course_session("Jan 12-14 & Jan 20-21 2026 | PECB CISO")

        assert set(map(tuple, result.datetime_range)) == {
            (datetime(2026, 1, 12), datetime(2026, 1, 14)),
            (datetime(2026, 1, 20), datetime(2026, 1, 21)),
        }
        assert result.course_name == "PECB CISO"
        assert result.duration == 0.0
        assert result.mode == SessionMode.OFFLINE
