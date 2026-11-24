# Rapor Tabloları

Köşeli parantezli alanlar gerçek çalışma sonuçları ve GitHub bağlantılarıyla
doldurulmalıdır. Aşağıdaki örnek satırlar yapılmış bir çalışmayı temsil etmez.

Grup numarası: [Grup]  
Public GitHub deposu: [Tam depo adresi]  
Ortam: [Python, paketler ve tarayıcı sürümleri]  
Son test komutu: [Çalıştırılan komut]

Teslim edilen kod ve testler, GitHub'daki projeyle uyumlu olmalıdır.

## 1. Senaryolar, testler ve son durum

S1 ve E1 satırları örnek yazım içerir. Aynı senaryoyu doğrulayan birden fazla test
aynı satırda gösterilebilir. S1 satırında grubun eklediği testler belirtilir.

| Senaryo | Beklenen sonuç | Test adı / araç | Sonuç |
|---|---|---|---|
| S1 — örnek yazım | Form ve `Öğrenci numarası giriniz.` mesajı görünür; sonuç kartı yoktur. | [Kendi S1 görünüm testiniz] / pytest-django; [kendi S1 tarayıcı testiniz] / Selenium | [Son çalıştırmadaki gerçek sonuç; çalıştırmadan “geçti” yazmayınız.] |
| S2 | `20260001` için Ada Deniz ve numarası görünür. | [Birim, görünüm, tarayıcı test adları] | [Gerçek sonuç] |
| S3 | `20260002` için Ege Kaya görünür. | [Birim ve görünüm test adları] | [Gerçek sonuç] |
| S4 | `99999999` için `None`; bulunamadı mesajı, sonuç kartı yok. | [Birim, görünüm, tarayıcı test adları] | [Gerçek sonuç] |
| S5 | `2026` tam numarayla eşleşmez; `None`. | [Birim test adı] | [Gerçek sonuç] |
| S6 | Boş sorgu için `None`; numara girme mesajı, sonuç kartı yok. | [Birim ve görünüm test adları] | [Gerçek sonuç] |
| S7 | Aynı tarayıcıda `20260001 → 20260002 → 99999999`; sonuç yenilenir, son adımda eski kart kalmaz. | [Tarayıcı test adı] | [Gerçek sonuç] |
| S8 | Kaynak liste, kayıtlar ve sıra korunur; tekrar sorgu aynı sonucu verir. | [Birim test adı] | [Gerçek sonuç] |
| E1 — yalnız örnek seçim | Dış boşluklar temizlenirse ` 20260001 ` için Ada Deniz bulunur; yalnız boşluk girilmesi boş sorgu sayılır. [Kendi seçiminizle değiştiriniz.] | [Seçtiğiniz davranışı sınayan gerçek test adları / araçları] | [Son çalıştırmadaki gerçek sonuç] |

## 2. İki RED–GREEN döngüsü

Grubun gerçekleştirdiği iki döngü için ilgili GitHub commit bağlantıları ve
sonuçlar yazılır. S1 ve S2 aşağıda yalnız örnek olarak kullanılmıştır.

| Senaryo | RED commit bağlantısı ve başarısızlık nedeni | GREEN commit bağlantısı ve sonuç |
|---|---|---|
| S1 — örnek | [Gerçek bağlantı] — [Eklenen testte gözlenen eksik davranış] | [Gerçek bağlantı] — [Testi geçiren değişiklik ve sonuç] |
| S2 — örnek | [Gerçek bağlantı] — [Beklenen kaydın neden bulunamadığı] | [Gerçek bağlantı] — [Doğru kaydı döndüren değişiklik ve sonuç] |

## 3. Üyeler, GitHub hesapları ve katkılar

Grubun 4–5 üyesinin tamamı tabloda yer almalıdır. Somut katkı test, uygulama veya
kod incelemesiyle ilişkilendirilir. Eşli çalışmada üyelerin rolleri açıklanır.

| Ad soyad | Öğrenci numarası | GitHub kullanıcı adı | Somut katkı | Commit bağlantısı |
|---|---|---|---|---|
| [Üye 1] | [Numara] | [Hesap] | [Örn. kendi S1 testleri ve ilgili kod; gerçek katkınızla değiştiriniz.] | [Gerçek bağlantı] |
| [Üye 2] | [Numara] | [Hesap] | [Gerçek katkı] | [Gerçek bağlantı] |
| [Üye 3] | [Numara] | [Hesap] | [Gerçek katkı] | [Gerçek bağlantı] |
| [Üye 4] | [Numara] | [Hesap] | [Gerçek katkı] | [Gerçek bağlantı] |
| [Varsa üye 5] | [Numara] | [Hesap] | [Gerçek katkı] | [Gerçek bağlantı] |

Tablolar bir uygulama görüntüsü, bir RED–GREEN karşılaştırması ve son toplu test
çıktısıyla desteklenir. Her test için ayrı ekran görüntüsü gerekmez.
