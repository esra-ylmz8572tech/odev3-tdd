"""find_student için birim testleri."""
from student_data import STUDENTS
from student_search import find_student


def test_s2_find_student_returns_ada_deniz():
    result = find_student(STUDENTS, "20260001")

    assert result == {"student_no": "20260001", "full_name": "Ada Deniz"}


def test_s3_find_student_returns_ege_kaya():
    result = find_student(STUDENTS, "20260002")

    assert result == {"student_no": "20260002", "full_name": "Ege Kaya"}