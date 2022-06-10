import apiaudio
import os

from dotenv import load_dotenv

load_dotenv()

apiaudio.api_key = os.getenv('API_KEY')
print(os.environ)
print(os.getenv("API_KEY"))


# script text
text = """
<<soundSegment::intro>>
<<sectionName::INTRO>>
<mstts:express-as style="excited"> At Aflorithmic dot A I you can now create the most relevant ad for every person. </mstts:express-as>
<<soundSegment::main>>
<<sectionName::MAIN>>
<break time="1s"/>
<mstts:express-as role="OlderAdultMale" style="calm"> With break tags, <break time="600ms"/> you can now keep your listener interested by adding pauses in between words or sentences. </mstts:express-as>
<<soundSegment::*>>
<<sectionName::MAIN1>>
Add as many sections as you need to make your ad more interactive. By adding more sections you can make use of multiple voices. Just add an asterisk in your sound segment tag to ensure smooth transitions between the sections.
<<soundSegment::outro>>
<<sectionName::OUTRO>>
Hyperfast content production with speech, sound design and mastering at your fingertips. Visit Aflorithmic dot A I for more information. 
"""
# script creation
script = apiaudio.Script.create(scriptText=text, scriptName="usingBreakTags")


r = apiaudio.Speech().create(
    scriptId=script.get("scriptId"),
    voice="charlie",
    speed=105,
    sections = {
        "INTRO": {
            "voice": "charlie",
            "speed" : 115,
        },
        "MAIN": {
            "voice": "gabriel",
            "speed": 110,
        },
        "MAIN1": {
            "voice": "charlie",
             "speed" : 115,
        },
        "OUTRO": {
            "voice": "charlie",
             "speed" : 115,
        }
    }
)


mastering = apiaudio.Mastering().create(
    scriptId=script["scriptId"],
    soundTemplate="cityechoes",
    masteringPreset="lightducking",
    share=True
)
print(mastering)

# Check the response
    print('Response from mastering', mastering)

# Listen and share your audio file 
    print('Listen to your audio here', mastering['shareUrl'])
