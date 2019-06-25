import warnings

letters = "0123456789abcdefghijklmnopqrstuvwxyz&':,$=!-().+?;/_"
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
         '-.-',
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
	]
def morse_audio( item ):

    from pyglet import media
    import pyglet
    import time
    import glob
    import os
    import wave
    from contextlib import closing
    pyglet.lib.load_library('avbin')
    pyglet.have_avbin=True
    files = []
    wavs = []
    audios = []
    for file in glob.glob('Morse\\*.mp3'):
        files.append(file)
    for file in glob.glob('Morse\\*.wav'):
        wavs.append(file)
    one = list(item)
    str_list = [x.strip(' ') for x in one]
    str_list = [x.strip('/') for x in str_list]

    for s in str_list[0]:
        if s != "-" and s !=  ".":
            list(item)
            for letter in item:
               for i in range(0, 51):
                    if letter == " ":
                        time.sleep(1.5)
                        audios.append("Morse\\noise3.wav")
                        break
                    if letter != letterlst[i] and letter != letterlst[i].lower():
                        continue
                    else:
                        #print ("1 " + files[i])
                        audio = media.load(files[i])
                        audio.play()
                        audios.append(wavs[i])
                        audios.append("Morse\\noise2.wav")
                        time.sleep(1)
        else:
            lst = item.split()
            #print (' '.join(lst))
            for code in lst:
                for i in range(0, 51):
                    if code == "/":
                        time.sleep(1.5)
                        audios.append("Morse\\noise3.wav")
                        break
                    if code != morse[i]:
                        continue
                    else:
                        #print (files[i])
                        audio = media.load("Morse\\0_number_morse_code.wav")
                        audio.play()
                        audios.append(wavs[i])
                        audios.append("Morse\\noise2.wav")
                        time.sleep(1)
                        break
    outfile = "Encoded.wav"

    data= []
    for file in audios:
        w = wave.open(file, 'rb')
        lol = w.getparams()
        #print (lol)
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
            
def decrypter( word ):
    list(word)
    result = []
    for letter in word:
        for i in range(0, 51):
            if letter == " ":
                result.append("/ ")
                break
            if letter != letterlst[i] and letter != letterlst[i].lower():
                continue
            else:
                result.append(morse[i])
                result.append(" ")
    print (''.join(result))
    
def morsecode(morse_code):
    lst = morse_code.split()
    decoded = []
    for code in lst:
        for i in range(0, 51):
            if code == "/":
                decoded.append(" ")
                break
            if code != morse[i]:
                continue
            else:
                decoded.append(letterlst[i])
    print  (''.join(decoded))
    
warnings.filterwarnings("ignore")
decrypter("0123456789ÁÄ@&':,$=!-().+?;/_")
morsecode("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. .-... .----. ---... --..-- ...-..- -...- -.-.-- -....- -.--.- -.--. .-.-.- .-.-. ..--.. -.-.-. -..-.")
morse_audio("I am mateen's code -_-!")#Put text here to get converted to audio


        
        
    

