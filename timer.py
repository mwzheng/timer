from tkinter import *

oneSecond = 1000  # 1000ms = 1s
maxSeconds = 86400  # Max time in seconds allowed
defaultTime = 60  # Default time in seconds
numRows = 10
numCols = 10
widgetList = {}  # Stores all the widgets created (Pixels, label)


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


def updateTime(miliSecLeft):
    if (miliSecLeft < 0):
        return

    timeLabel = widgetList["timeLabel"]
    timeLabel.config(text="Time Left: {0}s".format(int(miliSecLeft/oneSecond)))
    root.after(oneSecond, updateTime, miliSecLeft - oneSecond)


if __name__ == "__main__":
    timeSet = input("Enter timer duration in seconds: ")
    timeSet = validateTime(timeSet)

    # Convert from sec to ms
    timeSet *= 1000

    root = createGUI(timeSet)
    updateTime(timeSet)

    root.mainloop()
