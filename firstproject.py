memes_anlam = {
"LOL" : "Komik Cevap","CRINGE" : "Utandırıcı",
"PC" : "Kişisel Bilgisayar", "CREEPY" : "Korkunç",
"GG" : "İyi Oyundu" , "WP" : "İyi Oynadın"
}

cevap = input("Anlamını Öğrenmek İstediğiniz Kelimeyi Giriniz -> ")

if cevap in memes_anlam:
    print(memes_anlam[cevap])
else:
    print("Kelimenin Anlamı Sözlükte Bulunmamakta!")
