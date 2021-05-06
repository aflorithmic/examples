const Aflr = require("aflr").default;

async function aflr_create() {
  const YOUR_API_KEY = "";
  const audience = [{ username: "John" }];
  const text =
    "<<sectionName::welcome>> Hey {{username}}, welcome to my workout app!";
  try {
    Aflr.configure({ apiKey: YOUR_API_KEY });
    let script = await Aflr.Script.create({
      scriptText: text,
      projectName: "workout_app",
      moduleName: "welcome",
      scriptName: "welcome-message",
    });
    console.log(script);

    let speech = await Aflr.Speech.create({
      scriptId: script["scriptId"],
      voice: "Joanna",
      speed: "110",
      audience: audience,
    });
    console.log(`Response from text-to-speech: ${speech["message"]}`);

    let mastering = await Aflr.Mastering.create({
      scriptId: script["scriptId"],
      backgroundTrackId: "full__tropics.wav",
      audience: audience,
    });
    console.log(`Response from mastering: : ${mastering["Message"]}`);

    let masteringResult = await Aflr.Mastering.retrieve(
      script["scriptId"],
      audience[0]
    );
    console.log(masteringResult.url);
    return masteringResult.url;
  } catch (e) {
    console.error(e);
  }
}

const url = aflr_create();
