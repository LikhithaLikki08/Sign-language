from flask import Flask, render_template, request
import threading
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import string

app = Flask(__name__)

# Function for speech to sign (already defined in your code)
def func():
    r = sr.Recognizer()
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', ...]  # your predefined list
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("I am Listening")
        audio = r.listen(source)
        try:
            a = r.recognize_google(audio).lower()
            print('You Said: ' + a)
            # Process recognized speech
            for c in string.punctuation:
                a = a.replace(c, "")
            if a in isl_gif:
                # Display GIF or any other sign language representation
                pass
            else:
                for i in a:
                    if i in arr:
                        ImageAddress = 'letters/' + i + '.jpg'
                        ImageItself = Image.open(ImageAddress)
                        ImageNumpyFormat = np.asarray(ImageItself)
                        plt.imshow(ImageNumpyFormat)
                        plt.draw()
                        plt.pause(0.8)
        except:
            print("Speech recognition failed")

@app.route('/')
def home():
    return render_template('index.html')

# Route to start speech-to-sign conversion
@app.route('/speech_to_sign', methods=['POST'])
def speech_to_sign():
    # Run the speech recognition in a separate thread
    threading.Thread(target=func).start()
    return render_template('index.html', pred="Speech to Sign is now active!")

# Other routes for start/stop can go here
@app.route('/predict', methods=['POST'])
def predict():
    return render_template('index.html', pred="Prediction result here")

@app.route('/stop', methods=['POST'])
def stop():
    return render_template('index.html', pred="Stopped")

if __name__ == '__main__':
    app.run(debug=True)
