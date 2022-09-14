import "./styles.css";
import apiaudio from "apiaudio";

const button = document.getElementById("generate");

button.onclick = async () => {
  // Get values from the DOM
  const apiKey = document.getElementById("apikey").value;
  const scriptText = document.getElementById("content").value;

  try {
    button.innerText = "Loading...";

    // Configure API audio with the API key
    apiaudio.configure({ apiKey });

    // Generate a script using the value from the textarea
    let script = await apiaudio.Script.create({
      scriptText
    });
    console.log(script);

    // Generate speech using the scriptId returned from the script endpoint
    let speech = await apiaudio.Speech.create({
      scriptId: script.scriptId,
      voice: "Joanna", // Check api.audio for a full list of voices
      speed: "110"
    });
    console.log(speech);

    let mastering = await apiaudio.Mastering.create(
      {scriptId: script["scriptId"],
      soundTemplate: "citynights"}
    )
    console.log(mastering)
    console.log(`Response from mastering: : ${mastering["Message"]}`);
    let masteringResult = await apiaudio.Mastering.retrieve(
      script["scriptId"]);
    console.log(masteringResult["url"]);
    // Set the source of the audio player to our new file
    const audio = document.getElementById("audio");
    audio.src = masteringResult.url;

    // Reset
    apiaudio.reset();
    button.innerText = "Generate Audio";
  } catch (e) {
    console.log(e);
  }
};
