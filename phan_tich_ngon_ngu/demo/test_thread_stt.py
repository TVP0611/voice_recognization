
import os
from playsound import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
# import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import vlc
import pafy
import threading
import time
from io import BytesIO
import numpy as np
import base64
import sounddevice as sd
import soundfile as sf
# from pygame import mixer
from pydub import AudioSegment
from pydub.playback import play


room_master = 'Phúc'
name_butler = 'mimi'
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
stop_event = threading.Event()
words = []

# sentence = """Quê hương em là một ngôi làng nhỏ phía bên bờ dòng sông Hồng.
# Nơi đây có cánh đồng lúa rộng mỏi cánh cò bay, có những vườn cây trĩu quả ngọt, 
# có những luống rau xanh mướt mắt… Chiều chiều, bên bờ đê, lại bay lên những cánh diều đủ hình thù màu sắc của lũ trẻ. 
# ại thấp thoáng những hơi khói mỏng manh bay lên từ căn bếp nhỏ. 
# Lại văng vẳng tiếng cười, tiếng nói của những gia đình nhỏ mà ấm áp.
# Ôi! Sao mà bình yên đến thế!"""

def wake_up():
    pass

def speak_feedback(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound("sound.mp3", False)
    time.sleep(2)
    os.remove("sound.mp3")

def speak(text, stop_event):
    if stop_event == None:
        flag = False
    else:
        flag =  stop_event.is_set()
    # if flag == True:
    #     # os.remove("sound.mp3")
    #     sys.exit()
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)

    #region byte_audio
    # mp3 = BytesIO()
    # tts.write_to_fp(mp3)
    # mp3.seek(0)
    # # song = AudioSegment.from_file(mp3, format="mp3")
    # # play(song)
    # data_mp3 = base64.b64encode(mp3.getvalue())
    # # data_mp3.decode('UTF-8')
    # data_byte = base64.b64decode((data_mp3))
    # data_arr = np.frombuffer(data_byte, dtype=np.int16)
    # sf.write('myfile.wav', data_arr, 22050)  
    # sd.play(data_arr, 22050)
    # status = sd.wait()
    #endregion

    tts.save("sound.mp3")
    # playsound("sound.mp3", False)
    player = vlc.MediaPlayer("sound.mp3")
    if flag == True:
        player.stop()
        stop_event.clear()
        sys.exit()
    player.play()
    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
    while str(player.get_state()) in good_states:
        print(str(player.get_state()))
        if flag == True:
            player.stop()
            stop_event.clear()
            sys.exit()
    player.stop()
    # time.sleep(2)
    # os.remove("sound.mp3")
    

def speak_test(text, stop_event):
    
    flag = stop_event.is_set
    
    t_play = threading.Thread(target=speak, args=(text, stop_event, ), daemon=True)
    t_play.start()
    # if len(text) > 0:
    #     print("Bot: {}".format(text))
    #     if name_butler in text:
    #         stop_event.set()
    #         # tts = gTTS(text=sentence, lang=language, slow=False)
    # else:
    #     print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound1.mp3")
    if flag == True:
        os.remove("sound1.mp3")
        sys.exit()
    time.sleep(2)
    os.remove("sound1.mp3")

def get_audio():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Tôi: ", end='')
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                print(text)
                if text == name_butler:
                    stop_event.set()
                return text
            except:
                print("...")
                return 0

def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))


def stop():
    speak("Hẹn gặp lại bạn sau!")

def get_text():
    while True:
        text = get_audio()
        if text:
            return text.lower()
        else:
            speak_feedback("Bot không nghe rõ. Bạn nói lại được không!")
            time.sleep(1)
            return 0

def get_up():
    while True:
        text = get_audio()
        if text:
            return text.lower()
        else:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
            time.sleep(1)
            pass
        # else:
        #     speak("Bot không nghe rõ. Bạn nói lại được không!")
        #     time.sleep(1)
        #     return 0

def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=5).to_dict()
        if result:
            break
    ############### sẽ có if result = None trả lời tôi không kiếm đc
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    # webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")
    video = pafy.new(url)
    best = video.getbestaudio()
    playurl = best.url
    ins = vlc.Instance()
    player = ins.media_player_new()
    code = urllib.request.urlopen(url).getcode()
    if str(code).startswith('2') or str(code).startswith('3'):
        print('Stream is working')
    else:
        print('Stream is dead')
    Media = ins.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
    while str(player.get_state()) in good_states:
        print('Stream is working. Current state = {}'.format(player.get_state()))

    print('Stream is not working. Current state = {}'.format(player.get_state()))
    # while 1:
    #     player.get_state()
    player.stop()
    
def current_weather(stop_event):
    speak_feedback("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = input("thành phố")
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,                                                              hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content, None)
        time.sleep(20)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
    if stop_event.is_set():
        print("dừng thời tiết.")
        sys.exit()



def assistant():
    global words
    while True:
        # stop_event = threading.Event()
        # # speak("chào bạn")
        # text = get_text()
        # # stop_event.set()
        # if name_butler in str(text):
            #     stop_event.set()
            #     ### phản hồi khi gọi tên
        # speak("Ai kêu Mi á có Mi đây. Bạn cần Mi giúp gì?") #### chạy random trong file
        # if name_butler in words:
        #     words.pop(0)
        action_sentence = input("action")
        if "thời tiết" in action_sentence:
            t_wth = threading.Thread(target= current_weather, args=(stop_event, ), daemon= True)
            t_wth.start()
            t_wth.join()
        elif "mở nhạc" in action_sentence:
            play_song()
            # else :
            #     stop()
        # if stop_event.is_set():
        #     print ("Thread has been interrupted by an event.")
        #     return

def wake_word(text):
    global words
    text = input(">>")
    # stop_event.set()
    if name_butler in str(text):
        # speak("Ai kêu Mi á có Mi đây. Bạn cần Mi giúp gì?")
        speak("Ai kêu Mi á có Mi đây. Bạn cần Mi giúp gì?", None)
        stop_event.set()
        # if os.path.isfile("sound.mp3"):
        #     os.remove("sound.mp3")
    else:
        pass


# def test():
    global words
    while True:
        if len(words) > 0:
            # speak_test(words, stop_event)
            words.pop(0)
        else: pass

# wake_up = input(">>")
# words.append(wake_up)
while True:
    # wake_up = input(">>")
    # words.append(wake_up)
    # assistant()
    # if name_butler in str(wake_up):
    t = threading.Thread(target=wake_word, args=(wake_up, ), daemon= True)
    t.start()
    t.join
    assistant()