## **Animated Pixel Timer**
---
Simple timer that slowly reveals a pixel image as the time ticks down towards zero. Made in python using tkinter. 

### Requirements:
- Python3
- Tkinter 

### To Run:
- `$ python3 timer.py`

### Optional ToDo:
- Change the customImage to update the image. Array indexes are for coordinates and the value is the color. Ex: [["red"]] row: 0, column: 0, Color: red
- Change numsRow & numCols to match size of customImage 

### Notes:
- Only allows for times in seconds less than 86500 (24hrs). To extend, change maxSeconds var.
- Timer defaults to 60s if input is invalid. To change, edit defaultTime var.
- Timer is not 100% accurate may be slightly off 
