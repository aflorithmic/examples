const apiaudio = require("apiaudio").default;

async function apiaudio_create() {
  apiaudio.configure({ apiKey: "API_KEY" });

  // script text
  text = `
    <<soundSegment::intro>>
    <<sectionName::INTRO>>
    At Aflorithmic dot A I you can now create the most relevant ad for every person.
    <<soundSegment::main>>
    <<sectionName::MAIN>>
    <break time="1s"/>
    With break tags, <break time="600ms"/> you can now keep your listener interested by adding pauses in between words or sentences.
    <<soundSegment::*>>
    <<sectionName::MAIN1>>
    Add as many sections as you need to make your ad more interactive. By adding more sections you can make use of multiple voices. Just add an asterisk in your sound segment tag to ensure smooth transitions between the sections.
`;

  const script = await apiaudio.Script.create({
    scriptText: text,
    scriptName: "usingBreakTags",
  });

  await apiaudio.Speech.create({
    scriptId: script.scriptId,
    voice: "charlie",
    speed: "105",
    sections: {
      INTRO: {
        voice: "charlie",
        speed: 115,
      },
      MAIN: {
        voice: "gabriel",
        speed: 110,
      },
      MAIN1: {
        voice: "charlie",
        speed: 115,
      },
      OUTRO: {
        voice: "charlie",
        speed: 115,
      },
    },
  });

  const mastering = await apiaudio.Mastering.create({
    scriptId: script["scriptId"],
    soundTemplate: "cityechoes",
    masteringPreset: "lightducking",
    share: True,
  });

  //  Check the response
  print("Response from mastering", mastering);

  //  Listen and share your audio file
  print("Listen to your audio here", mastering.shareUrl);
}

apiaudio_create();
