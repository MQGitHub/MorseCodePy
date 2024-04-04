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
def morse_audio(item):

    from playsound import playsound
    import time
    import glob
    import os
    import wave
    from contextlib import closing
    files = []
    wavs = []
    audios = []

    morseDot = "Morse\\morse_dih.wav"
    morseDash = "Morse\\morse_dah.wav"
    morsePause = "Morse\\noise2.wav"
    morseSpace = "Morse\\noise3.wav"
                 
    if any(item.strip('./- ')):
        word = decrypter(item)
    else:
        word = item
    for l in word:
        if l == '.':
            audios.append(morseDot)
            audios.append(morsePause)
        elif l == '-':
            audios.append(morseDash)
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
    
    playsound(outfile.replace(" ", "%20"))
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
    
warnings.filterwarnings("ignore")
decrypter("0123456789':,$=!-().+?;/_")
morsecode("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. .-... .----. ---... --..-- ...-..- -...- -.-.-- -....- -.--.- -.--. .-.-.- .-.-. ..--.. -.-.-. -..-.")
#morse_audio("I am mateen's code -_-!")#Put text here to get converted to audio


        
        
    

