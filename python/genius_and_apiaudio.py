import lyricsgenius as genius
import re 
import apiaudio
from argparse import ArgumentParser

apiaudio.api_key = "your-key"  # or define env variable: export apiaudio_key=<your-key>
geniusCreds = "your-genuis-client-access-token" #check https://docs.genius.com/#/getting-started-h1 to get an API key

def multiple_replace(dict, text): #function to replace using a dictionary rather then just single strings
  regex = re.compile("|".join(map(re.escape, dict.keys())))
  return regex.sub(lambda mo: dict[mo.group(0)], text) 

def main(args):
    '''py script that allows to call the Genuis API to call retrieve lyrics from your favourite
       and render them trough the apiaudio API
       
       sample usage from CLI:
       python python/genius_and_apiaudio.py -a "Eminem" -s 'The Real Slim Shady' -v 'Joanna' -m 'full__fargalaxy_dark_father.wav' -e 'dark_father' 
       
       paramter
       -a   --artist            artist who sings your song, example: "Eminem"
       -s   --song              song from the given artist, example: "The Real Slim Shady"
       -v   --voice        voice from API.audio, example: "Joanna"
       -m   --mastering_sound   mastering background track, example: "full__fargalaxy_dark_father.wav"
       -e   --effect            efffect you want to apply over your voice, example: "dark_father"
    '''
    
    #print(apiaudio.Voice().list()) #use to print all available voices  
    #print(apiaudio.Sound().list()) #use to print all available background tracks
    
    genius_api = genius.Genius(geniusCreds)
    song = genius_api.search_song(title=args.song, artist=args.artist, song_id=None, get_full_info=True) #find the wanted song from a given artist
    replace_dict_clean_lyrics = {'\n': ' ', 
                                '\u0399': ' ',
                                '[Intro]': ' ',
                                '[Chorus]': ' ',
                                '[Verse 1]': ' ',
                                '[Verse 2]': ' ',
                                '[Verse 3]': ' ',
                                "\"": ' ',
                                '"': ' ',
                                '-': ' ',
                                '—': ' '
                                } 
    lyrics = multiple_replace(replace_dict_clean_lyrics, song.lyrics) #clean lyrics from a couple of predefined strings, feel free to add more depending on your song
    lyrics = re.sub(' +', ' ', lyrics) #more cleaning 
    
    
    # Create a new script and print the script created
    script = apiaudio.Script().create(
        scriptText="<<sectionName::lyrics>> " + lyrics[:500], #full songs with background track can be quite difficult to handle thus we only render the first 500 characters
    )

    # create a text-to-speech
    response = apiaudio.Speech().create(scriptId=script["scriptId"],
                                    voice=args.aflr_voice, #define voice
                                    speed=str(150), #define voice speed
                                    effect=args.effect, #define effects
                                    )
    print('response: ', response)
    
    audio_files = apiaudio.Speech().download(scriptId=script["scriptId"], destination=".") #download raw speech
    
    apiaudio.Mastering().create(
	scriptId=script.get("scriptId"),
	backgroundTrackId=args.mastering_sound #define mastering background track
	)
    
    url = apiaudio.Mastering().download(scriptId=script.get("scriptId"), destination=".") #download mastered speech


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-a",
        "--artist",
        type=str,
        required=True,
        help="artist of the song",
    )
    parser.add_argument(
        "-s",
        "--song",
        type=str,
        required=True,
        help="song name",
    )
    parser.add_argument(
        "-v",
        "--voice",
        type=str,
        required=False,
        default="Joanna",
        help="voice for inference through apiaudio API",
    )
    parser.add_argument(
        "-m",
        "--mastering_sound",
        type=str,
        required=False,
        default="full__citynights.wav",
        help="mastering track",
    )
    parser.add_argument(
        "-e",
        "--effect",
        type=str,
        required=False,
        help="effects used while mastering a track track",
    )
    args = parser.parse_args()
    main(args)
