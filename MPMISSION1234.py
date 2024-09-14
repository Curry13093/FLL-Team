from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, Matrix
import math

# Initialize hub and set stop button
hub = InventorHub()
hub.system.set_stop_button((Button.BLUETOOTH))

# Robot configuration
motorattachmentleft = Motor(Port.F)
motorattachmentright = Motor(Port.B)
motordriveleft = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motordriveright = Motor(Port.E)
drivebase = DriveBase(motordriveleft, motordriveright, wheel_diameter=56, axle_track=80)

# Attachment motors
Attachment1 = motorattachmentleft
Attachment2 = motorattachmentright

# Gyro calibration and initialization
hub.light.on(Color.RED)
while not hub.imu.ready(): pass
hub.light.on(Color.MAGENTA)
hub.imu.reset_heading(0)

# Helper functions
def stopmotors() -> None:
    """Stops all motors to coast."""
    motorattachmentleft.stop(Stop.COAST)
    motorattachmentright.stop(Stop.COAST)
    drivebase.stop(Stop.COAST)

def turnto(angle: float, speed: int = 100) -> None:
    """Turns to the specified absolute angle using gyro heading."""
    target_angle = angle - hub.imu.heading()
    if target_angle < -180:
        target_angle += 360
    elif target_angle > 180:
        target_angle -= 360
    drivebase.turn(target_angle, speed)

def initrun(angle: float) -> None:
    """Initializes the run by resetting sensors and driving backwards."""
    hub.system.set_stop_button((Button.CENTER))
    motordriveleft.dc(0)
    motordriveright.dc(0)
    wait(500)
    drivebase.brake()

    # Reset angles and drivebase
    hub.imu.reset_heading(angle)
    drivebase.reset()
    motorattachmentleft.reset_angle(0)
    motorattachmentright.reset_angle(0)

def catcherr(err: BaseException) -> bool:
    """Error handler for robot functions."""
    stopmotors()
    print(repr(err))
    if isinstance(err, SystemExit) and not any(hub.buttons.pressed()):
        hub.speaker.beep(50, 50)
        return True
    hub.light.on(Color.RED)
    hub.speaker.beep(100, 50)
    return False

# ================================ Run Code ================================

def run1() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run2() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run3() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run4() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run5() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run6() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run7() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run8() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run9() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

def run10() -> None:
    global runindex
    initrun(0)
    # Add specific movements here
    runindex += 1

# Image bitmaps for display
digits = [
    Matrix([[0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,1,1,1,0]]) * 100,
    # Add more digit matrices here...
]

# ================================ Master Program ================================

runindex = 0
runs = [
    [digits[0], run1],
    [digits[1], run2],
    [digits[2], run3],
    [digits[3], run4],
    [digits[4], run5],
    [digits[5], run6],
    [digits[6], run7],
    [digits[7], run8],
    [digits[8], run9],
    [digits[9], run10],
]
numruns = len(runs)

hub.speaker.beep(900, 100)

while True:
    stopmotors()
    hub.light.on(Color.GREEN)
    hub.display.icon(runs[runindex][0])

    buttons = []
    while not any(buttons):
        buttons = hub.buttons.pressed()

    if Button.CENTER in buttons:
        hub.speaker.beep(1100, 50)
        while any(hub.buttons.pressed()): pass
        hub.light.on(Color.WHITE)
        hub.display.off()

        try:
            runs[runindex][1]()
            stopmotors()
            hub.speaker.beep(800, 50)
        except BaseException as err:
            if catcherr(err):
                raise

        runindex %= numruns
        hub.system.set_stop_button((Button.BLUETOOTH))
        while Button.CENTER in hub.buttons.pressed(): pass

    elif Button.RIGHT in buttons:
        runindex = (runindex + 1) % numruns
        wait(200)
        hub.speaker.beep(600, 50)

    elif Button.LEFT in buttons:
        runindex = (runindex + numruns - 1) % numruns
        wait(200)
        hub.speaker.beep(550, 50)
