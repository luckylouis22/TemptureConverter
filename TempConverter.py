from tkinter import *


class Converter:
    def __init__(self):
        self.root = Tk()

        self.container = Frame(self.root)
        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.to_cFrame()
        self.frames["to_fFrame"] = self.to_fFrame()
        self.container.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainFrame")

    def create_main_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        self.Cbutton = Button(
            frame,
            text="To Centigrade",
            bg="yellow",
            command=lambda: self.show_frame("to_cFrame"),
        )
        self.Fbutton = Button(
            frame,
            text="To Fahrenheit",
            bg="pink",
            command=lambda: self.show_frame("to_fFrame"),
        )

        self.label_text1 = Label(
            frame,
            text="Tempture Converter",
        )
        self.Cbutton.grid(
            row=1,
            column=0,
        )
        self.Fbutton.grid(
            row=1,
            column=1,
        )
        self.label_text1.grid(
            row=0,
            column=0,
            columnspan=2,
        )
        return frame

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def to_cFrame(self):
        cframe = Frame(self.container)
        cframe.grid(row=0, column=0, sticky="nsew")
        self.calculuate_button = Button(
            cframe,
            text="Calculuate",
        )
        self.back_button = Button(
            cframe,
            text="Back",
            command=lambda: self.show_frame("MainFrame"),
        )
        self.reset_button = Button(
            cframe,
            text="Reset",
        )
        self.label_text2 = Label(
            cframe,
            text="Enter the tempture in Centigrade",
        )
        self.entry1 = Entry(
            cframe,
        )
        self.label_text3 = Label(
            cframe,
            text="Converted tempture goes here",
        )
        self.calculuate_button.grid(
            row=2,
            column=0,
        )
        self.back_button.grid(
            row=2,
            column=1,
        )
        self.reset_button.grid(
            row=2,
            column=2,
        )
        self.label_text2.grid(
            row=0,
            column=0,
            columnspan=3,
        )
        self.label_text3.grid(
            row=3,
            column=0,
            columnspan=3,
        )
        self.entry1.grid(
            row=1,
            column=0,
            columnspan=3,
        )
        return cframe

    def to_fFrame(self):
        fframe = Frame(self.container)
        fframe.grid(row=0, column=0, sticky="nsew")
        self.calculuate_button = Button(
            fframe,
            text="Calculuate",
        )
        self.back_button = Button(
            fframe,
            text="Back",
            command=lambda: self.show_frame("MainFrame"),
        )
        self.reset_button = Button(
            fframe,
            text="Reset",
        )
        self.label_text2 = Label(
            fframe,
            text="Enter the tempture in Fahrenheit",
        )
        self.entry1 = Entry(
            fframe,
        )
        self.label_text3 = Label(
            fframe,
            text="Converted tempture goes here",
        )
        self.calculuate_button.grid(
            row=2,
            column=0,
        )
        self.back_button.grid(
            row=2,
            column=1,
        )
        self.reset_button.grid(
            row=2,
            column=2,
        )
        self.label_text2.grid(
            row=0,
            column=0,
            columnspan=3,
        )
        self.label_text3.grid(
            row=3,
            column=0,
            columnspan=3,
        )
        self.entry1.grid(
            row=1,
            column=0,
            columnspan=3,
        )
        return fframe

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Converter()
    app.run()
