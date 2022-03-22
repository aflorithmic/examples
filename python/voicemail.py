import apiaudio

apiaudio.api_key = "your-key"  # or define env variable: export apiaudio_key=<your-key>
text = """<<sectionName::welcome>> Hey {{name}}, this is Evan Fleming calling from {{phonenumber}}.
 I thought of you because I’m working with an active footwear brand that’s seen about a
 {{percent}} percent increase in reorders, and I think that I could help your brand do the same,
 but I’m not exactly sure. So if you could give me a call back at {{phonenumber}}. Again, this is Evan. Thanks!"""
audience = [{"name": "Shelley", "percent": "20", "phonenumber": "1-2-3-4-5-6-7"}]

# script creation
script = apiaudio.Script().create(
    scriptText=text,
    projectName="voicemail_example",
    moduleName="sales",
    scriptName="sales_example",
)
print(f"Script created: \n {script} \n")

# get the scriptId from the script created.
scriptId = script["scriptId"]

# speech creation
response = apiaudio.Speech().create(
    scriptId=scriptId, voice="Joanna", speed="120", audience=audience
)
print(f"Response from text-to-speech: \n {response} \n")

# mastering process
response = apiaudio.Mastering().create(
    scriptId=scriptId, soundTemplate="summerlove", audience=audience
)
print(f"Response from mastering: \n {response} \n")

# get url of audio tracks generated
url = apiaudio.Mastering().retrieve(scriptId=scriptId, parameters=audience[0])
print(f"url to download the track: \n {url} \n")

# or download
file = apiaudio.Mastering().download(
    scriptId=scriptId, parameters=audience[0], destination="."
)
print(f"file location: \n {file} \n")
