user_in = 1
class Motor:
    cylinders = 4       # amount of cylinders, usually 4 - 8
    cyl_ali = "V"       # cylinder alignment, in S or V
    disp_L = 2.7        # displacement in liters
    torque_lbf = 170    # pulling power, pounds per foot
    hp = 150            # horse power
    gears = 5           # amount of gears, usually 4 - 6
    turbos = 0          # amount of turbos
    bSuperCharge = 1    # 0 has SC
    def ShowStats(self):
        if(self.bSuperCharge == 0):
            self.hp += 80
            self.torque_lbf += 90
            print self.gears,"gear - Super Charged",self.cyl_ali+str(self.cylinders),self.disp_L, "Engine"
        else:
            print self.gears,"gear -",self.cyl_ali+str(self.cylinders),self.disp_L, "L Engine"
        print self.torque_lbf,"Torque Power"
        print self.hp,"Horse Power"
        if(self.turbos >= 1):
            self.hp += (self.turbos*64)
            print self.turbos,"Turbo"


class V8(Motor):
    cylinders = 8       # amount of cylinders, usually 4 - 8
    cyl_ali = "V"       # cylinder alignment, in S or V
    disp_L = 2.7        # displacement in liters
    torque_lbf = 260    # pulling power, pounds per foot
    hp = 270            # horse power
    gears = 6           # amount of gears, usually 4 - 6

class V8Turbo(V8):
    turbos = 2

class V6(Motor):
    cylinders = 6       # amount of cylinders, usually 4 - 8
    cyl_ali = "V"       # cylinder alignment, in S or V
    disp_L = 2.1        # displacement in liters
    torque_lbf = 160    # pulling power, pounds per foot
    hp = 160            # horse power
    gears = 6           # amount of gears, usually 4 - 6

class V6SC(V6):
    bSuperCharge = 0

class S5(Motor):
    cylinders = 5
    cyl_ali = "S"
    disp_L = 2.5
    torque_lbf = 170    # pulling power, pounds per foot
    hp = 175            # horse power
    gears = 5

class S5Turbo(S5):
    turbos = 1

class V4(Motor):
    cylinders = 4
    cyl_ali = "V"
    disp_L = 2.2
    torque_lbf = 150    # pulling power, pounds per foot
    hp = 145            # horse power
    gears = 5

class S4(Motor):
    cylinders = 4
    cyl_ali = "S"
    disp_L = 2.3
    torque_lbf = 145    
    hp = 140            
    top_speed = 120     
    gears = 5

class V2(Motor):
    cylinders = 2
    cyl_ali = "V"
    disp_L = 2.3
    torque_lbf = 130
    hp = 125
    gears = 4

class S2(V2):
    cyl_ali = "S"

class Wheels:
    material = "Steel"  # material wheels made of usually, steel or aluminum
    diameter_in = 15    # diameter of the wheel 
    width_in = 8.5      # width of wheel 
    tire_diam_in = 18   # tire diameter from edge to edge
    tire_width_in = 9.5 # width of tire
    def ShowStats(self):
        print self.diameter_in,"inch by",self.width_in,"inch",self.material,"wheels with",self.tire_diam_in,"inch by",self.tire_width_in,"inch tires"

class SmallWheels(Wheels):
    material = "Aluminum"
    diameter_in = 15    # diameter of the wheel 
    width_in = 7.0      # width of wheel 
    tire_diam_in = 16   # tire diameter from edge to edge
    tire_width_in = 7.5 # width of tire

class MedWheels(Wheels):
    material = "Steel"
    diameter_in = 16    # diameter of the wheel 
    width_in = 7.0      # width of wheel 
    tire_diam_in = 17   # tire diameter from edge to edge
    tire_width_in = 8   # width of tire

class BigWheels(Wheels):
    material = "Steel"
    diameter_in = 18    # diameter of the wheel 
    width_in = 9.0      # width of wheel 
    tire_diam_in = 22   # tire diameter from edge to edge
    tire_width_in = 10   # width of tire

class LargeWheels(Wheels):
    material = "Steel"
    diameter_in = 22    # diameter of the wheel 
    width_in = 11.0     # width of wheel 
    tire_diam_in = 26   # tire diameter from edge to edge
    tire_width_in = 13.5   # width of tire

class Body:
    doors = 4           # doors to enter car
    axels = 2           # amount of axels
    weight_lb = 3500    # weight of body
    seats = 4           # max passengers, may vary
    open_trunk = 1      # 0 is an open trunk, 1 is not.
    susp_in = 0.0       # + or - to lower or raise car    
    length_m = 4.7      # length from tip of hood to back of trunk
    width_m = 1.9       # from side mirror to side mirror
    height_m = 1.6      # bottom of door to top of car, susp does not affect.
    def ShowSpecs(self):
        print self.doors,"Door"
        print "Weights",self.weight_lb,"pounds"
        print "About",self.length_m,"meters long"
        print "About",self.width_m,"meters wide"
        print "About",self.height_m,"meters tall"
        if(self.open_trunk == 0):
            print "Has a big open trunk"
        else:
            print "Has a standard trunk"
    
class Hatchback(Body):
    doors = 2
    weight_lb = 3000
    seats = 5
    open_trunk = 0
    length_m = 4.8
    width_m = 1.8
    height_m = 1.6
    
class Coupe(Body):
    doors = 2
    weight_lb = 2450
    bConvertable = 0    # 0 yes, 1 not convertable
    seats = 4 
    length_m = 4.4
    width_m = 1.8
    height_m = 1.5

class Sedan(Body):
    doors = 4
    weight_lb = 3100
    seats = 5
    length_m = 4.7
    width_m = 1.9
    height_m = 1.6

class SUV(Body):
    doors = 4
    weight_lb = 3600
    seats = 7
    open_trunk = 0
    length_m = 5.7
    width_m = 2.2
    height_m = 2.6
    
class Truck(Body):
    doors = 2
    weight_lb = 4000
    seats = 2
    open_trunk = 0   
    bBed = 0            # 0 has a bed, 1 is false
    bed_len_ft = 0.0    # bed length, if bBed = 1 then this is 0
    susp_in = 6.0    
    length_m = 5.1
    width_m = 2.2
    height_m = 2.8    
    if(bBed == 0):
        bed_len_ft = 5.0

class OneAxel(Body):
    doors = 0
    axels = 1
    weight_lb = 400
    seats = 2
    open_trunk = 1 
    susp_in = 4.0
    length_m = .9
    width_m = .58
    height_m = .42

class Sport_bike(OneAxel):
    weight_lb = 420
    susp_in = 3.0
    length_m = .9
    width_m = .58
    height_m = .42

class Touring_bike(OneAxel):
    weight_lb = 440
    susp_in = 3.0
    length_m = .9
    width_m = .7
    height_m = .6

class Cruiser_bike(OneAxel):
    weight_lb = 440
    susp_in = 3.0
    length_m = .9
    width_m = .7
    height_m = .6
    
class Automobile:
    mnfr = "manufacturer"
    model_name = "model name"
    model_year = 2017
    Engine = Motor()
    Body_type = Body()
    WheelType = SmallWheels()
    top_speed = 150
    drive_train = "FWD"

class Motorcycle(Automobile):
    mnfr = "Harley"
    model_name = "test"
    model_year = 2010
    Engine = Motor()
    Body_type = Body()

class Car(Automobile):
    mnfr = "VW"
    model_name = "test"
    model_year = 2008
    Engine = Motor()
    BodyType = Sedan()
    WheelType = SmallWheels()
    top_speed = 150
    drive_train = "FWD"
    def ShowStats(self):
        print
        print self.model_year,self.model_name,self.drive_train,"by",self.mnfr
        self.BodyType.ShowSpecs()
        self.Engine.ShowStats()
        self.WheelType.ShowStats()
        print

user_car = Car()

def Names():
    user_car.mnfr = raw_input("Enter Manufacturer Name:")
    user_car.model_name = raw_input("Enter Model Name:")
    user_car.model_year = input("Enter Model Year: ")
    user_car.ShowStats()

def chooseDrive():
    print "(1) Front Wheel Drive"
    print "(2) Rear Wheel Drive"
    print "(3) Four Wheel Drive"
    print "(4) start over..."
    user_ch = input("Select drivetrain:")
    if(user_ch == 1):
        user_car.drive_train = "FWD"
    elif(user_ch == 2):
        user_car.drive_train = "RWD"
    elif(user_ch == 3):
        user_car.drive_train = "4WD"
    else:
        Engines()
    Names()
    print

def TypeWheels():
    print "(1) Alloy"
    print "(2) Steel"
    print "(3) Chrome"
    print "(4) Aluminum"
    print "(5) start over..."
    user_ch = input("Select wheel material:")
    if(user_ch == 1):
        user_car.WheelType.material = "Alloy"
    elif(user_ch == 2):
        user_car.WheelType.material = "Steel"
    elif(user_ch == 3):
        user_car.WheelType.material = "Chrome"
    elif(user_ch == 4):
        user_car.WheelType.material = "Aluminum"
    else:
        Engines()
    chooseDrive()
    print
    

def wheels():
    print "(1) Small Wheels"
    print "(2) Medium Wheels"
    print "(3) Big Wheels"
    print "(4) Huge Wheels"
    print "(5) start over..."
    user_ch = input("Select a wheels and tires: ")
    if(user_ch == 1):
        user_car.WheelType = SmallWheels()
    elif(user_ch == 2):
        user_car.WheelType = MedWheels()
    elif(user_ch == 3):
        user_car.WheelType = BigWheels()
    elif(user_ch == 4):
        user_car.WheelType = LargeWheels()
    else:
        Engines()
    TypeWheels()
    print
        
def Bodies():
    print "(1) Coupe"
    print "(2) Hatchback"
    print "(3) Sedan"
    print "(4) Truck"
    print "(5) Sport Bike"
    print "(6) Cruiser Bike"
    print "(7) Touring Bike"
    print "(8) SUV"
    print "(9) start over..."
    user_ch = input("Select a body type: ")
    if(user_ch == 1):
        user_car.BodyType = Coupe()
    elif(user_ch == 2):
        user_car.BodyType = Hatchback()
    elif(user_ch == 3):
        user_car.BodyType = Sedan()
    elif(user_ch == 4):
        user_car.BodyType = Truck()
    elif(user_ch == 5):
        user_car.BodyType = Sport_bike()
    elif(user_ch == 6):
        user_car.BodyType = Cruiser_bike()
    elif(user_ch == 7):
        user_car.BodyType = Touring_bike()
    elif(user_ch == 8):
        user_car.BodyType = SUV()
    else:
        Engines()
    wheels()
    print
    
def Engines():
    global user_car
    user_ch = 1
    print "______________________________"   
    print "#~. PYTHON CREATE-O-MOBILE .~#"
    print "______________________________"
    print "(1) V8"
    print "(2) V8 Turbo "
    print "(3) V6 "
    print "(4) V6 Super Charged"
    print "(5) S5 Turbo"
    print "(6) S5 "
    print "(7) V4 "
    print "(8) S4 "
    print "(9) V2 "
    print "(10) S2"
    user_ch = input("Select an engine: ")
    if(user_ch == 1):
        user_car.Engine = V8()
    elif(user_ch == 2):
        user_car.Engine = V8Turbo()
    elif(user_ch == 3):
        user_car.Engine = V6()
    elif(user_ch == 4):
        user_car.Engine = V6SC()
    elif(user_ch == 5):
        user_car.Engine = S5Turbo()
    elif(user_ch == 6):
        user_car.Engine = S5()
    elif(user_ch == 7):
        user_car.Engine = V4()
    elif(user_ch == 8):
        user_car.Engine = S4()
    elif(user_ch == 9):
        user_car.Engine = V2()
    elif(user_ch == 10):
        user_car.Engine = S2()
    else: Engines()
    Bodies()
    print
Engines()
