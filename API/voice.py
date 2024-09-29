import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    # recoginze_() method will throw a request
    # error if the API is unreachable,
    # hence using exception handling
    
    try:
        # using google speech recognition
        print("Text google: "+r.recognize_google(audio_text))
        # print("Text azure: "+r.recognize_azure(audio_text)) #Requires azure account
        # print("Text ibm: "+r.recognize_ibm(audio_text)) #Requires IBM account
        # print("Text assemplyai: "+r.recognize_assemblyai(audio_text)) #Requieres API token
        # print("Text amazon: "+r.recognize_amazon(audio_text)) #Uses bucket with acces key or secret key
        # print("Text houndify: "+r.recognize_houndify(audio_text)) #Create houndify account
        

    except:
         print("Sorry, I did not get that")

