# PythonTr
Test veya eğitim amaçlı kullanılabilecek Python program ve dökümanları.


helptext2html.py metin dosyasından html dosyasına dönüştürür. Girdi dosyasında ana başlık, bölüm başlıkları ve ayrıntıları yer alır. Her bölüm şunlardan biriyle başlar: #---, ---, /---, //--- ve boş bir satırla veya yeni bir bölümün başlamasıyla biter. Bölüm ayrıntıları başlangıçta gizlidir, bölüm başlığına tıkladığınızda görünür hale gelir, tekrar tıklarsanız yeniden gizlenir.
Ayrıntılar program kodu şeklinde, yani sabit genişlikli fontta görüntülenir. girdi_metin_dosyasi ve cikti_html_dosyasi argüman olarak verilebilir. Verilmemişse program çalıştırıldığında ister. myFunction adında bir Javascript fonksiyonu bölüm ayrıntılarının gizlenmesi ve gösterilmesi işlemini gerçekleştirir.Her yeni bölüm Div+bölüm_sayaci şeklinde adlandırılır ve fonksiyon her bölüm için çağrılarak başlangıçta gizlenmeleri sağlanır.

deneme.txt helptext2html.py programı için örnek girdi dosyasıdır.

deneme.html helptext2html.py programı için örnek çıktı dosyasıdır.


