# Ödev 3 — Hazır Projeden TDD ile Öğrenci Sorgulamaya

Bu hazır Django projesi `/` adresinde **Başlangıç sayfası** başlığını gösterir;
arama işlevi eksiktir. Proje, önce testler yazılarak S1–S8 senaryoları ve grubun
seçtiği bir ek senaryo üzerinden geliştirilir.

## 1. Kurulum ve ilk çalıştırma

Önerilen ve doğrulanan Python sürümü **3.12**'dir. Komutları bu README'nin
bulunduğu proje ana dizininde çalıştırılır:

```bash
python -m venv .venv
```

Sanal ortamı Linux/macOS'ta `source .venv/bin/activate`, Windows PowerShell'de
`.venv\Scripts\Activate.ps1` ile etkinleştirilir. Ardından:

```bash
python -m pip install -r requirements.txt
python manage.py check
git init -b main
git add .
git commit -m "Initial project"
python -m pytest -m "not browser" -v
```

`check` hata vermemeli; ilk pytest çalıştırması **1 başarısız test** göstermelidir.
Nedeni, hazır testin `Öğrenci Sorgulama` beklemesine karşılık sayfanın henüz
`Başlangıç sayfası` yazmasıdır. Bu beklenen bir assertion hatasıdır; kurulum
hatası değildir. Başlangıçta geçen veya atlanan test yoktur. Henüz test metodu
bulunmayan Selenium sınıfı tarayıcı açmaz.

Bir üye ortak GitHub deposunu oluşturur ve başlangıç kaydını bu depoya gönderir.
Diğer üyeler aynı depoyu klonlar ve kendi hesaplarıyla çalışır. Depo adresi
raporda belirtilir; depo teslim sırasında public olmalıdır.

## 2. Başlangıç dosyaları

| Dosya | Başlangıç durumu ve yapılacak çalışma |
|---|---|
| `manage.py`, `obs_project/` | Hazır Django ayarları ve `/` URL bağlantısı |
| `student_data.py` | Sabit dört kurgusal öğrenci kaydı |
| `student_search.py` | İmza ve açıklama hazır; `find_student` şu an `NotImplementedError` üretir |
| `students/views.py` | Yalnızca şablonu açar; sorgu ve sonuç davranışı eklenecektir |
| `students/templates/students/search.html` | Yer tutucu başlık; form, mesaj ve sonuç gösterimi geliştirilecektir |
| `tests/test_views.py` | S1 için yalnızca hazır başlık testi; görünüm kontrolleri genişletilecektir |
| `tests/test_student_search.py` | Birim testlerinin yazılacağı boş test dosyası |
| `tests/test_functional.py` | Tarayıcı açma/kapatma çatısı; test metotları eklenecektir |

Veritabanı, model, migration, giriş sistemi ve kalıcı kayıt gerekmez.

## 3. İlk RED–GREEN döngüsü

Başlangıç dosyalarındaki sonraki değişiklikler `git commit -am "açıklama"` ile
kaydedilir; ayrıca `git add` gerekmez.

1. Hazır `test_s1_page_heading` testi çalıştırılır. Başlığın neden başarısız
   olduğu, sayfanın mevcut içeriğiyle karşılaştırılarak incelenir.
2. Uygulama kodundan önce S1'in form, yönlendirme ve sonuç kartının bulunmaması
   beklentileri için web testleri ve bir Selenium testi yazılır. Testler, 6.
   bölümdeki iki terminal düzeniyle çalıştırılır.
3. Eksik davranışı gösteren testler
   `git commit -am "[S1] RED - Başlangıç ekranı beklentileri"` ile kaydedilir.
4. Bu testleri geçiren uygulama kodu geliştirilir. Testler yeniden çalıştırılıp
   geçtiğinde `git commit -am "[S1] GREEN - Başlangıç ekranı"` ile kaydedilir.

## 4. Diğer senaryolar

Birim testi arama işlevini, görünüm testi Django yanıtını, tarayıcı testi gerçek
kullanıcı akışını denetler. Her senaryo, tabloda belirtilen test düzeylerinin
tamamında doğrulanmalıdır. Test kodunun ve testlerin düzeninin tasarlanması
gruba aittir; bu README'deki “Ortak işlev ve arayüz kuralları” uygulama
gereksinimlerinin parçasıdır.

| Senaryo | Girdi / beklenen davranış | Test düzeyleri |
|---|---|---|
| S1 | İlk açılış: form ve yönlendirme; sonuç yok | Görünüm, tarayıcı |
| S2 | `20260001` → Ada Deniz ve numarası | Birim, görünüm, tarayıcı |
| S3 | `20260002` → Ege Kaya; ilk öğrenciye sabitlenmez | Birim, görünüm |
| S4 | `99999999` → `None`, bulunamadı mesajı; sonuç yok | Birim, görünüm, tarayıcı |
| S5 | `2026` → `None`; kısmi eşleşme yok | Birim |
| S6 | Boş dize → `None`, yönlendirme; sonuç yok | Birim, görünüm |
| S7 | Aynı tarayıcıda `20260001 → 20260002 → 99999999`; sonuç yenilenir, son adımda eski kart kalmaz | Tarayıcı |
| S8 | Kaynak liste, kayıtlar ve sıra değişmez; tekrar sorgu aynı sonucu verir | Birim |
| E1 | Grubun seçtiği bir küçük ek davranış | Seçime uygun düzeyler |

Her senaryoda önce test yazılır ve çalıştırılır; ardından gerekli uygulama kodu
geliştirilir. Önceki senaryoların testleri de yeniden çalıştırılır. Test ilk
çalışmada geçerse kod değiştirilmeden sonuç kaydedilir ve bu durum kısaca açıklanır.

Ek senaryo mevcut arama akışına ilişkin küçük bir davranış olmalıdır; numaranın
çevresindeki boşlukların ele alınması bir seçenektir. En az iki anlamlı Selenium
akışı bulunmalıdır: ilk açılıştan başarılı aramaya geçiş ve S7'nin ardışık sorguları.
Senaryo sayısı ile test fonksiyonu sayısının aynı olması gerekmez.

## 5. Ortak işlev ve arayüz kuralları

`find_student(students, student_no)`, kendisine verilen listedeki numarayı tam
olarak eşleştirir. Bulursa kayda eşit bir sözlük, boş veya bilinmeyen numarada
`None` döndürür. Numara `str` türündedir; `02026004` başındaki sıfırı korur.
Kaynak veri ve sıralama değişmez. Metin dışı girdiler, bozuk kayıtlar ve yinelenen
numaralar için doğrulama zorunlu değildir. Arayüz bu işlevi `STUDENTS` ile kullanır.

| Web öğesi | Ortak değer |
|---|---|
| Adres / yöntem / sorgu | `/` / `GET` / `student_no` |
| Başlık | `Öğrenci Sorgulama` |
| Giriş | `id="student-no"`, `name="student_no"`, `type="text"`; `required` yok |
| Düğme / mesaj | `id="search-button"` / `id="search-message"` |
| Sonuç kartı | `id="student-result"` |
| Karttaki numara / ad | `id="result-student-no"` / `id="result-full-name"` |

İlk açılış ve boş sorgu: `Öğrenci numarası giriniz.`; eşleşme:
`Öğrenci bulundu.`; eşleşmeme: `Öğrenci bulunamadı.` Mesajlar aynen kullanılmalıdır.
Bu durumların HTTP kodu `200` olmalıdır. İlk/boş/bilinmeyen sorguda sonuç kartı
DOM'da bulunmamalıdır; CSS ile gizlemek yeterli değildir. Yerleşim ve renkler serbesttir.

## 6. Testlerin çalıştırılması

Tarayıcısız hızlı kontrol: `python -m pytest -m "not browser" -v`.
Selenium için Chrome/Chromium gerekir; ilk sürücü indirmesinde internet gerekebilir.
Sanal ortam iki terminalde de etkinleştirilir.

**Terminal 1 — sunucu:**

```bash
python manage.py runserver 127.0.0.1:8000
```

**Terminal 2 — tüm testler:**

```bash
python -m pytest -v
```

pytest sunucuyu açmaz; Django kod değişikliklerini otomatik yükler. Çatı varsayılan
olarak penceresiz tarayıcı kullanır; `HEADLESS=0` ile tarayıcı penceresi gösterilebilir.
Selenium test metotları yalnız `self` alır; pytest fixture parametresi eklenmez.

## 7. GitHub ve rapor

Her geliştirme commit'i ilgili senaryoya odaklanır. Başarısız testler RED kaydıyla,
bu testleri geçiren kod GREEN kaydıyla ayrı ayrı GitHub'a gönderilir. Bir
senaryo birden fazla küçük adımda geliştirilebilir. Üyelerin katkıları kendi
hesapları üzerinden görünmeli; değişiklikler grup içinde gözden geçirilmelidir.
Yeni dosya eklenirse ilgili commit'ten önce bir kez `git add .` çalıştırılır.

`RAPOR_TABLOLARI.md` içindeki üç tablo; senaryo sonuçları, iki gerçek RED–GREEN
döngüsünün GitHub commit bağlantıları ve bütün üyelerin katkılarıyla doldurulur.
Tablolar bir uygulama görüntüsü, bir RED–GREEN karşılaştırması ve son toplu test
çıktısıyla desteklenir. Teslim edilen kod ve testler GitHub'daki projeyle uyumlu
olmalıdır. Sanal ortam, önbellek ve sürücü ikili dosyaları ZIP'e eklenmez;
ayrıntılı teslim kuralları ödev yönergesindedir.
