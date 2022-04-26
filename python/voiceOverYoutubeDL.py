# To run this script copy the following commands and run it in your terminal:
# 1. pip3 install -U pytube apiaudio
# 2. pip3 install ffmpeg-python
# 3. add .env file to your root directory and add your API_KEY=****************************
import youtube_dl
import apiaudio
import os

from dotenv import load_dotenv

load_dotenv()

apiaudio.api_key = os.getenv('API_KEY')
print(os.environ)
print(os.getenv("API_KEY"))


def apiaudio_create(scriptname, message):
    script = apiaudio.Script().create(scriptText=message, scriptName=scriptname, moduleName="video",
                                      projectName="new_video")
    print(script)

    sectionProperties = {'intro': {"endAt": 6, 'justify': 'flex-start'},
                         'main': {'endAt': 41, 'justify': 'flex-start'},
                         'outro': {'endAt': 60, 'justify': 'flex-start'}
                         }

    response = apiaudio.Speech().create(scriptId=script.get("scriptId"),
                                        voice="klaus", speed="110", silence_padding=(1000 * 2))

    print(response)
    if scriptname == "audio":
        response = apiaudio.Mastering().create(
            scriptId=script.get("scriptId"))
        print(response)
    elif scriptname == "speech":
        response = apiaudio.Mastering().create(
            scriptId=script.get("scriptId"),
            soundTemplate="melancholia",
            sectionProperties=sectionProperties,
            masteringPreset="heavyducking")
        print(response)
    response = apiaudio.Mastering().download(
        scriptId=script.get("scriptId"), destination=".")


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting...")


def downloadyoutube(filename, url):
    ydl_opts = {
        "format": "best",
        "outtmpl": str(filename),
        'noplaylist': True,
        "nooverwrites": True,
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def combine_audio(video, speech):
    os.system(
        f'ffmpeg -i {speech} speech.wav')
    os.system(
        f'ffmpeg -i {video} -filter:a "volume=0.3" videoextractaudio.wav')
    os.system(
        f'ffmpeg -i videoextractaudio.wav -i speech.wav -filter_complex amix=inputs=2:duration=first:dropout_transition=0 finalVideoAudio.wav')
    os.system(
        f'ffmpeg -i downloadedVideo.mp4 -i finalVideoAudio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4')


def download_create():

    text = """
        <<soundSegment::intro>>
        <<sectionName::intro>>
        Die Leute fragen mich immmer wieder, Wird es einen Nachfolger geben?
        <<soundSegment::main>>
        <<sectionName::main>>
        Bart von Vertellis hier. Ja, Es wird einen Nachfolger für Tschäppters geben!
        Du kennst Tschäppters noch nicht? Dann schaus dir unbedingt mal an.
        Tschäppters ist unser meistverkauftes Tagebuch und verspricht weniger Stress, sowie bessere mentale Gesundheit.
        Sogar das niederländische Fernsehen hat das gecheckt und bestätigt. Tschäppters gibt es mittlerweile in mehreren Sprachen.
        Seit fast 5 Jahren arbeiten wir an einem Nachfolger und der ist noch besser und cooler geworden.
        Aber wir brauchen deine Hilfe, denn ganz alleine können wir es nicht schaffen.<<soundSegment::outro>>
        <<sectionName::outro>>
        Seit Corona hatten wir eine schwierige Zeit. Nicht nur die Herstellungskosten sind in die Höhe geschossen.
        Wir wollen wirklich etwas verändern, denn es ist unsere Mission, Menschen zu verbinden. Und mit deiner Hilfe können wir Tschäppters 2 herausbringen.
        Klicke einfach hier, um mehr zu erfahren.
        """

    downloadyoutube("downloadedVideo.mp4",
                    "https://youtu.be/qqYLSuHS2o4")
    tracks = ["speech", "audio"]
    for track in tracks:
        apiaudio_create(track, text)
        combine_audio("downloadedVideo.mp4", "speech.mp3")


download_create()
