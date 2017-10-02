from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        #Create instuction label
        self.inst_lbl = Label(self, text = "Choose item from the list to get a description and a picture (Picture quality will be low because Tkinter only supports .GIF file extensions for images):")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #Create the list for the dropdown menu
        self.option = StringVar()
        self.IOList = ["Keyboard", "Mouse", "Microphone", "Trackball", "Joystick", "Touch Screen", "XBox Kinect", "Eye Gaze Tracker", "Webcam", "Touchpad", "Monitor", "Speakers", "Printer", "Plotters", "3D Printer", "Sound Card", "Graphics Card"]

        #create the dropdown menu
        self.options = OptionMenu(self, self.option, *self.IOList)
        self.options.grid(row = 1, column = 0, sticky = W)

        #create the 'get description' button
        self.get_desc_bttn = Button(text = "Get Description", command = self.get_description)
        self.get_desc_bttn.grid(row = 1, column = 0, sticky = W)
        
        #create the description text and rebind all the keys to stop editing while the GUI is running
        self.desc_txt = Text(self, width = 50, height = 10, wrap = WORD)
        self.desc_txt.grid(row = 3, column = 0, sticky = W)
        self.re_bind_all_keys()

    def re_bind_all_keys(self):

        self.i = 0 #first loop counter
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m" "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"] #Alphabet for rebinding
        self.j = 0 #second loop conter

        #Loop until 'j' is more than the length of the array letters
        while self.j < len(self.letters):
            self.desc_txt.bind(str(self.letters[self.j]), lambda e: "break")#rebind the letter to 'break'
            self.j += 1

        #loop until i is more than 10, while rebinding the numpad and numbers on the keyboard  
        while self.i < 10:
            self.desc_txt.bind(str(self.i), lambda e: "break")#rebindthe number to 'break'
            self.i += 1

    def get_description(self):
        self.option_chosen = self.option.get()

        if self.option_chosen == "Keyboard":
            message = "A computer keyboard is an input device used to enter characters and functions into the computer system by pressing buttons, or keys. It is the primary device used to enter text. A keyboard typically contains keys for individual letters, numbers and special characters, as well as keys for specific functions"
            self.img = PhotoImage(file = "Keyboard.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Mouse":
            message = "A computer mouse is an input device that is most often used with a personal computer. Moving a mouse along a flat surface can move the on-screen cursor to different items on the screen."
            self.img = PhotoImage(file = "Mouse.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Trackball":
            message = "A trackball is a pointing device consisting of a ball held by a socket containing sensors to detect a rotation of the ball about two axis—like an upside-down mouse with an exposed protruding ball. It is mostly used by CAD software users for more accuracy."
            self.img = PhotoImage(file = "Trackball.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)

        elif self.option_chosen == "Microphone":
            message = "A microphone is a object which takes sound waves from the user, converts them to electrical signals, for transportation across a computer or network, and either outputs them on speakers to a friend, or records it as a audio file. The microphone shown below is a favourite of the russian Counter-Strike gamers"
            self.img = PhotoImage(file = "MicroPhone.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Joystick":
            message = "A joystick is a cursor control device used in computer games and assistive technology . The joystick, which got its name from the control stick used by a pilot to control the ailerons and elevators of an airplane, is a hand-held lever that pivots on one end and transmits its coordinates to a computer."
            self.img = PhotoImage(file = "Joystick.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Touch Screen":
            message = "A touch screen is a computer display screen that is also an input device. The screens are sensitive to pressure; a user interacts with the computer by touching pictures or words on the screen. Resistive touch screen panels are not affected by outside elements such as dust or water."
            self.img = PhotoImage(file = "Touchscreen.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "XBox Kinect":
            message = "The Xbox Kinect (codenamed Project Natal during dev.) is technology which can see and hear XBox users. Kinect uses a camera which has a depth sensor and a infrared projecter with a monochrome CMOS sensor which sees the enviroment not as a flat enviroment, but as dots arranged in a 3D enviroment."
            self.img = PhotoImage(file = "Kinect.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Eye Gaze Tracker":
            message = "Eye tracking is the process of measuring either the point of gaze (where one is looking) or the motion of an eye relative to the head. An eye tracker is a device for measuring eye positions and eye movement. Used in games when the user needs to look around, 'Elite Dangerous' supports this kind of eye tracking"
            self.img = PhotoImage(file = "EyeTracker.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Webcam":
            message = "A webcam is a video camera that feeds or streams its image in real time to or through a computer to a computer network. When \"captured\" by the computer, the video stream may be saved, viewed or sent on to other networks via systems such as the internet, and emailed as an attachment."
            self.img = PhotoImage(file = "Webcam.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Touchpad":
            message = "A touch pad is a device for pointing (controlling input positioning) on a computer display screen. It is an alternative to the mouse. Originally incorporated in laptop computers, touch pads are also being made for use with desktop computers. A touch pad works by sensing the user's finger movement and downward pressure."
            self.img = PhotoImage(file = "Touchpad.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Monitor":
            message = " A display screen used to provide visual output from a computer, cable box, video camera, VCR or other video generating device. Computer monitors use CRT and LCD technology, while TV monitors use CRT(Cathode Ray Tube, only for ancient computers), LCD and plasma technologies."
            self.img = PhotoImage(file = "Monitor.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)

        elif self.option_chosen == "Speakers":
            message = "Speakers are output devices used with computer systems. They receive audio input from the computer's sound card and produce audio output in the form of sound waves"
            self.img = PhotoImage(file = "Speakers.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)

        elif self.option_chosen == "Printer":
            message = "A printer is a device that accepts text and graphic output from a computer and transfers the information to paper, usually to standard size sheets of paper. Printers vary in size, speed, sophistication, and cost. In general, more expensive printers are used for higher-resolution color printing"
            self.img = PhotoImage(file = "Printer.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Plotters":
            message = "The plotter is a computer printer for printing vector graphics. In the past, plotters were used in applications such as computer-aided design, though they have generally been replaced with wide-format conventional printers. A plotter gives a hard copy of the output."
            self.img = PhotoImage(file = "Plotter.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "3D Printer":
            message = "3D printing, also known as additive manufacturing (AM), refers to processes used to create a three-dimensional object in which layers of material are formed under computer control to create an object."
            self.img = PhotoImage(file = "3DPrinter.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Sound Card":
            message = "Most of your music collection is probably in digital format, either on CDs or as files on your computer. In order to be able to listen to your music, a sound card converts digital data to analog sound waves you can hear. The output signal is then connected to a headphone or set of speakers."
            self.img = PhotoImage(file = "SoundCard.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        elif self.option_chosen == "Graphics Card":
            message = "A video card connects to the motherboard of a computer system and generates output images to display. Video cards are also referred to as graphics cards. Video cards include a processing unit, memory, a cooling mechanism and connections to a display device"
            self.img = PhotoImage(file = "GTX1080.gif")
            self.img_lbl = Label(image = self.img)
            self.img_lbl.grid(row = 4, column = 0, sticky = W)
            
        self.desc_txt.delete(0.0, END)
        self.desc_txt.insert(0.0, message)

#Main
root = Tk()
root.geometry("800x500")
root.title("Input and Output devices")

app = Application(root)

root.mainloop()
