# pip3 install apiaudio
# pip3 install ffmpeg-python
#
import apiaudio
import csv
import os

# Get your API_AUDIO_KEY here: https://console.api.audio/
# Create a .env file in your root directory and add your API_AUDIO_KEY=*******************
from dotenv import load_dotenv

load_dotenv()

apiaudio.api_key = os.getenv('API_AUDIO_KEY')
print(os.environ)
print(os.getenv("API_AUDIO_KEY"))


script_keys = ['intro', 'main', 'cta']

# Function to read the csv file


def read(filepath):
    content = []
    with open(filepath) as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)
        for row in csv_reader:
            row_data = {key: value for key, value in zip(headers, row)}
            content.append(row_data)
        return content

# Select the file that includes sections
# Split in rows with the following headers: intro, main and cta
# Drag your csv file into the root directory and name it "sample.csv"
# Make sure you also have a column for the speakers voice


content = read("sample.csv")

# Combine your video and audio and pass the scriptId dynamically


def combine_audio(video, audio, id):
    if (audio):
        os.system(
            f'ffmpeg -i {video} -i {audio} -c:v copy substituteAudio_{id}.mp4')


# Iterate through the content + printing of the url results
# with the mastered files


def api_audio_create():
    for item in content:
        for row in item.items():
            newScript = ""
            for key in row:
                if(row[0] == 'intro'):
                    intro = row[1]
                    introText = '<<soundSegment::intro>><<sectionName::intro>>' + \
                        intro
                if(row[0] == 'main'):
                    main = row[1]
                    mainText = '<<soundSegment::main>><<sectionName::main>>' + \
                        main
                if(row[0] == 'cta'):
                    outro = row[1]
                    cta = '<<soundSegment::outro>><<sectionName::outro>>' + \
                        outro
                if(row[0] == 'speaker'):
                    voice = row[1]
                if(row[0] == 'id'):
                    id = row[1]
        newScript = introText + mainText + cta

# Script, speech and master your audio file, then combine the video with the mastered URL
        tryOver
            script = apiaudio.Script().create(scriptText=newScript, scriptName=id,
                                              moduleName="dynamicVoiceOver", projectName="dynamicVoiceOver")
            speech = apiaudio.Speech().create(scriptId=script.get("scriptId"), voice=voice)
            mastering = apiaudio.Mastering().create(
                scriptId=script.get("scriptId"), soundTemplate="newhorizons")
            r = apiaudio.Mastering().download(
                scriptId=script.get("scriptId"), destination="./AudioFiles")
            print(mastering["url"])
            mastered_url = mastering["url"]
            id = id.replace(" ", "")
            combine_audio("video.mp4", mastered_url, id)

        except Exception as e:
            print(e)


api_audio_create()
