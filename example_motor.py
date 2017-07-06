import create2api       # iRobot
import time             # sleep function
import os               # filesystem

dir = os.path.dirname(__file__)
configFile = dir+'/config.json'

print '//// Start Connection ////////////////////////////////////////////'
bot = create2api.Create2(configFile)
bot.start()
bot.full()

print '  // Forward'
bot.drive_straight(200)
time.sleep(1)

print '  // Backward'
bot.drive_straight(-200)
time.sleep(1)

print '  // Circle'
velocity = 200
radius = 500
bot.drive(velocity, radius)
time.sleep(1)

print '  // Stop'
bot.drive_straight(0)

bot.reset()
bot.destroy()
