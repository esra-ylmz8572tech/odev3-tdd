"""Hazır ilk adım: S1'in yalnızca sayfa başlığı beklentisi.

S1'in diğer kontrollerini ve sonraki senaryoların testlerini siz ekleyiniz.
"""


def test_s1_page_heading(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Öğrenci Sorgulama" in response.content.decode("utf-8")
