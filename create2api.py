import json
import serial
import struct

#first thing we want to do is load up our config file with our opcodes and other data.

configFileName = 'config.json'
configData = None
baud = 115200

class Error(Exception):
    """Error"""
    pass
    
class ROIDataByteError(Error):
    """Exception raised for errors in ROI data bytes.
    
        Attributes:
            msg -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

class ROIFailedToSendError(Error):
    """Exception raised when an error in data bytes prevented a packet to be sent
    
        Attributes:
            msg -- explanation of the error    
    """
    def __init__(self, msg):
        self.msg = msg


with open(configFileName, 'r') as fileData:
    try:
        json.load(fileData, configData)
        print 'Loaded config and opcodes'
    except ValueError, e:
        print 'shits fucked up yo. No config and data'
        
class SerialCommandInterface(object):
    """This class handles sending commands to the Create2.
    
    """
    
    def __init__(self):
        self.ser = serial.Serial(0)
        self.ser.baudrate = baud
        print self.ser.name
        if self.ser.isOpen(): 
            #print "port was open"
            self.ser.close()
        self.ser.open()
    
    def send(self, opcode, data):
        if data = None
            #Sometimes opcodes don't need data.
        
        sendRaw(data)
    
    def sendRaw(self, data):
        #This converts your nice human readable data into the necesary serial data.
        self.ser.write()
        
class Create2(object):
    """The top level class for controlling a Create2.
        This is the only class that outside scripts should be interacting with.    
    
    """
    
    def __init__(self):
        #Nothing yet
        self.SCI = SerialCommandInterface()
    
    def start():
        SCI.send(configData['opcodes']['start'], None)
        
    def reset():
        SCI.send(configData['opcodes']['reset'], None)
        
    def stop():
        SCI.send(configData['opcodes']['stop'], None)
        
    def baud(baudRate):
        baud_dict = dict(
            300 = 0,
            600 = 1,
            1200 = 2,
            2400 = 3,
            4800 = 4,
            9600 = 5,
            14400 = 6,
            19200 = 7,
            28800 = 8,
            38400 = 9,
            57600 = 10,
            115200 = 11
            )
        if baudRate in baud_dict:
            SCI.send(configData['opcodes']['baud'], baud_dict[baudRate])
        else:
            raise ROIDataByteError("Invalid buad rate")
    
    
    def safe():
        SCI.send(configData['opcodes']['safe'], None)
    
    def full():
        SCI.send(configData['opcodes']['full'], None)
    
    def clean():
        SCI.send(configData['opcodes']['clean'], None)
    
    def max():
        SCI.send(configData['opcodes']['max'], None)
    
    def spot():
        SCI.send(configData['opcodes']['spot'], None)
    
    def seek_dock():
        SCI.send(configData['opcodes']['seek_dock'], None)
    
    def power():
        SCI.send(configData['opcodes']['power'], None)
    
    def schedule():  ####SKIPPED THIS ONE GODDAMMIT
        #SCI.send(configData['opcodes']['start'],0)
    
    def set_day_time(day, hour, minute):
        """Sets the Create2's clock
            
            Args:
                day: A string describing the day. Assumes all lowercase letters.
                hour: A number from 0-23 (24 hour format)
                minute: A number from 0-59
        """
        data = []
        noError = True
        
        day_dict = dict(
            sunday = 0,
            monday = 1,
            tuesday = 2,
            wednesday = 3,
            thursday = 4,
            friday = 5,
            saturday = 6
            )
        
        if day in day_dict:
            data[0] = day
        else:
            noError = False
            raise ROIDataByteError("Invalid day input")
        
        if hour >= 0 and hour <= 23:
            data[1] = hour
        else:
            noError = False
            raise ROIDataByteError("Invalid hour input")
        
        if minute >= 0 and minute <= 59:
            data[2] = minute
        else:
            noError = False
            raise ROIDataByteError("Invalid minute input")
            
        if noError:
            #SCI.send(configData['opcodes']['start'],0)
        else
            raise ROIFailedToSendError("Invalid data, failed to send")
    
    def drive(velocity, radius): 
        """Controls the Create 2's drive wheels.
        
            Args:
                velocity: A number between -500 and 500. Units are mm/s. 
                radius: A number between -2000 and 2000. Units are mm.
                    Drive straight: 32767
                    Turn in place clockwise: -1
                    Turn in place counterclockwise: 1
        """
        noError = True
        data = []
        v = None
        r = None

        #Check to make sure we are getting sent valid velocity/radius.
        if velocity >= -500 and velocity <= 500:
            v = int(velocity) & 0xffff
            #Convert 16bit velocity to Hex
        else:
            noError = False
            raise ROIDataByteError("Invalid velocity input")
        
        if radius >= -2000 and radius <= 2000:
            r = int(radius) & 0xffff
            #Convert 16bit radius to Hex
        else:
            noError = False
            raise ROIDataByteError("Invalid radius input")

        if noError:
            data = struct.unpack('4B', struct.pack('>2H', velocity, radius))
            #An example of what data looks like:
            #print data >> (255, 56, 1, 244)
            
            #data[0] = Velocity high byte
            #data[1] = Velocity low byte
            #data[2] = Radius high byte
            #data[3] = Radius low byte
            
            SCI.send(configData['opcodes']['drive'], data)
        else
            raise ROIFailedToSendError("Invalid data, failed to send")
        
    
    def drive_direct():
        #SCI.send(configData['opcodes']['start'],0)
    
    def drive_pwm():
        #SCI.send(configData['opcodes']['start'],0)
    
    def motors():
        #SCI.send(configData['opcodes']['start'],0)
    
    def motors_pwm():
        #SCI.send(configData['opcodes']['start'],0)
    
    def led():
        #SCI.send(configData['opcodes']['start'],0)
    
    def scheduling_led():
        #SCI.send(configData['opcodes']['start'],0)
    
    def digit_led_raw():
        #SCI.send(configData['opcodes']['start'],0)
    
    def buttons():
        #SCI.send(configData['opcodes']['start'],0)
    
    def digit_led_ascii():
        #SCI.send(configData['opcodes']['start'],0)
    
    def song():
        #SCI.send(configData['opcodes']['start'],0)
    
    def play():
        #SCI.send(configData['opcodes']['start'],0)
    
    def sensors():
        #SCI.send(configData['opcodes']['start'],0)
    
    def query_list():
        #SCI.send(configData['opcodes']['start'],0)
    
    def stream():
        #SCI.send(configData['opcodes']['start'],0)
    
    def pause_resume_stream():
        #SCI.send(configData['opcodes']['start'],0)

        






