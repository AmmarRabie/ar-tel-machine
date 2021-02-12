from pydub import AudioSegment
from pydub import playback
import time

speakers = ["ammar", ]
speaker_name = speakers[0]

def loadDigit(base, digit):
    fpath = f"assets/{speaker_name}/{base}_{digit}.wav"
    audioSeg = AudioSegment.from_file(fpath)
    return audioSeg

def loadSeparator():
    return AudioSegment.from_file(f"assets/{speaker_name}/sep.wav")


def getNumerSound(number):
    if(number > 100 or number < 0):
        raise("supports only positive numbers <= 100")
    if(number == 100):
        return loadDigit(2, 0)
    if(number == 10):
        return loadDigit(1, 0)
    if(number >= 11 and number <= 19):
        fpath = f"assets/{speaker_name}/{number}.wav"
        audioSeg = AudioSegment.from_file(fpath)
        return audioSeg
    if(number < 10):
        return loadDigit(0, number)
    if(number % 10 == 0):
        return loadDigit(1, number // 10)
    d1 = str(number)[1]
    d2 = str(number)[0]
    print(d1, d2)
    # for i in range(len(str(number))):
    return loadDigit(0, d1).append(loadSeparator()).append(loadDigit(1, d2))
    # loadDigit(1, d2)

def play(seg):
    playback.play(seg)
def playNum(num):
    seg = getNumerSound(int(num))
    # seg = AudioSegment.from_file(f"assets/{speaker_name}/client.wav").append(AudioSegment.silent(500)).append(seg)
    play(seg)

def playRange(s, e):
    for num in range(s, e + 1):
        playNum(num)
        time.sleep(0.5)
def playRandom():
    import random
    global speaker_name
    while(True):
        randSpeakerIndex = random.randint(0, len(speakers) - 1)
        speaker_name = speakers[randSpeakerIndex]
        randNum = random.randint(1, 100)
        playNum(randNum)
        time.sleep(0.5)

if __name__ == "__main__":
    # playRange(11, 100)
    playRandom()
    # playNum(20)


