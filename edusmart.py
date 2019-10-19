import speech_recognition as sr
from pytube import YouTube
class edusmart:
    mode=-1
    def __init__(self, m):
        pass
    def takeNotes(self,file_name='temp.txt'):
        r = sr.Recognizer()
        f = open(file_name, "w")
        with sr.Microphone() as source:
            print('Say something!')
            audio = r.listen(source)
        try:
            f.write(r.recognize_google(audio))
        except:
            pass
        f.close()
    def annotateNotes(self,file):
        pass
    def youtubeNotes(self,url,file_name='temp.txt'):
        src=YouTube(url)
        cap=src.captions.get_by_language_code('en')
        srt=cap.generate_srt_captions()
        f=open(file_name,"w")
        f.write(srt)
        f.close()