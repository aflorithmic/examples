const Genius = require("genius-lyrics");
const apiaudio = require("apiaudio").default;

const YOUR_API_KEY = "-";
const geniusCreds = "-"; // check https://docs.genius.com/#/getting-started-h1 to get an API key

args = {
  song: "Dragostea Din Tei",
  artist: "O-Zone",
  voice: "Lupe",
  backgroundTrackId: "full__heatwave.wav",
};

async function apiaudio_getURL(lyrics) {
  try {
    apiaudio.configure({ apiKey: YOUR_API_KEY });
    const script = await apiaudio.Script.create({
      scriptText: lyrics,
    });
    console.log(script);
    const response = await apiaudio.Speech.create({
      scriptId: script["scriptId"],
      voice: args.voice, // define voice speed
      speed: "70", // define voice speed
    });
    const audio_files = await apiaudio.Speech.retrieve(script["scriptId"]); // retrieve url
    apiaudio.Mastering.create({
      scriptId: script["scriptId"],
      backgroundTrackId: args.backgroundTrackId, // define mastering background track
    });
    const url = await apiaudio.Mastering.retrieve(script["scriptId"]); // retrieve mastered speech
    console.log(url["url"]);
  } catch (e) {
    console.log(e);
  }
}

function multiple_replace(text) {
  //clean lyrics from a couple of predefined strings
  console.log("tipo", typeof text);
  try {
    let lyrics;
    var list = text.split("\n\n");
    for (i = 0; i < list.length; i++) {
      var verse = list[i].replace("[", "").split("]");
      lyrics = lyrics.concat(verse[1]);
    }
    lyrics = lyrics.replace("-", '<break time="0.5s"/>');
    console.log(lyrics);
    return lyrics;
  } catch (e) {
    console.log(e);
  }
}

async function genius() {
  try {
    const Client = new Genius.Client(geniusCreds);
    const searches = await Client.songs.search(args.song);
    const firstSong = searches[0];
    const lyrics = await firstSong.lyrics();
    return multiple_replace(lyrics.slice(0, 500)); //full songs with background track can be quite difficult to handle thus we only render the first 500 characters
  } catch (e) {
    console.log(e);
  }
}

async function main() {
  try {
    var lyrics = await genius();
    console.log(lyrics);
    await apiaudio_getURL(lyrics);
  } catch (e) {
    console.log(e);
  }
}

main();
