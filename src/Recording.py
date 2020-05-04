from datetime import datetime
import threading
import wave
import pyaudio


class Recording:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "record"

    def __init__(self, label):
        self.lock = threading.Lock()
        self.frames = []
        self.label = label

    def start(self, seconds):
        self.RECORD_SECONDS = seconds
        try:
            print("* recording")
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=self.FORMAT,
                                      channels=self.CHANNELS,
                                      rate=self.RATE,
                                      input=True,
                                      frames_per_buffer=self.CHUNK)
        except:
            return "Запись невозможна. Микрофон не обнаружен. Проверьте работу микрофона и перезапустите приложение."

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)
            self.label.update(int(i / self.RATE * self.CHUNK))

        print("* done recording")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(str(self.WAVE_OUTPUT_FILENAME) + "_" + str(datetime.utcnow()) + ".wav", 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()



