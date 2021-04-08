import aflr

aflr.api_key = "your-key"  # or define env variable: export aflr_key=<your-key>
text = "<<sectionName::update>> Hey {{username}}, you are running at {{speed}} minutes per km and your heart rate is {{bpm}}."
audience = [{"username": "matt", "speed": "4:40", "bpm": "152"}]

# script creation
script = aflr.Script().create(
    scriptText=text,
    projectName="workout_app",
    moduleName="running",
    scriptName="running_update",
)
print(f"Script created: \n {script} \n")

# get the scriptId from the script created.
scriptId = script["scriptId"]

# text to speech creation
response = aflr.Speech().create(
    scriptId=scriptId,
    voice="Joanna",
    speed="110",
    audience=audience,
)
print(f"Response from text-to-speech: \n {response} \n")

# get url of the speech file generated
url = aflr.Speech().retrieve(scriptId=scriptId)
print(f"url to download the speech track: \n {url} \n")


### OPTIONAL, get the mastered track.
# # create mastering
# aflr.Mastering().create(
#     scriptId=scriptId,
#     backgroundTrackId="full__deepsea.wav",
#     audience=audience,
# )
# print(f"Response from mastering: \n {response} \n")

# # get url of audio tracks generated
# url = aflr.Mastering().retrieve(scriptId=scriptId, parameters=audience[0])
# print(f"url to download the mastered track: \n {url} \n")

# # or download
# file = aflr.Mastering().download(
#     scriptId=scriptId, parameters=audience[0], destination="."
# )
# print(f"file location: \n {file} \n")