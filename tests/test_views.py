"""Hazır ilk adım: S1'in yalnızca sayfa başlığı beklentisi.

S1'in diğer kontrollerini ve sonraki senaryoların testlerini siz ekleyiniz.
"""


def test_s1_page_heading(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Öğrenci Sorgulama" in response.content.decode("utf-8")


def test_s1_initial_page_form_message_and_no_result(client):
    response = client.get("/")
    html = response.content.decode("utf-8")

    assert response.status_code == 200
    assert "<form" in html
    assert 'id="student-no"' in html
    assert 'name="student_no"' in html
    assert 'type="text"' in html
    assert 'id="search-button"' in html
    assert 'id="search-message"' in html
    assert "Öğrenci numarası giriniz." in html
    assert 'id="student-result"' not in html


def test_s2_search_returns_ada_deniz(client):
    response = client.get("/", {"student_no": "20260001"})
    html = response.content.decode("utf-8")

    assert response.status_code == 200
    assert 'id="search-message"' in html
    assert "Öğrenci bulundu." in html
    assert 'id="student-result"' in html
    assert 'id="result-student-no"' in html
    assert "20260001" in html
    assert 'id="result-full-name"' in html
    assert "Ada Deniz" in html


def test_s3_search_returns_ege_kaya(client):
    response = client.get("/", {"student_no": "20260002"})
    html = response.content.decode("utf-8")

    assert response.status_code == 200
    assert 'id="search-message"' in html
    assert "Öğrenci bulundu." in html
    assert 'id="student-result"' in html
    assert 'id="result-student-no"' in html
    assert "20260002" in html
    assert 'id="result-full-name"' in html
    assert "Ege Kaya" in html
    assert "Ada Deniz" not in html