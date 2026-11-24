"""find_student için birim testlerini senaryo sırasıyla buraya yazınız.

İlgili senaryonun beklentisini testte kurduktan sonra student_search.py
dosyasındaki uygulamayı geliştiriniz. Bu dosyada henüz test yoktur.
"""
"""find_student için birim testleri."""
from student_data import STUDENTS
from student_search import find_student


def test_s2_find_student_returns_ada_deniz():
    result = find_student(STUDENTS, "20260001")

    assert result == {"student_no": "20260001", "full_name": "Ada Deniz"}