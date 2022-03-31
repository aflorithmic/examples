<p align="center">
<a href="https://www.api.audio/" rel="noopener">
 <img src="https://d9hhrg4mnvzow.cloudfront.net/www.api.audio/ddeb49ef-logo-api-audio-isolines_10au02y000000000000028.png" alt="api.audio logo"></a>
</p>

<h3 align="center">api.audio Examples</h3>

---

<p align="center"> A collection of ready-to-deploy examples for <a href="https://www.api.audio/" rel="noopener">api.audio</a> using <a href="https://github.com/aflorithmic/aflr_python" rel="noopener"> aflr python SDK </a> and <a href="https://github.com/aflorithmic/aflr_npm" rel="noopener">aflr javascript SDK</a>.
    <br>
</p>

## Python examples

All python examples use the official <a href="https://github.com/aflorithmic/aflr_python" rel="noopener"> aflr python SDK </a>

| Example                                                                                                                                                                                                         | Industry      |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| [Welcome audio message](https://github.com/aflorithmic/examples/blob/main/python/welcome.py) <br/> Give a warm welcome to your users, using their name as personalisation parameter.                            | 🏃‍♂️Fitness     |
| [Running update](https://github.com/aflorithmic/examples/blob/main/python/running_update.py) <br/> A running audio update using name, speed and heart rate as personalisation parameters.                       | 🏃‍♂️Fitness     |
| [Voucher code](https://github.com/aflorithmic/examples/blob/main/python/voucher_code.py) <br/> A voucher code audio generator with voices and background tracks personalised depending on the user preferences. | ✨MarTech     |
| [Voicemail](https://github.com/aflorithmic/examples/blob/main/python/voicemail.py) <br/> A voicemail message with personalisation for names and various preferences.                                            | ✨SalesOps    |
| [Multispeaker Audio](https://github.com/aflorithmic/examples/blob/main/python/multispeaker.py) <br/> Create audio with multiple speakers                                                                        | 🎵Advertising |

## Documentation

Find the detailed documentation on [docs.api.audio](https://docs.api.audio)

# Development

There is a pre-commit hook that will run before you commit a file. This is to keep the code standards high. To enable it, you should run `make`. Then it will set up the pre-commit hook for git. Thats all! Now every time before you commit, it will run to tell you about the standards.

If you use VSCode for committing files, you may bump into `pre-commit command not found` error. That is ok, just run `brew install pre-commit` or your fave package manager [from the list here](https://pre-commit.com/#installation).

If you bump into `your pip version is old` error, just ignore it and use the terminal.

If there is a problem and you are in a rush, you can add `--no-verify` at the end of the commit command, it will skip the pre-commit hooks, e.g `git commit -m 'your commit message' --no-verify`
