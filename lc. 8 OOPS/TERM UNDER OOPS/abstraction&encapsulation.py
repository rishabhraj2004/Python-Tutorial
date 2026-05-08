class Car:
    def __init__(self):
        self.accelerator = False #means acc not press
        self.brk = False #means brake not press
        self.clutch = False #means clutch not press
    
    #ye sab nhi ayega output mai ki pehle clutch press karo fir accelerator press karo fir brake press karo
    #this is called abstraction means we hide the internal details and show only the functionality to the user
    
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car started")


car1 = Car()
car1.start()