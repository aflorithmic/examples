const apiaudio = require("apiaudio").default;

async function apiaudio_create() {
  try {
    apiaudio.configure({ apiKey: "API-KEY" });

    text = `
      <<soundSegment::intro>><<sectionName::intro>>
      Great news for all {{band}} fans!
      <<soundSegment::main>><<sectionName::main>>
      They have just added two new tour dates to their previously sold-out concert in {{city}}.
      <<soundSegment::outro>><<sectionName::outro>>
      Head over to buytickets.com to grab your tickets before they sell out!
      `;

    const audience_params = [
      { band: "Nickelback", city: "Berlin" },
      { band: "The Animals", city: "Barcelona" },
      { band: "Coldplay", city: "London" },
    ];

    await apiaudio.Script.create({
      scriptId: "concert-ad",
      scriptText: text,
      scriptName: "concert-ad",
    });

    audience_params.forEach(async (audience) => {
      try {
        await apiaudio.Speech.create({
          scriptId: "concert-ad",
          voice: "sonia",
          audience,
        });

        const mastering = await apiaudio.Mastering.create({
          scriptId: "concert-ad",
          soundTemplate: "cityechoes",
          masteringPreset: "lightducking",
          share: true,
          audience,
        });

        console.log("Response from mastering", mastering);

        console.log("Listen to your audio here", mastering.shareUrl);
      } catch (e) {
        console.log(e);
      }
    });
  } catch (e) {
    console.log({ e });
  }
}

apiaudio_create();
