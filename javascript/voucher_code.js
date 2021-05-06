const Aflr = require("aflr").default;
const https = require("https");
const fs = require("fs");

const YOUR_API_KEY = "-";

async function get_voucher_audio(scriptId, audience, voice, background_track) {
  console.log(`Creating voucher audio for ${audience[0]["username"]}`);
  try {
    let speech = await Aflr.Speech.create({
      scriptId: scriptId,
      voice: voice,
      speed: "110",
      audience: audience,
    });
    console.log("Response from text-to-speech");
    console.log(speech);

    //  OPTIONAL, get the mastered track.
    let mastering = await Aflr.Mastering.create({
      scriptId: scriptId,
      backgroundTrackId: background_track,
      audience: audience,
    });
    console.log(mastering);
    console.log(audience);
    let masteringResult = await Aflr.Mastering.retrieve(scriptId, audience[0]);
    // get url of audio tracks generated
    console.log(
      `url to download the track with username ${audience[0]["username"]}: \n ${masteringResult["url"]} \n`
    );
    return masteringResult.url;
  } catch (e) {
    console.error(e);
  }
}

users = [
  {
    username: "bjorn",
    location: "barcelona",
    voucher: "1 2 3",
    background_track: "full__citynights.wav",
    voice: "Brian",
  },
  {
    username: "matt",
    location: "barcelona",
    voucher: "4 5 6",
    background_track: "full__deepsea.wav",
    voice: "Joey",
  },
  {
    username: "lars",
    location: "berlin",
    voucher: "7 8 9",
    background_track: "full__geneticcode.wav",
    voice: "Matthew",
  },
  {
    username: "peadar",
    location: "luxemburg",
    voucher: "a b c",
    background_track: "full__sundaymorning.wav",
    voice: "Justin",
  },
];

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

async function voucher() {
  try {
    const text =
      "Hey {{username}}, Thanks for reaching out from {{location}}. Your voucher code is {{voucher}}. I will repeat one more time for you, {{username}}, your voucher code is {{voucher}}";
    Aflr.configure({ apiKey: YOUR_API_KEY });
    let script = await Aflr.Script.create({
      scriptText: text,
      projectName: "voucher_app",
      moduleName: "winter_campaign",
      scriptName: "voucher_2021",
    });
    const scriptId = script["scriptId"];
    console.log(`✨ Script created with id: ${scriptId}`);

    for (var i = 0; i < users.length; i++) {
      const user = users[i];
      let url_mp3;
      const audience = {
        username: user["username"],
        location: user["location"],
        voucher: user["voucher"],
      };
      url_mp3 = await get_voucher_audio(
        scriptId,
        [audience],
        user["voice"],
        user["background_track"]
      );
      downloadUrl(
        "voucher_app_winter_campaign_voucher_2021_".concat(
          audience["username"]
        ),
        url_mp3
      );
    }
  } catch (e) {
    console.log(e);
  }
}

voucher();
