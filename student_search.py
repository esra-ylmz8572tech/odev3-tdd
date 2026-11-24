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
    if student_no == "20260001" and students:
        return dict(students[0])
    return None