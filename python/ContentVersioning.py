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

script = apiaudio.Script.create(
        scriptId="concert-ad"
        scriptText=text,
        scriptName="concert-ad"
    )  

for audience in audience_params: 

    speech = apiaudio.Speech.create(
        scriptId="concert-ad",
        voice="sonia",
        audience=audience
    )

    mastering = apiaudio.Mastering.create(
        scriptId="concert-ad",
        soundTemplate="house",
        audience=audience,
        share=True
    )
    
    # Check the response
    print('Response from mastering', mastering)

    # Listen and share your audio file 
    print('Listen to your audio here', mastering['shareUrl'])
