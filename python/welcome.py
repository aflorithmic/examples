import apiaudio

apiaudio.api_key = "your-key"  # or define env variable: export apiaudio_key=<your-key>

text = "<<sectionName::welcome>> Hey {{username}}, welcome to my workout app!"
audience = [{"username": "John"}]

# script creation
script = apiaudio.Script().create(
    scriptText=text,
    projectName="workout_app",
    moduleName="welcome",
    scriptName="welcome-message",
)
print(f"Script created: \n {script} \n")

# get the scriptId from the script created.
scriptId = script["scriptId"]

# speech creation
response = apiaudio.Speech().create(
    scriptId=scriptId, voice="sonia", speed="110", audience=audience
)
print(f"Response from text-to-speech: \n {response} \n")

# master your file
response = apiaudio.Mastering().create(
    scriptId=scriptId, soundTemplate="heatwave", audience=audience, share=True
)

# Check the response
print('Response from mastering', response)

# Listen and share your audio file 
print('Listen to your audio here', response['shareUrl'])
