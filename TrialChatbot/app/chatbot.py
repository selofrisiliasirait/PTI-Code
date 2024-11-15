 # ==========FOLDER FORMAT==============
 #   /templates
 #       index.html
 #       chat.html
 #   /static
 #      (optional: CSS, JS, or image files)
 #      app.py (or chatbot.py)



from flask import Flask, render_template, request
import re
import math
import random

app = Flask(__name__)

# Fungsi percakapan
def handle_conversation(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "halo" in user_text or "hai" in user_text or "hi" in user_text:
        return "Haiii!! Ada yang bisa aku bantu?"
    elif "aku pusing banget" in user_text or "gangerti mtk" in user_text or "bantu pliss" in user_text:
        return "Butuh bantuan apaaa aku bisa kokk semoga."
    elif "kamu siapa" in user_text:
        return "Aku math bot yang bisa membantu kamu dalam perhitungan dasar. Kehadiran aku membuat kamu merasakan sesuatu yang lebih interaktif."
    elif "byee" in user_text or "thank you" in user_text:
        return "Byee sama- sama!!"
    else:
        return "Maaf, aku hanya bisa membantu dengan soal matematika dan bercanda!"

# Fungsi untuk memeriksa ekspresi matematika
def is_math_expression(user_text):
    math_pattern = r'^[0-9\+\-\/%\s\(\)\.\\*sqrt]+$'
    return re.match(math_pattern, user_text.strip())

# Fungsi untuk evaluasi ekspresi matematika
def solve_math_expression(user_text):
    try:
        user_text = user_text.replace("sqrt(", "math.sqrt(")
        result = eval(user_text)
        return str(result)
    except Exception as e:
        return "Error solving math expression."

# Daftar jokes yang akan diberikan oleh chatbot
jokes_list = [
    "Kamu itu seperti konstanta Pi, tak terhingga dan selalu bikin aku terpana.",
    "Hubungan kita kayak garis paralel, selalu sejajar dan nggak akan pernah berpisah.",
    "Kalau kamu jadi variabel X, aku bakal jadi Y, biar kita selalu ada dalam persamaan yang sama.",
    "Kamu seperti akar dari -1, nggak nyata tapi selalu ada dalam pikiranku.",
    "Aku boleh nggak jadi turunanmu? Biar aku selalu mengejar perubahan kecil dalam hidupmu.",
    "Kalau kamu sudut, aku pasti 90 derajat, karena aku jatuh tegak lurus mencintaimu.",
    "Aku dan kamu bagaikan himpunan, selalu saling melengkapi dan tak terpisahkan.",
    "Kamu seperti eksponensial, semakin lama semakin membuat hati ini berdegup lebih cepat.",
    "Jangan jadi irasional, biarkan kita jadi satu pasangan sempurna.",
    "Kita itu kayak limit, semakin dekat tanpa batas, walaupun nggak pernah benar-benar bertemu.",
    
]

# Fungsi utama chatbot response
def chatbot_response(user_text):
    if "joke" in user_text.lower() or "jokes" in user_text.lower():
        return random.choice(jokes_list)
    elif is_math_expression(user_text):
        return solve_math_expression(user_text)
    else:
        return handle_conversation(user_text)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/get")
def get_chatbot_response():
    user_message = request.args.get('userMessage')
    response = chatbot_response(user_message)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)