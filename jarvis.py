fimport speech_recognition as sr
import pyttsx3
import subprocess

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text to speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def jarvis():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Request error from Google Speech Recognition service: ", e)
        return ""

if __name__ == "__main__":
    speak("Hello! I am Jarvis..I'M The assissant of the bayya maniteja.. How can I assist you today?")
    while True:
        command = jarvis().lower()
        
        if "bye" in command:
            speak("...Goodbye!.......")
            break
        
        # Add more commands and responses as needed
        elif "hello" in command:
            speak("Hello! How are you today?")
        
        elif "how are you" in command:
            speak("I'm just a program, so I don't have feelings, but thank you for asking!")
        
        elif "who is bhaiya" in command:
            speak("Bayya Maniteja, a name resonating with determination, curiosity, and a relentless pursuit of knowledge, embodies the essence of a modern-day learner. At the tender age of 19, Maniteja has already carved a path that reflects his deep-rooted passion for technology, particularly in the realm of Artificial Intelligence and Machine Learning (AIML).Born with an innate curiosity and an insatiable thirst for understanding the intricacies of the world around him, Maniteja embarked on his journey of exploration at a young age. Growing up in an era dominated by technological advancements, he found himself drawn towards the captivating allure of AI and its boundless potential to revolutionize industries and societies alike.")

        elif "where is charminar" in command:
            speak("It is a wonderful place located in the hyderbad in telaganna")
        elif "who created you" in command:
            speak("I'm jarvis AI.It is created by a wonderful creative...He is non another than Mr.maniteja")
        elif "where is taj mahal" in command:
            speak("It is a wonderful place located in india.In the city agra")
        elif "who is the father of the computer" in command:
            speak("carlees babage")
        elif "who invented the bulb" in command:
            speak("The bulb was invented by the thomas edison in 1878")
        elif "who is the prime minister of india" in command:
            speak("Narendara modi")
        elif "who invented the C language" in command:
            speak("Dennis richae")
        elif "open chrome" in command:
            speak("Opening Chrome.")
            subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
            break
        
        elif "open youtube" in command:
            speak("Opening YouTube.")
            subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "https://www.youtube.com"])
            break
        elif "open instagram" in command:
            speak("opening Instagram")
            subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe","https://www.instagram.com"])
            break
        elif "what is the capital of india" in command:
            speak("the capital of india is delhi")
        elif "who is the current prime minister of india" in command:
            speak("narendar modi")
        elif "who heads th rbi" in commad:
            speak("governer")
        elif "who created a bitcoin" in command:
            speak("Satoshi Nakamoto")
        elif "What is the currency of India" in command:
            speak("rupee")
        elif "Who is the current President of India" in command:
            speak("Droupadi Murmu")
        elif "When was India’s independence day" in command:
            speak("august 15")
        elif "Where is India’s Silicon Valley located" in command:
            speak("Bangalore")
        elif "India’s space agency acronym" in command:
            speak("ISRO")
        elif "Premier tech institute in India" in command:
            speak("IIT (Indian Institutes of Technology")
        elif "What is the national bird of India" in command:
            speak("peacock")
        elif "What is the national flower of India" in command:
            speak("lotus")
        elif "what is the national language of india" in command:
            speak("hindi")
        elif "What is the national anthem of India" in command:
            speak("Jana Gana Mana")
        elif "What is the national flag of India" in command:
            speak("tiranga")
        elif "What is the highest mountain peak in Indian Subcontinent" in command:
            speak("Mount Everest")
        elif "What is the longest river in India" in command:
            speak("river ganga")
        elif "What is the most populous state in India" in command:
            speak("uttar pradesh")
        elif "What is the least populous state in India" in command:
            speak("sikkim")
        elif "What is the richest state in India" in command:
            speak("maharastra")
        elif "What is the poorest state in India" in command:
            speak("bihar")
        elif "What is the most literate state in India" in command:
            speak("kerela")
        elif "What is the most developed state in India" in command:
            speak("kerela")
        elif "What is the Full form of ISRO" in command:
            speak("Indian Space Research Organization")
            

        



                  
            
        
        else:
            speak("Sorry, I didn't understand that command. Can you please repeat?")



        
