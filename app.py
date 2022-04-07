from flask import Flask, render_template
import os


# SHOW IMAGE
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

app = Flask(__name__)

## SHOW FORMIDLINGSAPP

@app.route('/')
def index():
	
# Open the file in append & read mode ('a+')
	with open("loggwebserver.txt", "a+") as file_object:
# Move read cursor to the start of file.
		file_object.seek(0)
# If file is not empty then append '\n'
		data = file_object.read(100)
		if len(data) > 0 :
			file_object.write("\n")
# Append text at the end of file
		file_object.write("visited!")
		
	return render_template('index.html')

def showimage(image):
    os.system("sudo fbi -a -noverbose -T 1 /static/bilder/jobber/" + image + ".png")
    
    showimage(image)
    ImageAddress = "/static/bilder/"+ image +".png"
    ImageItself = Image.open(ImageAddress)
    ImageNumpyFormat = np.asarray(ImageItself)
    plt.imshow(ImageNumpyFormat)
    plt.draw()
    plt.pause(5) # pause how many seconds
    plt.close()
    
    
# Open the file in append & read mode ('a+')
    with open("loggwebserver.txt", "a+") as file_object:
# Move read cursor to the start of file.
        file_object.seek(0)
# If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
# Append text at the end of file
        file_object.write("Visited!" + image)

@app.route('/gaard')
def gaard():
    showimage("gaard")
    return render_template('index.html')

@app.route('/mansion')
def mansion():
	showimage("mansion")
	return render_template('index.html')

@app.route('/byhus')
def byhus():
	showimage("byhus")
	return render_template('index.html')

@app.route('/under_vann')
def under_vann():
	showimage("skmu")
	return render_template('index.html')

@app.route('/blank')
def blank():
	os.system("sudo killall -15 fbi")
	os.system("sudo killall -3 fbi")
	return render_template('index.html')

## LIST SILOCAMS

@app.route('/silo')
def silo():
	return render_template('silo.html')


## REBOOT PI
@app.route('/reboot')
def reboot():
	os.system("sudo reboot")
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',80)))
        #app.run(debug=True, host='0.0.0.0', port=80)