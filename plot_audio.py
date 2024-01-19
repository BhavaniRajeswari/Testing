import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("iron_man.wav","rb")
sample_freq = obj.getframerate()
n_sample = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()

t_audio = n_sample / sample_freq
print(t_audio)


signal_array = np.frombuffer(signal_wave, dtype= np.int16 )
times = np.linspace(0, t_audio, num = n_sample)
times = np.linspace(times[0], times[-1], len(signal_array))

plt.figure(figsize=(15 , 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("signal Wave")
plt.xlabel("Time (sec)")
plt.xlim(0, t_audio)
plt.show()
