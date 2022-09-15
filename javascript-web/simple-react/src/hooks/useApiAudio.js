import { useState } from "react";
import apiaudio from "apiaudio";

/**
 * Custom Hook for generating audio
 * We do this to encapsulate the state variables and improve reusability
 */
export const useApiAudio = () => {
  const [url, setUrl] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  /**
   * Handles the generation of a new audio file
   * @param apikey your api.audio key
   * @param scriptText the text that you wish to render
   */
  const generate = async (apiKey, scriptText) => {
    try {
      // Reset values and configure apiaudio
      setIsLoading(true);
      setError("");
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
      setUrl(masteringResult.url);

      // Reset
      apiaudio.reset();
      setIsLoading(false);

      // Handle errors
    } catch (e) {
      console.log(e);
      if (e.message) setError(e.message);
      else if (e.errors) setError(e.errors[0]);
      else setError(e);
      setIsLoading(false);
    }
  };

  return {
    generate,
    url,
    isLoading,
    error,
  };
};
