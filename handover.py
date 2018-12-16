# -*- coding: utf-8 -*-
# @Time    : 18/6/25 下午 9:12
# @Author  : Ji
# @File    : handover.py
# @Software: PyCharm

from LTE import *
import numpy as np
import random
import math
import matplotlib.pyplot as plt

NUM_STATIONS = 15 # number of cellular stations

# possible of noise and signal strength and computation of SNR obtained from information page below
# http://www.speedguide.net/faq/how-to-read-rssisignal-and-snrnoise-ratings-440


SRRI_RANGE = range(-50, 1)  # range of average signal stength in dB
NOISE_RANGE = range(-120, -80)  # range of noise level in dB

LOCATION_X = range(0, 500)  # 0 to 500 possible x coordinates
LOCATION_Y = range(0, 500)  # 0 to 500 possible x coordinates

SPEED_RANGE = range(0, 16)
STATIONS = []

Path_loss_exponent =1.6
power = 23

time_simult = 0
# SimultRunTime = 3000
HANDOVER_TIMES = 0
PINGPANG_TIMES = 0

random.seed(2)


def distance(location1,location2):
    dis = math.sqrt((location1.coordinate[0]-location2.coordinate[0])**2 +
                    (location1.coordinate[1]-location2.coordinate[1])**2)
    return dis

def calcultRSSI(d,power):
    temp = math.log(d,10) * (10**Path_loss_exponent) + power
    return (temp)

# random locations, signal strength and noise. SNR is the difference between the two
# def generateStations():
for _ in range(NUM_STATIONS):
    pos = Location(random.choice(LOCATION_X), random.choice(LOCATION_Y))
    srri = random.choice(SRRI_RANGE)
    noise = random.choice(NOISE_RANGE)
    STATIONS.append(eNB(_, pos, srri, noise))

locationset_x = []
locationset_y = []
for bs in STATIONS:
    locationset_x.append(bs.location[0])
    locationset_y.append(bs.location[1])
    print(bs)

# plt.plot(locationset_x,locationset_y, marker = '*')
# plt.show()

def NeedHandover(ue):
    result = -1
    currentRssi = 0
    for eNB in STATIONS:
        if eNB.node_id == ue.BS_id:
            d = distance(eNB.location, ue.location)
            currentRssi = calcultRSSI(d,power)
            # print('       CurrentRssi:'+str(currentRssi))
            # print('       CurrentDistance:'+str(d))
    for eNB in STATIONS:
        if eNB.node_id != ue.BS_id:
            d = distance(eNB.location,ue.location)
            # print('        distance: ',end='')
            # print(d)
            eNBRSSI = calcultRSSI(d,power)
            # print('bs rssi:' + str(eNBRSSI))
            if eNBRSSI < currentRssi:
                result = eNB.node_id
                currentRssi = eNBRSSI
    return result


# computing inverse distances from one stations to all the other ones (used for transition probability matrix)
# closer distances get higher values :)
def run(SimultRunTime,predict_rate=1):
    time_simult = 0
    HANDOVER_TIMES =0
    hdtimesset, simltset, pptset, pre_pptset, timeset = [], [], [], [], []
    # location_ue = Location(random.choice(LOCATION_X), random.choice(LOCATION_Y))
    location_ue = Location(250, 250)
    speed = random.choice(SPEED_RANGE)
    final_location = Location(location_ue[0] + math.sqrt(2) * random.randint(-1, 1) * speed * 1000 / 3600,
                              location_ue[1] + math.sqrt(2) * random.randint(-1, 1) * speed * 1000 / 3600)

    ue = UE(location_ue, final_location, speed, BS_id=0)  # creating the user
    print('UE INFO: ', ue)
    while time_simult < SimultRunTime:
        print('UE INFO: ', ue)
        ue.move_in_second()
        time_simult = time_simult + 1
        need_id = NeedHandover(ue)
        if need_id >= 0:
            HANDOVER_TIMES += 1
            ue.handover(need_id)
        else:
            ue.handover(ue.BS_id)
        if time_simult%500 ==0:
            hdtimesset.append(HANDOVER_TIMES)
            simltset.append(time_simult)
            pptset.append(ue.pingpang_times)
            pre_pptset.append(ue.pingpang_times*predict_rate)
            timeset.append(time_simult)

    print('handover times:' + str(HANDOVER_TIMES))
    print('simulation time:' + str(time_simult))
    print('pingpang handover times: ' + str(ue.pingpang_times))

    # return HANDOVER_TIMES,time_simult,ue.pingpang_times,ue.pingpang_times*predict_rate
    return hdtimesset, simltset, pptset, pre_pptset, timeset
if __name__ == '__main__':
    # location_ue = Location(random.choice(LOCATION_X), random.choice(LOCATION_Y))
    location_ue = Location(250,250)
    speed = random.choice(SPEED_RANGE)
    final_location = Location(location_ue[0] + math.sqrt(2)*random.randint(-1,1)*speed*1000/3600,
                              location_ue[1] + math.sqrt(2)*random.randint(-1,1)*speed*1000/3600)

    ue = UE(location_ue, final_location, speed,BS_id=0)  # creating the user
    print('UE INFO: ', ue)
    while time_simult < 1000:
        print('UE INFO: ', ue)
        ue.move_in_second()
        time_simult = time_simult+1
        need_id = NeedHandover(ue)
        if need_id >= 0:
            HANDOVER_TIMES += 1
            ue.handover(need_id)
        else:
            ue.handover(ue.BS_id)


    print('handover times:'+str(HANDOVER_TIMES))
    print('simulation time:'+str(time_simult))
    print('pingpang handover times: '+ str(ue.pingpang_times))
