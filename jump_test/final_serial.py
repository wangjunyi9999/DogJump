import serial
import time
import datetime
import _thread
import pandas as pd
import keyboard
import os
# ZERO METHOD:
#  SW,00,001,0
#  SW,00,001,1
force_list=[]
height_list=[]#max-min
time_list=[]
# def get_data():

#     while True:

def csv_save():
    # time_string=time_now.strftime("%m-%d %H:%M:%S")
    # path=time_string+'motion_data.csv'
    path=f'{time_now}_motion_data_50_1.csv'
    time_force_data=list(zip(time_list,force_list,height_list))
    df=pd.DataFrame(data=time_force_data, 
                    columns=['Time','Force','Height'])
    df.to_csv(path,index=False)

if __name__ == '__main__':
    #get_data()
    # test_com6()
    laser_data_ser = serial.Serial("COM6",9600)
    weight_data_ser= serial.Serial("COM5",9600)

    while True:
        # laser data send and receive
        send_data='M0\r'
        laser_data_ser.flushInput()
        #send_data_ctrl=''
        laser_data_ser.write(send_data.encode())         
        rec_data=laser_data_ser.readline() #laser_data_ser.inWaiting())#.decode('ascii')#('ascii')
        rec_data=str(rec_data,encoding='ascii')
        
        #time data
        time_now=datetime.datetime.now()
        time_now=pd.to_datetime(time_now)
        time_list.append(time_now.strftime("%H:%M:%S.%f"))
        
        # weight data 
        weight_data_count=weight_data_ser.inWaiting()
        weight_rec=weight_data_ser.readline().decode("ascii")
        force_now=round(float(weight_rec[-11:-4])*9.8,3)
        force_list.append(force_now)
        
        #height data
        height_now=round(float(rec_data[-9:])/10, 3)
        height_list.append(height_now)

        keyboard.add_hotkey(hotkey='esc',callback=csv_save)
        print("receive weight_data",force_now,
              "receive laser_data",height_now )
        #print(force_list,height_list)
        time.sleep(0.01)