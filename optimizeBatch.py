import os, subprocess
import messages as msg

# settings = helpers.get_settings()

def execute(PATH):
	imgFiles = os.listdir(PATH)
	print(imgFiles)
	msg.show(imgFiles)
	for item in imgFiles:
		fileName = item.replace('.png', '')
		subprocess.call([
			'convert',
			'-quality',
			'85%',
			item,
			fileName + '.jpg'
		])
