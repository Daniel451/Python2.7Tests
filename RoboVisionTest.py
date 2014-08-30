'''
Created on 23.08.2014

@author: daniel
'''


import math
import time
import random
import numpy

from threading import Timer
import datetime


class RoboVisionTest:
    
    
    # Script executions
    script_execs = 0
    
    # Ball information
    ball_move = False  # Does the ball move?
    ball_v_moveDirection = "left"  # does it move left or right on v
    ball_u_moveDirection = "forwards"  # does it move plus or minus on u? forwards -> plus, backwards -> minus
    ball_u = 1000  # vertical distance ( plus = in front of robot | minus = behind the robot | 0 = center )
    ball_v = 1  # horizontal distance ( plus = on the right | minus = on the left | 0 = center )
    ball_u_add = 0  # recorded u change
    ball_v_add = 0  # recorded v change
    ball_u_past = 1000  # last u value
    ball_v_past = 0  # last v value
    ball_angle = 1  # angle under which the ball is seen
    ball_rating = 0  # reliability of the information
    
    # Noisy ball information
    ball_noisy_u = 1000
    ball_noisy_v = 1
    ball_noisy_angle = 1
    global_noise = 1
    
    # Filtered ball information
    ball_filtered_u = 1000
    ball_filtered_v = 1
    ball_filtered_angle = 1
    ball_filter_puffer_u = []
    ball_filter_puffer_v = []
    
    # Debugging
    logPuffer = ""  # String, which is filled up with logging infos
        
        
        
    def __init__(self):
        
        logfile = open("infos.log", "w")
        logstring = "+++++++++++++++++++++++++++++++++++++++++\n" 
        logstring += "++++ New Execution of RoboVisionTest ++++\n"
        logstring += "+++++++++++++++++++++++++++++++++++++++++\n\n"
        logfile.write(logstring)
        logfile.close()



    def main(self):
        
        # Inc script executions
        self.script_execs += 1
        
        # Calculate new ball information
        self.calcRandomBall()
        
        # Filter noisy data
        self.filterDataMain()
        
        # Write Debug information
        self.debugInfos()


    
    # Filter noisy data
    def filterDataMain(self):
        
        # Fill the buffers
        self.ball_filter_puffer_u = self.fillBuffer(self.ball_filter_puffer_u, self.ball_noisy_u)
        self.ball_filter_puffer_v = self.fillBuffer(self.ball_filter_puffer_v, self.ball_noisy_v)
        
        
        # Calculate filtered info
        self.ball_filtered_u = self.calculateFilteredInfo(self.ball_filtered_u, self.ball_filter_puffer_u , self.ball_noisy_u)
        self.ball_filtered_v = self.calculateFilteredInfo(self.ball_filtered_v, self.ball_filter_puffer_v , self.ball_noisy_v)
        self.ball_filtered_angle = math.degrees(math.atan2(self.ball_filtered_v, self.ball_filtered_v))        



    def calculateFilteredInfo(self, item, buffer, noisyballinfo):
        # does the buffer have more than 1 entry?
            if len(buffer) > 1:
                
                if len(buffer) <= 5:
                    return self.filterInfo(item, buffer, noisyballinfo)
                    
                else:
                    # calculate mean
                    mean = 0.0
                    for bufferitem in buffer:
                        mean += bufferitem
                    mean = mean / float(len(buffer))
                    return mean
                
            else:
                # simply set filtered data to noisy data if only 1 dataset is present
                return noisyballinfo



    def filterInfo(self, item, buffer, noisyballinfo):
        # Filter the information
        stdDev = numpy.std(buffer)
        localBuffer = []
        
        for thingy in buffer:
            if math.fabs(thingy - stdDev) > 0:
                localBuffer.append(thingy)
        
        localBuffer = numpy.mean(localBuffer)
            
        return localBuffer

        
    def fillBuffer(self, item, noisyballinfo):
        
        # if u buffer is not full
        if len(item) < 5:
            item.append(noisyballinfo)
            return item
            
        # delete oldest entry in buffer and append new one
        else:
            item.pop(0)
            item.append(noisyballinfo)
            return item
        
    

    def calcRandomBall(self):
        
        # Does the ball move?
        numb = random.randint(1, 100)
        
        if self.ball_move == True and numb > 30:
            numb -= 30
        
        if numb <= 75:  # yes 
            self.ball_move = True
            # Global noise value from 0.650 to 1.350 - higher global noise when ball moves
            self.global_noise = float(random.randint(650, 1350)) / 1000.0
        else:  # no
            self.ball_move = False
            # Global noise value from 0.800 to 1.200 - lower global noise when ball stands still
            self.global_noise = float(random.randint(800, 1200)) / 1000.0
            
        
        
        # Cancel & return if ball doesnt move    
        if not self.ball_move:
            
            # Ball rating
            # random rating from 0 to 25 when ball stands still
            # and multiplied with global_noise to increase/decrease noise by -30% to +30%
            self.ball_rating = random.random() * 15 * self.global_noise
            
            # Ball u noisy
            # ball_u * global_noise * individual noise
            self.ball_noisy_u = self.ball_u * self.global_noise * float(random.randint(900, 1100)) / 1000.0
            
            # Ball v noisy
            # ball_v * global_noise * individual noise
            self.ball_noisy_v = self.ball_v * self.global_noise * float(random.randint(900, 1100)) / 1000.0
            
            # Ball u noisy
            # ball_u * global_noise * individual noise
            self.ball_noisy_angle = self.ball_angle * self.global_noise * float(random.randint(900, 1100)) / 1000.0
            
            # cancel all other things
            return
        
        
        # Does the ball move left or right?
        numb = random.randint(1, 100)
        
        # higher chance to continue moving in the same direction
        v_threshold = 50
        if self.ball_v_moveDirection == "left":
            v_threshold += 45
        else:
            v_threshold -= 45
        
        # Calculate new v direction
        if numb <= v_threshold:
            self.ball_v_moveDirection = "left"
        else:
            self.ball_v_moveDirection = "right"
        
            
        # Does the ball move forwards or backwards?
        numb = random.randint(1, 100)
        
        u_threshold = 50
        if self.ball_u_moveDirection == "backwards":
            u_threshold += 45
        else:
            u_threshold -= 45
        
        # Calculate new u direction
        if numb <= u_threshold:
            self.ball_u_moveDirection = "backwards"
        else:
            self.ball_u_moveDirection = "forwards"
        
        
        # calculate new ball positions
        self.ball_u_add = random.randint(1, 200)  # Amount of u movement 
        self.ball_v_add = random.randint(1, 200)  # Amount of v movement 
        
        # positive or negative v movement
        if self.ball_v_moveDirection == "left":
            self.ball_v_add *= -1
            
        # positive or negative u movement
        if self.ball_u_moveDirection == "backwards":
            self.ball_u_add *= -1
        
        # Set new positions & update past positions
        self.ball_u_past = self.ball_u  # update past u value
        self.ball_v_past = self.ball_v  # update past v value
        self.ball_u += self.ball_u_add  # set new u value
        self.ball_v += self.ball_v_add  # set new v value
        
        # Set new noisy data
        self.ball_noisy_u = self.ball_u * self.global_noise * float(random.randint(850, 1150)) / 1000.0
        self.ball_noisy_v = self.ball_v * self.global_noise * float(random.randint(850, 1150)) / 1000.0
        self.ball_noisy_angle = math.degrees(math.atan2(self.ball_noisy_v, self.ball_noisy_u))
        
        
        self.ball_angle = math.degrees(math.atan2(self.ball_v, self.ball_u))
        self.ball_rating = random.random() * 25 * self.global_noise
       
       
        
    def debugInfos(self):
        
        self.writeLogInfos("Script executions", self.script_execs)
        
        self.logPuffer += "----------------------------------------\n"
        
        self.writeLogInfos("Ball", "direction=" + self.spacer(self.ball_v_moveDirection
                           + "/" + self.ball_u_moveDirection)
                           + " | move=" + self.spacer(self.ball_move))
        
        self.writeLogInfos("Ballinfo u", "u=" + self.spacer(self.ball_u) + " | u_add=" + self.spacer(self.ball_u_add)
                           + " | u_old=" + self.spacer(self.ball_u_past))
        
        self.writeLogInfos("Ballinfo v", "v=" + self.spacer(self.ball_v) + " | v_add=" + self.spacer(self.ball_v_add)
                           + " | v_old=" + self.spacer(self.ball_v_past))
        
        self.writeLogInfos("Ballinfos", "angle=" + self.spacer(self.ball_angle) + " | rating=" + self.spacer(self.ball_rating))
        
        self.logPuffer += "----------------------------------------\n"
        
        self.writeLogInfos("Global noise", str(self.global_noise) + " ( ~" + str(int(self.global_noise * 100)) + "% of real values )")
        
        self.writeLogInfos("Ballinfo noisy u", self.spacer(int(self.ball_noisy_u)) + " | u_diff="
                           + self.spacer(int(self.ball_noisy_u - self.ball_u))
                           + " | " + str(int((100.0 / float(self.ball_u) * float(self.ball_noisy_u)))) + "% from real u")
        
        self.writeLogInfos("Ballinfo noisy v", self.spacer(int(self.ball_noisy_v)) + " | v_diff="
                           + self.spacer(int(self.ball_noisy_v - self.ball_v))
                           + " | " + str(int((100.0 / float(self.ball_v) * float(self.ball_noisy_v)))) + "% from real v")
        
        self.writeLogInfos("Ballinfo noisy angle", self.spacer(int(self.ball_noisy_angle)) + " | angle_diff="
                           + self.spacer(int(self.ball_noisy_angle - self.ball_angle))
                           + " | " + str(int((100.0 / float(self.ball_angle) * float(self.ball_noisy_angle)))) + "% from real angle")
        
        self.logPuffer += "----------------------------------------\n"
        
        self.writeLogInfos("Filtered Ball u", self.ball_filtered_u)
        self.writeLogInfos("Filtered Ball v", self.ball_filtered_v)
        self.writeLogInfos("Filtered Ball angle", self.ball_filtered_angle)
        
        with open("infos.log", "a+") as logfile:
            logfile.write("============================================================\n")
            logfile.write(self.logPuffer)
            
        self.logPuffer = ""
    
    
    
    def spacer(self, string):
        
        string = str(string)
        
        try:
            if int(string) >= 0:
                string = " " + str(string)
        except:
            pass
        
        while len(string) < 7:
            string = string + " "
        
        return string
    
    
    
    def writeLogInfos(self, ikey, ival):
        timeinfo = datetime.datetime.now().strftime("%H:%M:%S")
        self.logPuffer += "[" + str(timeinfo) + "] "
        self.logPuffer += str(ikey) + ": " + str(ival) + "\n"



Robo = RoboVisionTest()    
        
while True:
    Robo.main()
    time.sleep(1)
