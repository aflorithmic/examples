import apiaudio
apiaudio.api_key = "your-key" # or define env variable: export apiaudio_key=<your-key>

def get_voucher_audio(scriptId, audience, voice, background_track):
	print(f"⏳ Creating voucher audio for {audience[0]['username']}")
	# text to speech creation
	apiaudio.Speech().create(
		scriptId=scriptId,
		voice=voice,
		speed="110",
		audience=audience
		)

	# create mastering
	apiaudio.Mastering().create(
		scriptId=scriptId,
		backgroundTrackId=background_track,
		audience=audience
		)

	# retrieve mastered file
	filepath = apiaudio.Mastering().download(
		scriptId=scriptId,
		parameters=audience[0]
		)
	return filepath

users = [
	{"username": "bjorn", "location": "barcelona", "voucher": "1 2 3", "background_track": "full__citynights.wav", "voice": "Brian"},
	{"username": "matt", "location": "barcelona", "voucher": "4 5 6", "background_track": "full__deepsea.wav", "voice": "Joey"},
	{"username": "lars", "location": "berlin", "voucher": "7 8 9", "background_track": "full__geneticcode.wav", "voice": "Matthew"},
	{"username": "peadar", "location": "luxemburg", "voucher": "a b c", "background_track": "full__sundaymorning.wav", "voice": "Justin"},
]

text = "Hey {{username}}, Thanks for reaching out from {{location}}. Your voucher code is {{voucher}}. I will repeat one more time for you, {{username}}, your voucher code is {{voucher}}"
script = apiaudio.Script().create(
	scriptText=text,
	projectName="voucher_app",
	moduleName="winter_campaign",
	scriptName="voucher_2021"
)
scriptId = script["scriptId"]
print(f"✨ Script created with id: {scriptId}")

count = 1
files = []
for user in users:
	audience = [{"username":user["username"], "location":user["location"], "voucher": user["voucher"]}]
	file = get_voucher_audio(
		scriptId=scriptId,
		audience=audience,
		voice=user["voice"],
		background_track=user["background_track"]
	)
	files.append(file)
	print(f"✅ {count}/{len(users)} Files produced. File location: {file}")
	count += 1
