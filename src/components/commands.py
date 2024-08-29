import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import main
import components.weatherInfo as weatherInfo
import components.getNews as getNews

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say Again...")
        return "None"
    return query

def commands():
    query = takeCommand().lower()

    if 'who is' in query:
        main.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        main.speak("According to wikipedia")
        main.speak(results)

    elif 'weather in' in query or 'temperature in' in query:
        main.speak("Searching weather...")
        try:
            city_name = query.split("in ")[1]
            response = weatherInfo.getInfo(city_name)
            main.speak(response)
        except Exception as e:
            main.speak("Sorry, I couldn't get it...")

    elif 'read news' in query:
        main.speak("reading news...")
        news = getNews.news()
        print(news)
        main.speak(news)

    elif 'open youtube' in query:
        webbrowser.open('youtube.com')

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'what is the time' in query or 'tell me the time' in query:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        main.speak(f"The current time is {currentTime}")

    elif 'what is the date' in query or 'tell me the date' in query:
        currentDate = datetime.datetime.now().strftime("%d %B %Y")
        main.speak(f"Today's date is {currentDate}")

    elif query == 'good' or query == 'very good' or query == 'you are very good' or query == 'thank you':
        main.speak("Ohh thank you so much... ")

    elif 'how to stop you' in query:
        main.speak("Just say stop to stop me")

    elif 'stop' == query:
        main.speak("Thank you for having me.\nHave a Good Day")
        exit()

    elif 'what is' in query:
        main.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        main.speak("According to wikipedia")
        main.speak(results)

    elif 'i have' in query or 'i am experiencing' in query or 'symptom' in query or 'i think' in query:
        main.speak("Let me check potential remedies for you...")
        try:
            if 'i have' in query:
                symptom = query.split('i have ')[1]
            elif 'i am experiencing' in query:
                symptom = query.split('i am experiencing ')[1]
            elif 'symptom' in query:
                symptom = query.split('symptom ')[1]
            elif 'i think' in query:
                symptom = query.split('i think ')[1]

            search_query = f"{symptom} home remedies"
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            main.speak(f"Here are some potential remedies for {symptom}. I've also saved them as a PDF.")
        except Exception as e:
            main.speak("Sorry, I couldn't search for that...")