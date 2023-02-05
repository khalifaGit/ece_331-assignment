import speech_recognition as sr

def take():
    recognizer = sr.Recognizer()

    audio_file = sr.AudioFile('audio_files_harvard.wav')

    with audio_file as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        print("Recognizing your speech...")
        audio = recognizer.record(source)

    try:

        result = recognizer.recognize_google(audio, language='en-US')
        print("\n")
        print(result)

    except sr.UnknownValueError as error:
        print("An error occurred. Please enable internet connection")
        print("Error: ", error)
        return None

    except sr.RequestError as error:
        print("An error occurred. Please enable internet connection")
        print("Error: ", error)
        return None

    return result


query = take()
print("Quitting the program now")