from scipy.io import wavfile
samplerate, data = wavfile.read('C:/Users/PHUC//Desktop/test2.wav')
print(len(data))

