const apiaudio = require("apiaudio").default;
const https = require("https");
const fs = require("fs");

async function apiaudio_create() {
  const YOUR_API_KEY = "-";
  const text = `<<sectionName::intro>><<soundTemplate::intro>> Hey {{name}}, this is Evan Fleming calling from {{phonenumber}}.
  <<sectionName::main>> <<soundSegment::main>>I thought of you because I’m working with an active footwear brand that’s seen about a 
  {{percent}} percent increase in reorders, and I think that I could help your brand do the same, 
  but I’m not exactly sure. 
  <<sectionaName::outro>> <<soundSegment::outro>>So if you could give me a call back at {{phonenumber}}. Again, this is Evan. Thanks!`;
  const audience = [
    { name: "Shelley", percent: "20", phonenumber: "1-2-3-4-5-6-7" },
  ];

  try {
    apiaudio.configure({ apiKey: YOUR_API_KEY });
    let script = await apiaudio.Script.create({
      scriptText: text,
      projectName: "voicemail_example",
      moduleName: "sales",
      scriptName: "sales_example",
    });
    console.log("Script created");
    const scriptId = script["scriptId"];

    let speech = await apiaudio.Speech.create({
      scriptId: scriptId,
      voice: "Joanna",
      speed: "120",
      audience: audience,
    });
    console.log(`Response from text-to-speech: ${speech["message"]}`);

    let mastering = await apiaudio.Mastering.create({
      scriptId: script["scriptId"],
      soundTemplate: "tomorrowisfriday",
      audience: audience,
    });
    console.log(mastering);
    console.log(`Response from mastering: : ${mastering["Message"]}`);

    let masteringResult = await apiaudio.Mastering.retrieve(
      script["scriptId"],
      audience[0]
    );
    console.log(masteringResult["url"]);
    return masteringResult["url"];
  } catch (e) {
    console.error(e);
  }
}

function downloadUrl(fileName, url_mp3) {
  try {
    https.get(url_mp3, function (res) {
      const fileStream = fs.createWriteStream(fileName.concat(".mp3"));
      res.pipe(fileStream);
      fileStream.on("finish", function () {
        fileStream.close();
        console.log("mp3 audio file downloaded");
      });
    });
  } catch (e) {
    console.log(e);
  }
}

async function voiceMail() {
  try {
    const url_mp3 = await apiaudio_create();
    downloadUrl("default", url_mp3);
  } catch (e) {
    console.log(e);
  }
}

voiceMail();
