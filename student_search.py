"""Öğrencilerin testlerden başlayarak tamamlayacağı arama işlevi."""


def find_student(students, student_no):
    """Numarası tam eşleşen öğrenci kaydını veya None döndürür.

    students: student_no ve full_name alanlı sözlüklerden oluşan liste.
    student_no: aranacak öğrenci numarası; str türündedir.

    Eşleşmede ilgili kayda eşit bir sözlük döndürülür. Boş dize veya
    eşleşmeyen numara için None döndürülür. Kısmi eşleşme yapılmaz.
    Öğrenci numaralarının başındaki sıfırlar korunur.
    Kaynak liste, kayıtlar ve kayıt sırası değiştirilmez.
    """
    if not student_no:
        return None

    for student in students:
        if student["student_no"] == student_no:
            return dict(student)

    return None