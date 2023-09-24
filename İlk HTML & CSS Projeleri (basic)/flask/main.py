from flask import Flask
import random
import os

app = Flask(__name__)

def yazi_tura():
    yazi_or_tura = random.randint(0,2)
    if yazi_or_tura == 0:
        return "Yazı Geldi."
    else: 
        return "Tura Geldi."
    
def emojiler():
    emojis = [":D" , ";(" , ":O" , ":]" , "8<)"]
    return random.choice(emojis)

def secilen_photo():
    secilen_foto = random.choice(os.listdir("photos"))
    with open(f'photos/{secilen_foto}' , "wb") as f:
        foto = f.read()

    return foto


@app.route("/")
def hello_world():
    return f'<h1> Ana Hatlarıyla Borsa! </h1> <ul> <li><a href="/borsa">Borsa</a></li> <li>Analiz</li> <li><a href="/odev">Ödev</a></li> </ul>'

@app.route("/borsa")
def borsa():
    return f'<h1> Borsa </h1> <p>Ana sayfaya gitmek için<a href="/"> tıklayınız.</a></p>'

@app.route("/odev")
def odev():
    yazıtura = yazi_tura()
    emogi = emojiler()
    zyzz = random.randint(1,101)
    fotograf = secilen_photo()
    return f'<h1>Bu Sayfa Ödev için Kurulmuş Sayfadır</h1> <p> Ana sayfaya dönmek için <a href="/"> tıklayınız.</a></p> <p>Yazı / Tura = {yazıtura}</p>  <p>Emoji = {emogi}</p> <p>Rastgele Sayı = {zyzz}</p> <p>Rastgele Logo = {fotograf}</p>'

app.run(debug=True)