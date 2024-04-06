import warnings

letters = "0123456789abcdefghijklmnopqrstuvwxyz&':,$=!-().+?;/_ "
letters = letters.upper()
letterlst = list(letters)

morse = ['-----',
         '.----',
         '..---',
         '...--',
         '....-',
         '.....',
         '-....',
         '--...',
         '---..',
         '----.',
         '.-',
         '-...',
         '-.-.',
         '-..',
         '.',
         '..-.',
         '--.',
         '....',
         '..',
         '.---',
         '-.-',
         '.-..',
         '--',
         '-.',
         '---',
         '.--.',
         '--.-',
         '.-.',
         '...',
         '-',
         '..-',
         '...-',
         '.--',
         '-..-',
         '-.--',
         '--..',
         '.-...',
         '.----.',
         '---...',
         '--..--',
         '...-..-',
         '-...-',
         '-.-.--',
         '-....-',
         '-.--.-',
         '-.--.',
         '.-.-.-',
         '.-.-.',
         '..--..',
         '-.-.-.',
         '-..-.',
         '..--.-',
         '/',
	]
morseToLetter = {morseL: letter for morseL, letter in zip(morse, letterlst)}
lettertoMorse = {letter: morseL for letter, morseL in zip(letterlst, morse)}
def morse_audio(text, speed=0.25, play=False):


    """Create and play morse code audio representation of text, return wav file location

    Args:

        item: text you want to see in morse code
        speed: how fast you want the morse code to play (default = 0.3)
    """
    from playaudio import playaudio
    import os
    import wave
    from contextlib import closing
    
    audios = []

    morseDot = "Morse/morse_dih.wav"
    morseDash = "Morse/morse_dah.wav"
    morsePause = "Morse/noise2.wav"
    morseSpace = "Morse/noise3.wav"       
    sampleRate=8000
    numChannels=1
    sampleWidth=1
    with(wave.open("Morse/tempSpace.wav", 'wb')) as spaceWave:
        pauseFrames = int(speed * sampleRate)
        spaceWave.setnchannels(numChannels)
        spaceWave.setsampwidth(sampleWidth)
        spaceWave.setframerate(sampleRate)
        silence_frames = b'\x00' * sampleWidth * numChannels * pauseFrames
        spaceWave.writeframes(silence_frames)
        morsePause = "Morse/tempSpace.wav"
    if any(text.strip('./- ')):
        word = decrypter(text)
    else:
        word = text
    for l in word:
        if l == '.':
            audios.append(morseDot)
            audios.append(morsePause)
        elif l == '-':
            audios.append(morseDash)
            audios.append(morsePause)
        elif l == ' ':
            audios.append(morsePause)
        elif l == '/':
            audios.append(morseSpace)

    fileName = morsecode(word)
    outfile = fileName+".wav"

    data= []
    for file in audios:
        w = wave.open(file, 'rb')
        lol = w.getparams()
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()

    with closing(wave.open(outfile, 'wb')) as output:

    # find sample rate from first file
        with closing(wave.open(audios[0])) as w:
            output.setparams(w.getparams())

    # write each file to output
        for audioo in audios:
            with closing(wave.open(audioo)) as w:
                output.writeframes(w.readframes(w.getnframes()))
    file = os.path.dirname(__file__) + "\\" + outfile
    playaudio(file)
    return outfile
            
def decrypter(word):
    list(word)
    if not word:
        return ''
    result = [lettertoMorse[x.upper()]+' ' for x in word]
    result = ''.join(result).rstrip()
    return result
    
def morsecode(morse_code):
    result = (''.join([morseToLetter[x] for x in morse_code.split(' ')]))
    return result
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Convert text to Morse code or Morse code to text.')
    parser.add_argument('-t', nargs='+', help='Text to be converted to Morse code')
    parser.add_argument('-m', nargs='+', help='Morse code to be converted to text')
    parser.add_argument('-a', nargs='+', help='Text to be converted to audio')
    parser.add_argument('-s', type=float, help='Set speed for audio conversion (lower = faster)')
    parser.add_argument('-p', action='store_true', help='Play audio')
    args = parser.parse_args()
    if args.t:
        text = ' '.join(args.t)
        morse_code = decrypter(text)
        print(f"Text to Morse code conversion selected. Morse code: '{morse_code}'")
    elif args.m:
        morse_code = ' '.join(args.m)
        text = morsecode(morse_code)
        print(f"Morse code to text conversion selected. Text: '{text}'")
    elif args.a:
        text = ' '.join(args.a)
        speed = args.s if args.s else 0.15
        play_audio = args.p
        morse_audio(text, speed, play_audio)
        print("Audio conversion selected.")
    else:
        print("No conversion selected.")

    #Example usage
    #decrypter("0123456789':,$=!-().+?;/_")
    #morsecode("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. .-... .----. ---... --..-- ...-..- -...- -.-.-- -....- -.--.- -.--. .-.-.- .-.-. ..--.. -.-.-. -..-.")
    #morse_audio("I am mateen's code -_-!")#Put text here to get converted to audio


        
        
    

