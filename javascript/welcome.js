const apiaudio = require("apiaudio").default;

async function apiaudio_create() {
  const YOUR_API_KEY = "";
  const audience = [{ username: "John" }];
  const text =
    "<<sectionName::welcome>> Hey {{username}}, welcome to my workout app!";
  try {
    apiaudio.configure({ apiKey: YOUR_API_KEY });
    let script = await apiaudio.Script.create({
      scriptText: text,
      projectName: "workout_app",
      moduleName: "welcome",
      scriptName: "welcome-message",
    });
    console.log(script);

    let speech = await apiaudio.Speech.create({
      scriptId: script["scriptId"],
      voice: "Joanna",
      speed: "110",
      audience: audience,
    });
    console.log(`Response from text-to-speech: ${speech["message"]}`);

    let mastering = await apiaudio.Mastering.create({
      scriptId: script["scriptId"],
      soundTemplate: "jakarta",
      audience: audience,
    });
    console.log(`Response from mastering: : ${mastering["Message"]}`);

    let masteringResult = await apiaudio.Mastering.retrieve(
      script["scriptId"],
      audience[0]
    );
    console.log(masteringResult.url);
    return masteringResult.url;
  } catch (e) {
    console.error(e);
  }
}

const url = apiaudio_create();
