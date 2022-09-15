import { useState } from "react";
import apiAudioLogo from "./assets/logo.svg";
import { useApiAudio } from "./hooks/useApiAudio";
import { useFetchAssets } from "./hooks/useFetchAssets";

/**
 * Main App
 */
function App() {
  // States for our controlled components
  const [apiKey, setApiKey] = useState("");
  const [script, setScript] = useState(
    "Api Audio offers over 600 voices and more than 70 sound templates. Start creating audio assets today by creating a free account at api dot audio"
  );

  // Here we consume our custom hooks
  const audio = useApiAudio();
  const assets = useFetchAssets();

  return (
    <div className="container">
      <div className="center">
        <a href="https://api.audio" target="_blank">
          <img src={apiAudioLogo} alt="ApiAudio logo" width="200px" />
        </a>
      </div>
      <h3>Api Audio - Create an Advertisement</h3>

      {/* Input the API Key */}
      <p className="box">
        1 - Provide your API key here. It should be kept private and not bundled
        with the front end of your application. Sign up on&nbsp;
        <a href="http://console.api.audio" target="_blank">
          console.api.audio
        </a>
        &nbsp;for a free API key.
      </p>
      <label htmlFor="apikey">API Key:</label>
      <input
        id="apikey"
        type="password"
        value={apiKey}
        onChange={(e) => setApiKey(e.target.value)}
      />

      {/* 2 - Script Input */}
      <p className="box">2 - Write your advertisement script below</p>
      <label htmlFor="content">Script Content:</label>
      <textarea
        id="content"
        value={script}
        onChange={(e) => setScript(e.target.value)}
      />

      {/* 3 - Voice and sound selection */}
      <p className="box">
        3 - Click get Assets to fetch the list of voices and sound templates
        that are available. We'll randomly choose one of each from the list to
        start for some interesting combinations.
      </p>

      {/* Load assets button */}
      <div className="flex">
        <button onClick={() => assets.getVoicesAndSounds(apiKey)}>
          {assets.isLoading ? "Loading..." : "Get Assets"}
        </button>
        <p id="error">{assets.error}</p>
      </div>

      <div className="grid">
        {/* Voices */}
        <p style={{ width: "100px" }}>Voices</p>

        <select
          disabled={assets.voiceList.length === 0}
          value={assets.selectedVoice?.alias}
          onChange={(e) =>
            assets.setSelectedVoice(
              assets.voiceList.find((v) => v.alias === e.target.value)
            )
          }
        >
          {assets.voiceList?.map((voice) => (
            <option key={voice.alias}>{voice.alias}</option>
          ))}
        </select>

        <audio controls id="audio" src={assets.selectedVoice?.audioSample}>
          Your browser does not support the <code>audio</code> element.
        </audio>

        {/* Sounds */}
        <p style={{ width: "100px" }}>Sounds</p>
        <select
          disabled={assets.soundTemplateList.length === 0}
          value={assets.selectedSoundTemplate?.templateName}
          onChange={(e) =>
            assets.setSelectedSoundTemplate(
              assets.soundTemplateList.find(
                (item) => item.templateName === e.target.value
              )
            )
          }
        >
          {assets.soundTemplateList?.map((sound) => (
            <option key={sound.templateName}>{sound.templateName}</option>
          ))}
        </select>

        <audio controls id="audio" src={assets.selectedSoundTemplate?.sample}>
          Your browser does not support the <code>audio</code> element.
        </audio>
      </div>

      {/* 4 - Generate the audio */}
      <p className="box">
        4 - Generate your audio by clicking the button below and listen
      </p>
      <div className="flex">
        <button
          id="generate"
          onClick={() =>
            audio.generate({
              apiKey: apiKey,
              scriptText: script,
              voice: assets.selectedVoice.alias,
              sound: assets.selectedSoundTemplate.templateName,
            })
          }
          disabled={
            !assets.selectedVoice.alias ||
            !assets.selectedSoundTemplate.templateName
          }
        >
          {audio.isLoading ? "Loading..." : "Generate Audio"}
        </button>
        <audio controls id="audio" src={audio.url}>
          Your browser does not support the <code>audio</code> element.
        </audio>
      </div>

      <p id="error">{audio.error}</p>
    </div>
  );
}

export default App;
