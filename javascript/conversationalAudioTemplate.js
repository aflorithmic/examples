const apiaudio = require("apiaudio").default;

async function apiaudio_create() {
  apiaudio.configure({ apiKey: "API_KEY" });

  // script text
  text = `
  <<soundSegment::intro>>
  <<sectionName::INTRO>>
  Ever wondered why that tomato stain on your white shirt never fades no matter how many times you wash it?
  That’s because you haven’t tried 'stain no more!'<break time="500ms"/>
  <<soundSegment::main>>
  <<sectionName::MAIN>>
  <break time="1s"/>
  Remove any stain in one wash,<break time="600ms"/>even the most persistent stains from up to seven days ago.
  <<soundSegment::*>>
  <<sectionName::MAIN1>>
  And now, only at supermart, if you buy two units, you can get your third one free!
  <<soundSegment::outro>>
  <<sectionName::OUTRO>>
  Say no to more stains, and yes to more tomato sauce!
  `;

  const script = await apiaudio.Script.create({
    scriptText: text,
    scriptName: "conversational",
  });

  await apiaudio.Speech.create({
    scriptId: script.scriptId,
    voice: "charlie",
    speed: "105",
    sections: {
      INTRO: {
        voice: "hunter",
        speed: 90,
      },
      MAIN: {
        voice: "bella",
        speed: 110,
      },
      MAIN1: {
        voice: "hunter",
        speed: 105,
      },
      OUTRO: {
        voice: "bella",
        speed: 105,
      },
    },
  });

  const mastering = await apiaudio.Mastering.create({
    scriptId: script["scriptId"],
    soundTemplate: "feelinggood",
    masteringPreset: "lightducking",
    share: True,
  });

  //  Check the response
  print("Response from mastering", mastering);

  //  Listen and share your audio file
  print("Listen to your audio here", mastering.shareUrl);
}

apiaudio_create();
