import apiaudio
import os

from dotenv import load_dotenv

load_dotenv()

apiaudio.api_key = os.getenv('API_KEY')
print(os.environ)
print(os.getenv("API_KEY"))


# Uploads a media file
# -> returns a mediaId which must be supplied to mastering later
 response = apiaudio.Media.upload(
   file_path="./media/BorisJohnson.mp3",
   tags="tag1"
 )
 print(response)

 response = apiaudio.Media.upload(
   file_path="./media/ChrisPhilp.mp3",
   tags="tag2"
 )
 print(response)

response = apiaudio.Media.upload(
  file_path="./media/Depp.mp3",
  tags="tag3"
)
print(response) 

#Create a script 
script = apiaudio.Script().create(scriptText=
"""
<<soundSegment::intro>> 
<<sectionName::intro>>
Welcome back to weekly news in 90 seconds.
<<soundSegment::main>> 
<<sectionName::main>> 
Since the events in court last monday, many have said that Sir Keir Starmer's safety was put at risk based on Boris Johnson's false claims in the houses of parliament.
<<media::boris>> 
However, MP Chris Philp disagreed.
<<media::chris>>
In other news, in the ongoing trial between Johnny Depp and Amber Heard, Depp finally addressed the rumors everyone has been talking about in the courtroom this week:
<<media::depp>>
<<soundSegment::outro>>
<<sectionName::outro>>
That's all for today, tune in again next week for more weekly news in 90 seconds. 
""")
print(script)

#Create Speech 
response = apiaudio.Speech().create(scriptId=script.get("scriptId"), voice="sara")

#Choose from 500+ voices and 100+ sound designs: https://library.api.audio/voices

#Master it. Remember to define your media files 
template="bullmarket"
response = apiaudio.Mastering().create(
    scriptId=script.get("scriptId"),
    soundTemplate=template,
    mediaFiles=[{"boris": "a788990d" , "chris": "cedf5ce3", "depp": "db6a28b3"}],
    matchVoice=True
    share=True
    )

print(response)
    
# Check the response
    print('Response from mastering', mastering)

# Listen and share your audio file 
    print('Listen to your audio here', mastering['shareUrl'])
