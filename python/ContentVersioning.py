import apiaudio

apiaudio.api_key = "your-key"  # or define env variable: export apiaudio_key=<your-key>

audience_params = [
    {"band": "Nickelback", "city": "Berlin"},
    {"band": "The Animals", "city": "Barcelona"},
    {"band": "Coldplay", "city": "London"},
]

text = """
<<soundSegment::intro>><<sectionName::intro>>
Great news for all {{band}} fans!
<<soundSegment::main>><<sectionName::main>>
They have just added two new tour dates to their previously sold-out concert in {{city}}.
<<soundSegment::outro>><<sectionName::outro>>
Head over to buytickets.com to grab your tickets before they sell out!
"""
for audience in audience_params:

    script = apiaudio.Script.create(
        scriptText=text,
        scriptName="concertad"
    )   

    speech = apiaudio.Speech.create(
        scriptId=script.get("scriptId"),
        voice="sonia",
        audience=audience
    )

    mastering = apiaudio.Mastering.create(
        scriptId=script.get("scriptId"),
        soundTemplate="house",
        audience=audience
    )

    print(mastering)
