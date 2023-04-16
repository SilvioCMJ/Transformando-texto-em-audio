from gtts import gTTS
from playsound import playsound

audio = 'example.mp3'
lingua = 'pt-br'

sp = gTTS(text='Texto so de exemplo, isso aq vai virar o audio',lang=lingua)

sp.save(audio)
playsound(audio)
