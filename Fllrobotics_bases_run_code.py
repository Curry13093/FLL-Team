
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, Matrix

hub = InventorHub()
hub.system.set_stop_button((Button.BLUETOOTH))

# Robot configuration
motorattachmentleft = Motor(Port.B)
motorattachmentright = Motor(Port.D)

motordriveleft = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motordriveright = Motor(Port.E)
print(motorattachmentleft.control.limits())
motorattachmentleft.control.limits(1110, 10000, 190)
print(motorattachmentright.control.limits())
motorattachmentright.control.limits(1110, 10000, 190)
drivebase = DriveBase(motordriveleft, motordriveright, wheel_diameter = 56, axle_track = 80)
drivebase.use_gyro(True)
print(drivebase.settings())
drivebase.settings(400, 500, 300, 600) # straight_speed = 400, straight_acceleration = 500, turn_rate = 300, turn_acceleration = 600)
print(drivebase.heading_control.pid())
drivebase.heading_control.pid(30000, 100, 5300, 2, 10) # kp = 30000, ki = 100, kd = 5300, integral_deadzone = 2, integral_rate = 10, Don't change!
#drivebase.heading_control.pid(3000,200,100,5,10)

Attachment1 = motorattachmentleft
Attachment2 = motorattachmentright

# Wait for IMU to calibrate
hub.light.on(Color.RED)
while not hub.imu.ready(): pass
hub.light.on(Color.MAGENTA)

# ================================ Helper functions ================================

def stopmotors() -> None:
    """Stops all motors to coast.

    """

    motorattachmentleft.stop()
    motorattachmentright.stop()
    drivebase.stop()

def turnto(angle: Number) -> None:
    """Turns to the specified absolute angle.

    Arguments:
        angle (Number, deg): The target angle

    """

    drivebase.turn(angle - hub.imu.heading())

def initrun(angle: Number) -> None:
    """Starts the run by ramming backward into the wall.

    Arguments:
        angle (Number, deg): The angle the robot is initially facing

    """

    hub.system.set_stop_button((Button.CENTER))

    # Drive backwards a bit, unregulated
    motordriveleft.dc(-50)
    motordriveright.dc(-50)
    wait(500)
    drivebase.brake()

    # Reset angles
    hub.imu.reset_heading(angle)
    motordriveleft.reset_angle(0)
    motordriveright.reset_angle(0)
    drivebase.reset()
    motorattachmentleft.reset_angle(0)
    motorattachmentright.reset_angle(0)

def catcherr(err: BaseException) -> bool:
    stopmotors()

    print(repr(err))

    if isinstance(err, SystemExit) and not any(hub.buttons.pressed()):
        # If a SystemExit is triggered but no button was pressed on the hub,
        # it means you clicked the abort button in the IDE

        hub.speaker.beep(50, 50)
        return True

    hub.light.on(Color.RED)
    hub.speaker.beep(100, 50)
    return False

# ================================ Run code ================================

def run1() -> None:
    global runindex

    initrun(0)

    drivebase.straight(300)
    turnto(-45)
    drivebase.straight(250)
    drivebase.straight(-180)
    turnto(0)
    drivebase.straight(460)
    turnto(30)
    drivebase.straight(-40)
    turnto(90)
    drivebase.straight(100)
    drivebase.straight(-100)
    turnto(280)
    drivebase.straight(370)
    turnto(255)
    drivebase.straight(300)
    #drivebase.turn(-3)
    drivebase.straight(-40)
    turnto(210)
    drivebase.straight(-40)
    motorattachmentleft.run_target(100, -230)
    motorattachmentleft.run_target(1110, -600, wait = False)
    drivebase.straight(-60)
    turnto(270)
    drivebase.straight(170)
    motorattachmentright.run_target(1110, -800)
    drivebase.straight(130)
    motorattachmentright.run_target(1110, 0)
    drivebase.straight(200)
    turnto(230)
    drivebase.straight(700)

    runindex += 1

def run2() -> None:
    global runindex

    initrun(0)


    runindex += 1

def run3() -> None:
    global runindex

    initrun(0)
    
    #motorattachmentleft.run_target(1000, 1000)
    drivebase.straight(770)
    drivebase.turn(-90)
    drivebase.straight(170)
    motorattachmentright.run_angle(200, -260)
    drivebase.straight(220)
    drivebase.turn(45)
    drivebase.straight(140)
    motorattachmentleft.run_target(1000, 7000)
    drivebase.straight(-200)
    ##drivebase.turn(-40)
    #drivebase.straight(-200)
    #drivebase.turn(48)
    #drivebase.straight(-700)
    runindex += 1


def run4() -> None:
    global runindex

    initrun(0)
    
    motorattachmentleft.run_angle(100,-50)
    drivebase.straight(550)
    drivebase.turn(93)
    drivebase.straight(350)
    drivebase.straight(-60)
    motorattachmentleft.run_angle(80,-240)
    wait(1000)
    drivebase.straight(-170)
    motorattachmentleft.run_angle(100,300)
    drivebase.turn(92)
    drivebase.straight(2050)   

def run5() -> None:
    global runindex

    initrun(0)
    
    drivebase.straight(200)
    motorattachmentleft.run_angle(1000,200)
    drivebase.straight(-75)
    motorattachmentleft.run_angle(1000,-200)
    drivebase.straight(-100)
    motorattachmentleft.run_angle(1000,200)
    drivebase.straight(-200)
    wait(5000)
    drivebase.turn(-35)
    drivebase.straight(2000)
    drivebase.turn(35)

def run6() -> None:
    global runindex

    initrun(0)

def run7() -> None:
    global runindex

    initrun(0)

    #motorattachmentleft.run_angle(1000,-2300)
    drivebase.straight(655)
    drivebase.turn(45)
    drivebase.straight(500)
    drivebase.straight(-100)
    drivebase.straight(500)
    drivebase.straight(-255)
    drivebase.turn(-90)
  #  motorattachmentright.run_target(1000,1600)
    drivebase.straight(-135)
    motorattachmentright.run_angle(1000,-1000)
    drivebase.straight(-70)
    motorattachmentright.run_angle(1000,-1000)
    drivebase.turn(40)
    drivebase.straight(-800)
    #drivebase.straight(400)
    #drivebase.straight(-200)
    #drivebase.turn(-40)
   # drivebase.straight(-1000)
    
    runindex += 1

# ================================ Image bitmaps ================================

digits = [
    Matrix([[0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0]]) * 100,

    Matrix([[0,0,1,0,0],
            [0,1,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,1,1,1,0]]) * 100,

    Matrix([[0,1,1,1,0],
            [0,0,0,1,0],
            [0,1,1,1,0],
            [0,1,0,0,0],
            [0,1,1,1,0]]) * 100,

    Matrix([[0,1,1,1,0],
            [0,0,0,1,0],
            [0,1,1,1,0],
            [0,0,0,1,0],
            [0,1,1,1,0]]) * 100,

    Matrix([[0,1,0,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0],
            [0,0,0,1,0],
            [0,0,0,1,0]]) * 100,

    Matrix([[0,1,1,1,0],
            [0,1,0,0,0],
            [0,1,1,1,0],
            [0,0,0,1,0],
            [0,1,1,1,0]]) * 100,

    Matrix([[0,1,1,1,0],
            [0,1,0,0,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0]]) * 100,

    Matrix([[0,1,1,1,0],
            [0,0,0,1,0],
            [0,0,1,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0]]) * 100,

    Matrix([[0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0]]) * 100,

    Matrix([[0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0],
            [0,0,0,1,0],
            [0,1,1,1,0]]) * 100,
]

# ================================ Master program ================================

# You can add more runs by adding another entry in the list below
runindex: int = 0
runs = [ # [Icon, Callback]
    [digits[1], run1],
    [digits[2], run2],
    [digits[3], run3],
    [digits[4], run4],
    [digits[5], run5],
    [digits[6], run6],
    [digits[7], run7],
]
numruns: int = len(runs)

# Program is ready
hub.speaker.beep(900, 100)

while True:
    stopmotors()

    # Show selection
    hub.light.on(Color.GREEN)
    hub.display.icon(runs[runindex][0])

    # Wait for button press
    buttons = []
    while not any(buttons): buttons = hub.buttons.pressed()

    if Button.CENTER in buttons:
        # "Run selected" pressed

        hub.speaker.beep(1100, 50)

        # Wait for button released
        while any(hub.buttons.pressed()): pass
        hub.light.on(Color.WHITE)
        hub.display.off()

        try:
            # Do selected run
            runs[runindex][1]()
            stopmotors()
            hub.speaker.beep(800, 50)

        except BaseException as err:
            # An error happened
            if catcherr(err): raise # It was the abort button in the IDE, so end the program

        runindex %= numruns
        hub.system.set_stop_button((Button.BLUETOOTH))
        while Button.CENTER in hub.buttons.pressed(): pass

    elif Button.RIGHT in buttons:
        # "Next" pressed
        runindex = (runindex + 1) % numruns
        wait(200)
        hub.speaker.beep(600, 50)

    elif Button.LEFT in buttons:
        # "Previous" pressed
        runindex = (runindex + numruns - 1) % numruns
        wait(200)
        hub.speaker.beep(550, 50)
