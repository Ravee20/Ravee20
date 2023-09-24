from flask import Flask, render_template, request, redirect
import random
# Veri tabanı kitaplığını bağlama
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)




# Ana Sayfa
@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/mizah')
def mizah():
    liste_mizah = [
        "Adam kibar olayım derken yerin dibine girdi. Kız kulesine, bayan kulesi diyerek yılın kibar erkeği seçildi.",
        "Eğer bir gün çok ama çok zengin olursam eşe dosta yardım etmeyeceğim. Arkamdan parayı bulduktan sonra çok değişti bu dedirtmem. Param yokken nasıl yardım etmiyorsam gene etmem.",
        "Asgari ücretin ta kendisi benim. Hayatıma giren benimle asla geçinemiyor."
    ]
    rm = random.choice(liste_mizah)
    return render_template('mizah.html',rm=rm)

@app.route('/bilgi')
def bilgi():
    liste_bilgi = [
        "Dünyanın en kalabalık nüfusuna sahip iki ülke birbirine sınır komşusudur.",
        "Güneşin içine bir milyondan fazla Dünya sığabilir.",
        "İnsan burnu 1 trilyon farklı kokuyu algılayabilir."
    ]
    rb = random.choice(liste_bilgi)
    return render_template('bilgi.html',rb=rb)

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['name']

    # Veri tabanına gönderilecek bir nesne oluşturma
    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    return render_template('form_result.html', 
                           # Değişkenleri buraya yerleştirin
                           name=name,
                           )

if __name__ == "__main__":
    app.run(debug=True)