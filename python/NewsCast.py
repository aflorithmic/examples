import apiaudio

apiaudio.api_key = "your-key"  # or define env variable: export apiaudio_key=<your-key>


# Write your Script text
text = """
<<soundSegment::intro>>
<<sectionName::intro>>
Welcome to the NewsCast of the day. April 1st 2022. 
<<soundSegment::main>>
<<sectionName::main>>
The European Commission and the United States open new chapter in their energy cooperation
State aid: Commission approves €200 million Italian scheme to support the retail trade sector in the context of the coronavirus pandemic
<<soundSegment::outro>>
<<sectionName::outro>>
That's all for today 
"""

#Create a script 
script = apiaudio.Script.create(scriptText=text, scriptName="news")
sectionProperties = {
    'outro': {'endAt': 20, 'justify': 'flex-start'},
}

#Turn your text into speech
r = apiaudio.Speech().create(
    scriptId=script.get("scriptId"),
    voice="olivia",
    speed=105
)

#Master your file 
template = "headlines"
response = apiaudio.Mastering().create(
    scriptId=script.get("scriptId"),
    soundTemplate=template,
    sectionProperties=sectionProperties,
    share=True
)

# Retrieve your file 
print('Response from mastering', response)

# Listen and share your audio file 
print('Listen to your audio here', response['shareUrl'])
