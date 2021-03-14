import scipy.io.wavfile as wav
import scipy.signal as signal
from PIL import Image, ImageColor
from PIL import ImageDraw
x = []
fs, data = wav.read('arecibo.wav')
 
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a
 
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y



f1, f2 = 3000, 4000
data_f2 = butter_bandpass_filter(data, f2 - 200, f2 + 200, fs, order=3)


pix = []
l = len(data_f2)//1216


for i in range(1216):
    pix.append(sum(abs(data_f2[i*l:l*(i+1)]))/l)

for i in range(1216):
    if pix[i]>700:
        pix[i]='black'
    else:
        pix[i]='white'
     
for i in range(16):
    x.append(pix[76*i:76*(i+1)])      




image = Image.new("RGB", (76*5,16*5))
draw = ImageDraw.Draw(image)
for i in range(16):
    for j in range(76):
        draw.rectangle((j*5,i*5,(j+1)*5,(i+1)*5), fill = ImageColor.getrgb(x[i][j]))
image.save("empty1.png", "PNG") 
