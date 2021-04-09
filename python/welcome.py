import aflr
aflr.api_key = "your-key"  # or define env variable: export aflr_key=<your-key>

text = "<<sectionName::welcome>> Hey {{username}}, welcome to my workout app!"
audience = [{"username": "John"}]

# script creation
script = aflr.Script().create(
    scriptText=text,
    projectName="workout_app",
    moduleName="welcome",
    scriptName="welcome-message",
)
print(f"Script created: \n {script} \n")

# get the scriptId from the script created.
scriptId = script["scriptId"]

# speech creation
response = aflr.Speech().create(
    scriptId=scriptId, voice="Joanna", speed="110", audience=audience
)
print(f"Response from text-to-speech: \n {response} \n")

# mastering process
response = aflr.Mastering().create(
    scriptId=scriptId, backgroundTrackId="full__tropics.wav", audience=audience
)
print(f"Response from mastering: \n {response} \n")

# get url of audio tracks generated
url = aflr.Mastering().retrieve(scriptId=scriptId, parameters=audience[0])
print(f"url to download the track: \n {url} \n")

# or download
file = aflr.Mastering().download(
    scriptId=scriptId, parameters=audience[0], destination="."
)
print(f"file location: \n {file} \n")