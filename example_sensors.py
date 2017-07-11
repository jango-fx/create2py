import create2api       # iRobot
import json             # JSON Files
import time             # sleep function
import os               # filesystem

dir = os.path.dirname(__file__)
configFile = dir+'/config.json'

print '//// Start Connection ////////////////////////////////////////////'
#bot = create2api.Create2()
bot = create2api.Create2('/dev/cu.usbserial-DA01NWTC', 115200)
bot.start()
# bot.safe()

# # # # # # # # # # INIFINITE LOOP # # # # # # # # # # # # # # # # # # # #
while True:
    print '//// Getting Sensor Data /////////////////////////////////////////'
    bot.get_packet(100)
    sensorDataString = json.dumps(bot.sensor_state, indent=4, sort_keys=False)
    print '  RAW DATA: --------------------------------------'
    print sensorDataString
    print '  ------------------------------------------------'

    sensorDataDict = json.loads(sensorDataString)
    robotAngle = sensorDataDict['angle']
    print robotAngle

    if robotAngle > 10:
        print '+ + + Angle is larger than 10 + + +'
    if robotAngle < -10:
        print '- - - Angle is smaller than -10 - - -'

    time.sleep(0.25)
