<img src="https://lh4.googleusercontent.com/V-6OoK7yo2J-VMXkTOWCntp8h_y8MXOdIhbgHS__bb21mAu7RO7ikYJLFB6eQU0j79M=w2400" data-canonical-src="https://lh4.googleusercontent.com/V-6OoK7yo2J-VMXkTOWCntp8h_y8MXOdIhbgHS__bb21mAu7RO7ikYJLFB6eQU0j79M=w2400"/>

**A tool to help the visually impaired accurately locate items and navigate through surroundings.**

This project was made with [PeekingDuck](https://github.com/aisingapore/PeekingDuck) and **won** the [National AI Student Challenge 2022 - Category B](https://learn.aisingapore.org/national-ai-student-challenge-2022/)

# Features
 - Item Detection
 - Door Detection
 - Currency Detecion
 - 3D Surround Sound
 
# More info
 - [Youtube Video](https://youtu.be/dM9HiL169Ts)
 - [Presentation Slides](https://docs.google.com/presentation/d/12sfLQuavHRqNMKUimziwcDez71J3EDVFjtYy9YeGvWk/edit?usp=sharing)

# Models and datasets used
  - [YOLOv8](https://github.com/ultralytics/ultralytics)
  - [DoorDetect Dataset](https://github.com/MiguelARD/DoorDetect-Dataset)
  - [Custom Singapore Banknote Dataset](https://drive.google.com/drive/folders/1h-2Wim_NyZwUZfmJFs9iMRM1wMyfy3CL?usp=sharing)

## Dependencies
Libraries used: gTTS, PyAudio, PeekingDuck and SpeechRecognition, Winsound, CUDA 11.7, PyTorch, Ultralytics, OpenAL, playsound and pydub

Install ffmpeg from https://github.com/BtbN/FFmpeg-Builds/releases/

NOTE: PeekingDuck is buggy with Python 3.10 and above, use Python <= 3.9.13

Get dependencies with
```
pip install -r requirements.txt --no-deps
```


## How to use
Download folder and run run.py

### NOTE: This program only supports the Windows OS for now. However, this program is meant for mobile phones. 

(Optional) To experience what it is like to use this program on mobile phones as intended, please follow the steps below.
1. Visit https://www.dev47apps.com
2. Download DroidCam on your mobile device (available on both IOS and Android). You DO NOT have to download DroidCam on your computer.
3. Make sure your computer and mobile device is connected to the SAME WiFi network.
4. Open DroidCam. It will show you your ***WiFi IP*** and your ***DroidCam Port*** (by default usually 4747).
5. In pipeline_config_format.yml AND pipeline_config_banknote.yml, change input source to **http://<***WiFi IP***>:<***DroidCam Port***>/video**  
(e.g. http://196.168.200.200:4747/video)
6. **Done!** You can just fix your mobile device on your body and run run.py

**NOTE: Please wait for the webcam connection to stablise after running run.py. It is usually very laggy at first but it will stablise in a moment (i.e. The PeekingDuck cv2 windows receives live video signal from your mobile device almost without any lag, provided that you have a decent network connection). The time taken for the connection to stablise is usally considerably shorter on iOS than that on Android.**

Alternatively, if you want to just execute the program on your computer, change input source to 0 (i.e. webcam) in pipeline_config_format.yml and pipeline_config_banknote.yml and run run.py
