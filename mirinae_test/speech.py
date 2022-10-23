import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('당신의 기분은 어떠신가요? : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ko-KR")
        print('{}'.format(text))
    except:
        print('죄송합니다. 정확히 인식하지 못했습니다.')