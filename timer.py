from tkinter import *

numRows = 10
numCols = 10


def createGUI(time):  # Creates the entire GUI
    root = Tk()
    root.title("Timer")
    root.resizable(False, False)

    drawTimeLabel(root, time)
    drawGrid(root)

    return root


def drawTimeLabel(root, time):  # Creates & positon time label
    timeLabel = Label(root, font=("Ariel", 20))
    timeLabel.config(text="Time Left: {0}s".format(time))
    timeLabel.grid(row=0, column=0, pady=5, columnspan=int(numRows))


def drawGrid(root):  # Creates the pixel grid layout
    for row in range(1, numRows + 1):
        for col in range(0, numCols):
            pixel = Button(root, padx=0, pady=0, width=1, height=2)
            pixel.config(borderwidth=0, state="disabled")
            pixel.grid(row=row, column=col)


if __name__ == "__main__":
    root = createGUI(50)
    root.mainloop()
