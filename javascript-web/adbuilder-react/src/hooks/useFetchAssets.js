import { useState } from "react";
import apiaudio from "apiaudio";

/**
 * Custom Hook for getting and storing the list of voices and sound templates
 */
export const useFetchAssets = () => {
  const [voiceList, setVoiceList] = useState([]);
  const [soundTemplateList, setSoundTemplateList] = useState([]);
  const [selectedVoice, setSelectedVoice] = useState({});
  const [selectedSoundTemplate, setSelectedSoundTemplate] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  /**
   * Fetch the voices and sound templates
   * @param {*} apiKey
   */
  const getVoicesAndSounds = async (apiKey) => {
    try {
      // Reset values and configure apiaudio
      setIsLoading(true);
      setError("");

      // Configure the api with our API key
      apiaudio.configure({ apiKey });

      // We have over 600 voices! Let's reduce this by only retreiving english voices
      const voices = await apiaudio.Voice.list({
        query: { language: "english" },
      });
      if (voices.voices.length > 0) {
        setVoiceList(voices.voices);
        setSelectedVoice(voices.voices[randomInteger(0, voices.voices.length)]);
      }

      // Get the list of sound templat and store it in the useState
      const sounds = await apiaudio.Sound.list();
      if (sounds.templates.length > 0) {
        setSoundTemplateList(sounds.templates);
        setSelectedSoundTemplate(
          sounds.templates[randomInteger(0, sounds.templates.length)]
        );
      }

      setIsLoading(false);
      apiaudio.reset();

      // Handle any errors
    } catch (e) {
      console.log(e);
      if (e.message) setError(e.message);
      else if (e.errors) setError(e.errors[0]);
      else setError(e);
      setIsLoading(false);
      apiaudio.reset();
    }
  };

  return {
    getVoicesAndSounds,
    voiceList,
    selectedVoice,
    setSelectedVoice,
    soundTemplateList,
    selectedSoundTemplate,
    setSelectedSoundTemplate,
    isLoading,
    error,
  };
};

// Helper to get random integers
function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
