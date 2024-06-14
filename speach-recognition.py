
import speech_recognition as sr

# This uses Google Speech Recognition 

# Create a recognizer object
r = sr.Recognizer()

# Path to the audio file
audio_file_path = "assets/test-intro-th.wav"

# Use the audio file as the audio source
with sr.AudioFile(audio_file_path) as source:
    # Record the audio from the file
    audio = r.record(source)
    
    try:
        # Recognize speech using Google Speech Recognition + set it to listen to Thai
        # [NOTES] It cannot listen to both thai and english in the same file
        text = r.recognize_google(audio, language="th")
        
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Sorry, an error occurred. Please check your internet connection.")

print("You said:", text)

# send text to openai and use the text to generate a response 
# transform text to audio and play it back

