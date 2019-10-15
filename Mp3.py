from gtts import gTTS
import os


text = "hello Anks what are you doing?"
language = 'en'
output = gTTS(text=text,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")