const apiaudio = require("apiaudio").default;
const https = require("https");
const fs = require("fs");

async function apiaudio_create() {
  const YOUR_API_KEY = "-";
  const text =
    "<<sectionName::update>> Hey {{username}}, you are running at {{speed}} minutes per km and your heart rate is {{bpm}}.";
  const audience = [{ username: "matt", speed: "4:40", bpm: "152" }];
  try {
    apiaudio.configure({ apiKey: YOUR_API_KEY });
    let script = await apiaudio.Script.create({
      scriptText: text,
      projectName: "workout_app",
      moduleName: "running",
      scriptName: "running_update",
    });
    console.log("Script created");

    let speech = await apiaudio.Speech.create({
      scriptId: script["scriptId"],
      voice: "Joanna",
      speed: "110",
      audience: audience,
    });
    console.log(`Response from text-to-speech: ${speech["message"]}`);

    let url = await apiaudio.Speech.retrieve((scriptId = script["scriptId"]));
    console.log(`Response from text-to-speech: ${url["update"]}`);

    // OPTIONAL, get the mastered track.
    // // Create Mastering

    let mastering = await apiaudio.Mastering.create({
      scriptId: script["scriptId"],
      soundTemplate: "parisianmorning",
      audience: audience,
    });
    console.log(`url to download the speech track: ${mastering["Message"]}`);

    // // Get Url
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

async function running_update() {
  try {
    const url_mp3 = await apiaudio_create();
    downloadUrl("default", url_mp3);
  } catch (e) {
    console.log(e);
  }
}

running_update();
