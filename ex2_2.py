import scipy.io.wavfile as wav
import scipy.signal as signal
from PIL import Image, ImageColor
from PIL import ImageDraw
x = []
fs, data = wav.read('signal_2.wav')
 
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
l = len(data_f2)//2300


for i in range(2300):
    pix.append(sum(abs(data_f2[i*l:l*(i+1)]))/l)

for i in range(2300):
    if pix[i]>700:
        pix[i]='black'
    else:
        pix[i]='white'
     
for i in range(25):
    x.append(pix[92*i:92*(i+1)])      




image = Image.new("RGB", (92*5,25*5))
draw = ImageDraw.Draw(image)
for i in range(25):
    for j in range(92):
        draw.rectangle((j*5,i*5,(j+1)*5,(i+1)*5), fill = ImageColor.getrgb(x[i][j]))
image.save("empty2.png", "PNG") 


