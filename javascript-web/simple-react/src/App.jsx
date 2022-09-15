import { useState } from "react";
import apiAudioLogo from "./assets/logo.svg";
import { useApiAudio } from "./hooks/useApiAudio";

/**
 * Main App
 */
function App() {
  // States for our controlled components
  const [apiKey, setApiKey] = useState("");
  const [script, setScript] = useState(
    "This is a example of how API audio can be used in the browser. Paste your API key to get started!"
  );

  // Here we consume our custom hook
  const audio = useApiAudio();

  return (
    <div className="container">
      <div className="center">
        <a href="https://api.audio" target="_blank">
          <img src={apiAudioLogo} alt="ApiAudio logo" width="200px" />
        </a>
      </div>

      <h3>Api Audio - Simple Browser Demo</h3>
      <p className="box">
        1 - Provide your API key here. It should be kept private and not bundled
        with the front end of your application. Sign up on&nbsp;
        <a href="http://console.api.audio" target="_blank">
          console.api.audio
        </a>
        &nbsp;for a free API key.
      </p>

      <label for="apikey">API Key:</label>
      <input
        id="apikey"
        type="password"
        value={apiKey}
        onChange={(e) => setApiKey(e.target.value)}
      />

      <p className="box">2 - Write your script below</p>
      <label for="content">Script Content:</label>
      <textarea
        id="content"
        value={script}
        onChange={(e) => setScript(e.target.value)}
      />

      <p className="box">
        3 - Generate your audio by clicking the button below and listen
      </p>

      <div class="flex">
        <button id="generate" onClick={() => audio.generate(apiKey, script)}>
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
