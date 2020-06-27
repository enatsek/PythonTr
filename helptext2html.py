#!/usr/bin/env python3

"""
# helptext2html.py girdi_metin_dosyasi cikti_html_dosyasi

Metin dosyası html dosyasına dönüştürülür.
Girdi dosyası, ana başlık(ilk satır), bölüm başlıkları ve bölüm ayrıntılarını içeren bölümlerden
oluşur.
Bölüm başlıkları aşağıdakilerden biriyle başlayabilir:
    #---, /---, //---
Bölüm başlıkları sadece bir satır olabilir.
Bölümler bölüm başlığıyla başlar ve aşağıdakilerden biri olunca biter:
    - Boş bir satır
    - Yeni bir bölüm
Html dosyasında bölüm başlıkları bağlantı (link) olarak gösterilir.
Başlangıçta bütün bölüm aurıntıları gizlenmiştir.
Bir bölüm başlığına tıkladığınızda, bölüm ayrıntıları görünür hale gelir.
Tekrar tıkladığınızda gizlenir.
Ayrıntılar kod şeklinde, yani sabit genişlikli fontla gösterilir.
girdi_metin_dısyasi ve cikti_html_dosyasi komut argümanı olarak verilebilir.
Verilmemişlerse, program başladığında girilmesi istenir.
Html içinde myFunction adında bir fonksiyon vardır. Bu fonksiyon bölüm ayrıntılarının
gizlenmesini veya gösterilmesini sağlar.
Her yeni bölüm Div+Bölüm_sayacı şeklinde adlandırılır. Başlangıçta fonksiyon her bölüm için
çağırılıp, bölüm ayrıntıları gizlenir.
Özel karakterleri tercüme etmek için html.escape() yöntemi kullanılmıştır.
Örnek olması açısından deneme.txt ve deneme.html dosyaları verilmiştir.
Program çıkış kodları:
0  -> Herşey düzgün
11 -> Girdi Metin Dosyası bulunamadı
12 -> Çıktı HTML dosyası zaten var, kullanıcı üzerine yazdırmak istemedi.


    Copyright (C) 2020 Exforge exforge@karasite.com
    
    Bu program özgür yazılımdır: Özgür Yazılım Vakfı tarafından yayımlanan 
    GNU Genel Kamu Lisansı’nın sürüm 3 ya da daha sonraki sürümlerinin 
    hükümleri altında yeniden dağıtabilir ve/veya değiştirebilirsiniz.
    
    Bu program, yararlı olması umuduyla dağıtılmış olup, programın BİR 
    TEMİNATI YOKTUR; TİCARETİNİN YAPILABİLİRLİĞİNE VE ÖZEL BİR AMAÇ İÇİN 
    UYGUNLUĞUNA dair bir teminat da vermez. Ayrıntılar için GNU Genel Kamu 
    Lisansı’na göz atınız.
    
    Bu programla birlikte GNU Genel Kamu Lisansı’nın bir kopyasını elde 
    etmiş olmanız gerekir. Eğer elinize ulaşmadıysa 
    <http://www.gnu.org/licenses/> adresine bakınız.
"""

from sys import argv
import os
import html

# Html için başlangıç kodu
html_header = "<!DOCTYPE html> <html> <head> </head> <body>"
# Html için bitiş kodu
html_footer = "</body> </html>"
# Bölüm başlangıcı, bölüm ayrıntısı ve bölüm numarası dinamik olarak eklenecektir
section_header1 = '<p> <a href="javascript:myFunction(\'Div'
section_header2 = '\')">'
section_header3 = '</a> <div id="Div'
section_header4 = '" style="margin-left:10%;"><pre><code>'
# Bölüm sonu kodu
section_footer = '</code> </pre> </div> </p>\n'
# Javascript başlangıcı, kaç defa çağrılacağı dinamik olarak verilecektir.
script_header = '''<script>
function myFunction(divid) {
  var x = document.getElementById(divid);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
var i;
var str;

for (i=1; i<'''
# Javascript sonu, aslında ikinci parçası
script_footer = '''; i++) {
    str = "Div" + i.toString();
    myFunction(str);
}
</script>'''
# bölüm sayacı
section_ctr = 0

# Bölüm başlığı belirteci, bölümler bunlarla başlar
section_identifier = ["#---", "/---", "//---"]

status = -1
# -1 -> yeni başladı
# 0 -> Ana başlık verildi, henüz bir bölüm yok
# 1 -> Yeni bölüm başlığı verildi, bölüm ayrıntıları eklenecek
# 2 -> Bölüm ayrıntıları verildi

text_file = None
html_file = None

# 1 veya daha fazla argüman varsa, 1. argüman girdi_metin_dosyasi olacaktir
if len(argv) >= 2:
    text_file = argv[1]
# 2 veya daha fazla argüman varsa, 2. argüman cikti_html_dosyasi olacaktir
if len(argv) >= 3:
    html_file = argv[2]

# girdi_metin_dosyasi argüman olarak verilmedi, kullanıcıya sor
if text_file == None:
    text_file = input("Girdi Metin Dosyasının Adı: ")
# Dosya mevcut değilse yapılabilecek birşey yok
if not os.path.exists(text_file):
    print("Girdi Metin Dosyası bulunamadı. Program kapanıyor...")
    exit(11)

# cikti_html_dosyasi argüman olarak verilmedi, kullanıcıya sor
if html_file == None:
    # girdi dosyasının uzantısı html olacak şekilde bir varsayılan çıktı dosyası
    # adı oluştur
    filename, file_extension = os.path.splitext(text_file)
    temp_html_file = filename + ".html"
    html_file = input(f"Çıktı HTML Dosyasının Adı: ({temp_html_file}) ")
    # Kullanıcı hiçbirşey yazmadıysa, varsayılanı kullan
    if html_file.strip() == "":
        html_file = temp_html_file
# Çıktı dosyası zaten varsa, üzerine yazma konusunda onay al
if os.path.exists(html_file):
    ans = input("Çıktı HTML dosyası zaten var. Üzerine yazılsın mı? (e,H) ")
    if ans not in ("e", "E", "evet", "Evet", "EVET"):
        print("Program kapanıyor...")
        exit(12)

with open(text_file) as in_file, open(html_file, "w") as out_file:
    out_file.write(html_header)
    for line in in_file:
        new_section = False
        # İşlem yeni başladı, Ana Başlık'ı yaz
        if status == -1:
            if line.strip() == "":          # başlangıçtaki boş satırları atla
                continue        
            else:                           # Ana Başlık'ı yaz
                out_file.write("<H1>" + html.escape(line) + "</H1>")
                status = 0                  # Statüyü bölümleri beklemeye ayarla
                continue
        # Yeni bölüm başlangıcı olup olmadığını kontrol et
        for start in section_identifier:
            if line.startswith(start):
                starts_with = start
                new_section = True
                break
        # Yeni bir bölüme başlıyoruz
        if new_section:
            # Önceki bölüm bitirilmemişse bitir
            if status == 1:
                out_file.write(section_footer)
            section_ctr += 1
            # Yeni bölüm için html kodu ekle
            sheader_line = section_header1 + str(section_ctr) + section_header2 + \
                html.escape(line[len(starts_with):]) + section_header3 + str(section_ctr) + \
                section_header4
            out_file.write(sheader_line)
            status = 1              # Statüyü bölüm ayrıntılarını beklemeye ayarla
            continue
        # Boş satır bölüm bitti anlamına gelir (zaten bitmiş de olabilir)
        if line.strip() == "":
            if status == 1:                 # bölüm şimdi bitiyor
                out_file.write(section_footer)
                status = 2                  # bölüm zaten bitmiş
            continue
        # zaten bölüm ayrıntısı ekleme dönemindeysek ekle
        if status == 1:
            out_file.write(html.escape(line))
    # Dosya sonu geldi, son satırları hazırla
    out_file.write(section_footer)          # bölüm sonu
    out_file.write("<br /><br /><br />")    # 3 boş satır koy
    # Script'leri hazırla
    out_file.write(script_header + str(section_ctr+1) + script_footer)
    out_file.write(html_footer)

print("Bitti")
exit(0)   
