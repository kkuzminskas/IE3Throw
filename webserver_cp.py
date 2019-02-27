#import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import json
app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : "GPIO.LOW"},
   24 : {'name' : 'GPIO 24', 'state' : "GPIO.LOW"}
   }
"""
# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)"""

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   # for pin in pins:
   #    pins[pin]['state'] = "GPIO.input(pin)"
   # # Put the pin dictionary into the template data dictionary:
   # templateData = {
   #    'pins' : pins
   #    }
   # print("hello world")
   
   # Pass the template data into the template main.html and return it to the user
   # return render_template('webserver.html', **templateData)
   return render_template('webserver.html')
# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   """
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."""

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = "GPIO.input(pin)"

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('webserver.html', **templateData)

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