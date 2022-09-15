import apiaudio from "apiaudio";
import "./styles.css";

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
    let script = await apiaudio.Script.create({ scriptText });
    console.log(script);

    // Generate speech using the scriptId returned from the script endpoint
    let speech = await apiaudio.Speech.create({
      scriptId: script.scriptId,
      voice: "Joanna", // Check api.audio for a full list of voices
      speed: "110",
    });
    console.log(speech);

    // Master our file and convert it into an .mp3
    let mastering = await apiaudio.Mastering.create({
      scriptId: script.scriptId,
      endFormat: "mp3",
      soundTemplate: "citynights", // Check api.audio for a full list of sound templates
    });
    console.log(mastering);

    // Retreive the final result
    let masteringResult = await apiaudio.Mastering.retrieve(script.scriptId);
    console.log(masteringResult);

    // Set the source of the audio player to our new file
    const audio = document.getElementById("audio");
    audio.src = masteringResult.url;

    // Reset
    apiaudio.reset();
    button.innerText = "Generate Audio";

    // Handle errors
  } catch (e) {
    console.log(e);
    const errorElement = document.getElementById("error");
    if (e.message) errorElement.innerText = e.message;
    else if (e.errors) errorElement.innerText = e.errors[0];
    else errorElement.innerText = e;
    button.innerText = "Generate Audio";
    apiaudio.reset();
  }
};
