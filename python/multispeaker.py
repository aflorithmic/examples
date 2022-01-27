import apiaudio
apiaudio.api_key="your_key"

# Let's create a script!
text = """
	<<soundSegment::intro>>
	<<sectionName::intro>> 
	Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. 
	<<soundSegment::main>>
	<<sectionName::main>> 
	I am Azure voice from Microsoft. I think Azure voices sound awesome.
	<<soundSegment::outro>>
	<<sectionName::outro>>
	And I am a voice from Google. What do you think? 
"""
script = apiaudio.Script().create(scriptText=text, scriptName="multiple_speakers")
print(script) 

# Create text to speech 
r = apiaudio.Speech().create(
    scriptId=script["scriptId"],
    voice="Linda",
    speed=90,
    silence_padding=0,
     sections={
        "intro": {
            "voice": "Beth",
            "speed": 110,
            "silence_padding": 1000
        },
        "main": {
            "voice": "Guy",
            "speed": 100,
        },
        "outro": {
            "voice": "Hunter",
            "speed": 100,
        }
     }
)
print(r)

# Mastering creation 
r = apiaudio.Mastering().create(scriptId=script["scriptId"], soundTemplate="copacabana")
print(r)