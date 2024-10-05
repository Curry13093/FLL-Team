
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
drivebase = DriveBase(motordriveleft, motordriveright, wheel_diameter = 56, axle_track = 80)
drivebase.use_gyro(False)
wait(1)
drivebase.use_gyro(True)
drivebase.heading_control.pid(3000,200,100,5,10)


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

def run2() -> None:
    global runindex

    initrun(0)
    #motorattachmentleft.run_target(1000,-1000)
    #motorattachmentright.run_angle(1000,-1000)
    drivebase.straight(300)
    drivebase.turn(-50)
    drivebase.straight(350)
    drivebase.straight(-250)
    drivebase.turn(50)
    drivebase.straight(480)
    drivebase.turn(45)
    drivebase.straight(-50)
    drivebase.turn(45)
    drivebase.straight(200)
    drivebase.straight(-200)
    drivebase.turn(190)
    drivebase.straight(372)
    drivebase.turn(-10)
    drivebase.straight(320)
    #drivebase.turn(-3)
    drivebase.straight(-240)
    drivebase.turn(-40)
    motorattachmentleft.run_angle(100,-600)
    drivebase.turn(57)
    drivebase.straight(300)
    motorattachmentright.run_angle(1700,-800)
    #drivebase.straight(10)
    drivebase.straight(120)
    motorattachmentright.run_target(1000,200)
    drivebase.turn(-40)
    drivebase.straight(500)
    drivebase.turn(-35)
    drivebase.straight(100000)
  #  drivebase.turn(-55)
  #  drivebase.straight(700)
    #drivebase.turn(7)
    #drivebase.straight(240)
    #drivebase.turn(10)
    #motorattachmentleft.run_target(1000,1000)
    #motorattachmentleft.run_angle(1000,-1000)
    #drivebase.turn(-10)
    #drivebase.straight(30)
    #drivebase.turn(7)
    #drivebase.straight(140)
    #drivebase.turn(-30)
    #drivebase.straight(400)
    #drivebase.turn(-50)
    #drivebase.straight(600)
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
