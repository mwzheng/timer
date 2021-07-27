from tkinter import *
from tkinter import messagebox

oneSecond = 1000  # 1000ms = 1s
maxSeconds = 86400  # Max time in seconds allowed
defaultTime = 60  # Default time in seconds
numRows = 10
numCols = 10
widgetList = {}  # Stores all the widgets created (Pixels, label)

customImage = [
    [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "",
        "",
        "",
        "#f28e02",
        "#f28e02",
        "#09aa6c",
        "#f28e02",
        "",
        "",
        ""
    ],
    [
        "",
        "",
        "#f28e02",
        "#f28e02",
        "#09aa6c",
        "#09aa6c",
        "#09aa6c",
        "#f28e02",
        "",
        ""
    ],
    [
        "",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#09aa6c",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        ""
    ],
    [
        "",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#e1f014",
        "#f28e02",
        ""
    ],
    [
        "",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#e1f014",
        "#f28e02",
        ""
    ],
    [
        "",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        ""
    ],
    [
        "",
        "",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "",
        ""
    ],
    [
        "",
        "",
        "",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "#f28e02",
        "",
        "",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ]
]


def createGUI(time):  # Creates the entire GUI
    root = Tk()
    root.title("Timer")
    root.resizable(False, False)

    # Create GUI format
    drawTimeLabel(root, time)
    drawGrid(root)
    return root


def drawTimeLabel(root, time):  # Creates & positon time label
    timeLabel = Label(root, font=("Mono", 20))
    timeLabel.config(text="Time Left: {0}s".format(time))
    timeLabel.grid(row=0, column=0, pady=5, columnspan=int(numRows))
    widgetList["timeLabel"] = timeLabel


def drawGrid(root):  # Creates the pixel grid layout
    for row in range(1, numRows + 1):
        for col in range(0, numCols):
            pixel = Button(root, padx=0, pady=0, width=1, height=2)
            pixel.config(borderwidth=0, state="disabled")
            pixel.grid(row=row, column=col)
            widgetList[row, col] = pixel


def validateTime(time):  # Checks if time input is valid, defaults to 60 if not
    try:
        time = int(time)

        if (time > maxSeconds):
            print("Time greater than {0}s. Defaulting to {1}s."
                  .format(maxSeconds, defaultTime))

            return defaultTime
        else:
            return int(time)

    except ValueError:
        print("Invalid time. Defaulting to {0}s.".format(defaultTime))
        return defaultTime


def updateTime(miliSecLeft):  # Updates the rime label in the GUI
    if (miliSecLeft < 0):
        return

    timeLabel = widgetList["timeLabel"]
    timeLabel.config(text="Time Left: {0}s".format(int(miliSecLeft/oneSecond)))
    root.after(oneSecond, updateTime, miliSecLeft - oneSecond)


def animate(pixelNumber, currentPixel, delay):  # Draws a singple pixel
    if (currentPixel >= pixelNumber):
        messagebox.showinfo("showinfo", "Times up!")
        root.destroy()
        return

    row, col, color = coordinates[currentPixel]

    changePixelColor(row, col, color)

    root.after(delay, animate, pixelNumber, currentPixel + 1, delay)


def changePixelColor(row, col, color):  # Changes the color of a single pixel
    pixel = widgetList[row+1, col]
    pixel.config(highlightbackground=color)


def getCoordinates():  # Get coordinates or pixels
    coordinates = []

    for row in range(0, len(customImage)):
        for col in range(0, len(customImage[row])):
            color = customImage[row][col]

            if (color != "" and color != "#000000"):
                coordinates.append((row, col, color))

    return coordinates


if __name__ == "__main__":
    coordinates = getCoordinates()
    pixelCount = len(coordinates)

    timeSet = input("Enter timer duration in seconds: ")
    timeSet = validateTime(timeSet)

    # Convert from sec to ms
    timeSet *= 1000

    # Calculate delay before each pixel is placed
    delay = int(timeSet/(pixelCount))

    # Create the GUI
    root = createGUI(timeSet)

    root.after(delay, animate, pixelCount, 0, delay)

    updateTime(timeSet)

    root.mainloop()
