## Python Speech Recognition



1. 전체 통괄 파일 하나 만들어주기

   ```bash
   touch speech.py
   ```

2. python 내장 SpeechRecognition 설치

   ```bash
   pip install SpeechRecognition
   ```

3. python 내장 PyAudio

   ```bash
   pip install PyAudio
   ```

4. speech.py 작성해주기

   ```python
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
   ```

5. speech.py 실행 => 음성인식 실행

   ```bash
   python speech.py
   ```

   