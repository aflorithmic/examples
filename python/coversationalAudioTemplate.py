import apiaudio
    
apiaudio.api_key = "API-KEY"   
        
text = """
<<soundSegment::intro>>
<<sectionName::INTRO>>
Ever wondered why that tomato stain on your white shirt never fades no matter how many times you wash it?</mstts:express-as><mstts:express-as style="excited">That’s because you haven’t tried 'stain no more!'<break time="500ms"/>
<<soundSegment::main>>
<<sectionName::MAIN>>
<break time="1s"/>
Remove any stain in one wash,<break time="600ms"/>even the most persistent stains from up to seven days ago.
<<soundSegment::*>>
<<sectionName::MAIN1>>
And now, only at supermart, if you buy two units, you can get your third one free!
<<soundSegment::outro>>
<<sectionName::OUTRO>>
Say no to more stains, and yes to more tomato sauce!
"""
        
script = apiaudio.Script.create(scriptText=text, scriptName="conversational")
              
apiaudio.Speech.create(
    scriptId=script.get("scriptId"),
    voice="charlie",
    speed=105,
    sections = {
        "INTRO": {
            "voice": "hunter",
            "speed" : 90,
        },
        "MAIN": {
            "voice": "bella",
            "speed": 110,
        },
        "MAIN1": {
            "voice": "hunter",
            "speed" : 105,
        },
        "OUTRO": {
            "voice": "bella",
            "speed" : 105,
        }
    }
)
           
mastering = apiaudio.Mastering.create(
    scriptId=script["scriptId"],
    soundTemplate="Feelinggood",
    masteringPreset="lightducking",
    share=True
)

        
print("Response from mastering", mastering)
        
print("Listen to your audio here", mastering["shareUrl"])
