#import RPi.GPIO as GPIO
from flask import Flask, render_template, request, Response
import json
app = Flask(__name__)
import cv2
video_cap = cv2.VideoCapture(0)

#GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : "GPIO.LOW"},
   24 : {'name' : 'GPIO 24', 'state' : "GPIO.LOW"}
   }


@app.route("/")
def main():
   return render_template('webserver.html')

def generator():
   while True:
      if not video_cap.isOpened():
         raise RuntimeError('camera not started')
      _, img = video_cap.read()
      result = cv2.imencode('.jpg', img)[1].tobytes()
        # print(type(result))
      yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + result + b'\r\n\r\n')
               
@app.route('/video_feed')
def video_feed():
   return Response(generator(),
                     mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/postmethod",methods = ['POST'])
def parseJSdata():
   print("key: ")
   key = request.form['keyboard']
   if(key == 'a'):
      print('left')
   elif(key == 's'):
      print('down')
   elif(key == 'w'):
      print('up')
   elif(key == 'd'):
      print('right')
   elif(key == 'j'):
      print("shoot")

   return "return"
   

if __name__ == "__main__":
    # send request to 10.105.85.73:5000
    app.run(host='0.0.0.0')