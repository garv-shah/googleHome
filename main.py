from googlehomepush import GoogleAssistant
home = GoogleAssistant(host="192.168.0.102")
home.volume(1)
home.say(text="no", lang='en')
