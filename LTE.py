import math
import random

class Location:#location in a grid 500 miles x 500 miles [not enforcing the limits]
    def __init__(self, x, y):
        self.coordinate = (x,y)
    def __str__(self):
        return str(self.coordinate)
    def __getitem__(self, index):
        return self.coordinate[index]
    def __str__ (self):
        str1 = str(self.coordinate)
        return str1   
        
class eNB: 
    def __init__(self, node_id, location, SRRI, noise):
        self.node_id = node_id
        self.location = location
        self.SRRI = SRRI#dB
        self.noise = noise#dB
        self.SNR = self.SRRI-self.noise#SNR in dB
        
    def __str__ (self):
        str1 = 'node_id:'+str(self.node_id) +"Location: "+str(self.location)\
               +" SRRI: "+str(self.SRRI)+ " dB   Noise:"+ str(self.noise)+" dB"
        return str1
    
    
class UE:
    def __init__(self, location, final_location, speed,BS_id):
        self.location = location
        self.final_location = final_location
        self.speed = speed
        self.BS_id = BS_id
        self.llastBS = 0
        self.lastBS = 0
        self.pingpang_times =0

    def handover(self,aim_BS_id):
        if self.lastBS == aim_BS_id  and self.lastBS != self.BS_id:    #and self.BS_id == self.llastBS
            self.pingpang_times +=1
            print('******this appened pingpang handover********')
        self.llastBS = self.lastBS
        self.lastBS = self.BS_id
        self.BS_id = aim_BS_id

    def move_in_second(self):
        # self.location = Location(self.location[0] + math.sqrt(2)*random.randint(-1,1)*self.speed*1000/3600,
        #                          self.location[1] + math.sqrt(2)*random.randint(-1,1)*self.speed*1000/3600)
        self.location = Location(self.location[0] + math.sqrt(2) *random.randint(-1,1)* self.speed * 1000 / 3600,
                                 self.location[1] + math.sqrt(2) *random.randint(-1,1)* self.speed * 1000 / 3600)
        
    def __str__ (self):
        str1 = 'BS_ID:'+str(self.BS_id)+" Initial Location: "+str(self.location)+\
               ' lastBS:'+str(self.lastBS)+' llastBS:'+str(self.llastBS)+" Speed:"+ str(self.speed)+" MPH"
        return str1