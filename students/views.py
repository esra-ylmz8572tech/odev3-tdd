from django.shortcuts import render

from student_data import STUDENTS
from student_search import find_student


def search(request):
    """Öğrenci numarasıyla sorgulama yapar ve sonucu gösterir."""
    student_no = request.GET.get("student_no", "")
    student = None
    message = "Öğrenci numarası giriniz."

    if student_no:
        student = find_student(STUDENTS, student_no)
        if student is not None:
            message = "Öğrenci bulundu."

    return render(
        request,
        "students/search.html",
        {
            "student_no": student_no,
            "student": student,
            "message": message,
        },
    )