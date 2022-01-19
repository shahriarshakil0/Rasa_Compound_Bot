from flask import Flask, render_template, request, redirect, url_for,jsonify
# from tts import tts
import requests
# from tts_fun import speech
app = Flask(__name__)
app.secret_key = "865993ef250e4f10b25c9788e228d1c8"



# @app.route('/')
# def index():
    
#     print('shakil')
#     return render_template('index.html')

#http://127.0.0.1:8000/chat_bot?me=hi
# @app.route('/')
# def chat_interact():
#     text = request.args.get('me')

#     text = single_response(text)

#     return f"bot: {text}"

# @app.route('/')
# def my_form():
#     return render_template('index.html')

data = []
@app.route('/', methods=["GET",'POST'])
def my_form_post():
    bot_message = ""
    message=""
    if request.method == "POST":
        m_text = request.form['text']
        r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": "test_user","message": m_text})
        #tts(b_text)
        print(r.json())
        for i in r.json():
            bot_message = i['text']
            #print("shakil")
            print(f"bot: {bot_message}")
            # speech(bot_message)
        single_con={
            "m_text":m_text,
            "b_text":bot_message
        }
        data.append(single_con)
        # speech(bot_message)
        return render_template('index.html',data=data)
        
       
    else:
        return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)