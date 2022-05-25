import apiaudio

apiaudio.api_key = "your_key"

# Let's create a script!
text = """
	<<soundSegment::intro>>
	<<sectionName::intro>>
	Hey! Do you know we support multiple voices from different providers in the same script? My name is Sonia. I am from Microsoft!
	<<soundSegment::main>>
	<<sectionName::main>>
	And my name is Austin! I am a Resemble provided voice. Try me out!
	<<soundSegment::outro>>
	<<sectionName::outro>>
	Nice to meet you! I am Beth and I come from amazon! Try our voices out with your own script
"""

script = apiaudio.Script().create(scriptText=text, scriptName="multiple_speakers")

# Create text to speech !

speech = apiaudio.Speech().create(
    scriptId=script["scriptId"],
    voice="Linda",
    sections={
        "intro": {"voice": "Sonia", "speed": 100},
        "main": {"voice": "Austin", "speed": 90},
        "outro": {"voice": "Beth", "speed": 100},
    },
)

# Mastering creation

mastering = apiaudio.Mastering().create(
    scriptId=script["scriptId"], soundTemplate="lofi", share=True
)


# Check the response
print('Response from mastering', mastering)

# Listen and share your audio file 
print('Listen to your audio here', mastering['shareUrl'])
