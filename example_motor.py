import create2api       # iRobot
import time             # sleep function
import os               # filesystem

dir = os.path.dirname(__file__)
configFile = dir+'/create2api/config.json'

print '//// Start Connection ////////////////////////////////////////////'
bot = create2api.Create2('/dev/cu.usbserial-DA01NWTC', 115200, configFile)
bot.start()
bot.full()

print '  // Forward'
bot.drive_straight(200)
time.sleep(0.5)

print '  // Backward'
bot.drive_straight(-200)
time.sleep(0.5)

print '  // Circle Left'
velocity = 200
radius = 50
bot.drive(velocity, radius)
time.sleep(0.75)

print '  // Circle Backward'
velocity = -200
radius = 50
bot.drive(velocity, radius)
time.sleep(0.75)

print '  // Circle Right'
velocity = 200
radius = -50
bot.drive(velocity, radius)
time.sleep(0.75)

print '  // Stop'
bot.drive_straight(0)
time.sleep(0.2)

bot.reset()
bot.destroy()
