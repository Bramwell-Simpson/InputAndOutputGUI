from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        lbl_title = Label(self, text = "Choose an item below to see the definition")
        lbl_title.grid(row = 0, column = 0, sticky = W, padx = 5)

        item_list = ["Network Interface Card", "Fibre Cable", "Ethernet Cable", "Bridge", "Switch"]
        self.item_str = StringVar()
        item_list_widget = OptionMenu(self, self.item_str, *item_list)
        item_list_widget.grid(row = 1, sticky = W, padx = 5, pady = 10)

        self.definition_text_box = Text(self, width = 40, height = 20, wrap = WORD)
        self.definition_text_box.grid(row = 2, sticky = W, padx = 5, pady = 10)

        btn_submit = Button(self, text = "Get Definition", command = self.get_definition)
        btn_submit.grid(row = 3, sticky = W, padx = 5, pady = 10)

    def get_definition(self):
        self.item_selected = self.item_str.get()

        self.show_message()

    def show_message(self):

        message = ""

        item = self.item_selected

        if item =="Network Interface Card":
            message = "A network interface card (NIC) is a circuit board or card that is installed in a computer so that it can be connected to a network.\nA network interface card provides the computer with a dedicated, full-time connection to a network.\nPersonal computers and workstations on a local area network (LAN) typically contain a network interface card specifically designed for the LAN transmission technology."
        elif item == "Fibre Cable":
            message = "Fiber optic cable is a high-speed data transmission medium. It contains tiny glass or plastic filaments that carry light beams.\n Digital data is transmitted through the cable via rapid pulses of light.\n The receiving end of a fiber optic transmission translates the light pulses into binary values, which can be read by a computer."
        elif item == "Ethernet Cable":
            message = "Ethernet, pronounced \"E-thernet\" (with a long \"e\"), is the standard way to connect computers on a network over a wired connection.\n It provides a simple interface and for connecting multiple devices, such computers, routers, and switches.\n With a single router and a few Ethernet cables, you can create a LAN, which allows all connected devices to communicate with each other.\n A network of computers connected by Ethernet cables are more secure and less prone to interference than wireless connections."
        elif item == "Bridge":
            message = "When a road needs to extend across a river or valley, a bridge is built to connect the two land masses. Since the average car cannot swim or fly, the bridge makes it possible for automobiles to continue driving from one land mass to another.\nIn computer networking, a bridge serves the same purpose. It connects two or more local area networks (LANs) together. The cars, or the data in this case, use the bridge to travel to and from different areas of the network. The device is similar to a router, but it does not analyze the data being forwarded. Because of this, bridges are typically fast at transferring data, but not as versatile as a router.\n For example, a bridge cannot be used as a firewall like most routers can. A bridge can transfer data between different protocols (i.e. a Token Ring and Ethernet network) and operates at the \"data link layer\" or level 2 of the OSI (Open Systems Interconnection) networking reference model."
        elif item == "Switch":
            message = "An ethernet switch is a device used to build a network connection between the attached computers (allows computers to talk to each other).\n It differs from an ethernet hub: While a hub will send incoming data packets to all ports, a switch understands the packets' addressing scheme and will send any data packet only to its destination port, thus limiting the number of collisions (data sent at the same time)."

        self.definition_text_box.delete(0.0, END)
        self.definition_text_box.insert(0.0, message)

window = Tk()
window.title("Network Definitions")
window.geometry("500x500")

app = Application(window)

window.mainloop()