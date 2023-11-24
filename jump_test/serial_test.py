import serial
import time
import datetime
import _thread # 导入线程包
import pandas as pd
import keyboard
import sys

data_ser = serial.Serial("COM5",9600)      
data_ser.flushInput()

time_list=[]
force_list=[]

def on_key_press(event):
    if event.name=='esc':
        csv_save()
        

def get_data():

    while True:
        # normal
        data_count = data_ser.inWaiting()
        if data_count !=0 :
            recv = data_ser.readline().decode("ascii")
            #print(datetime.datetime.now(),"data_recv->", recv)
            time_now=datetime.datetime.now()
            #time_now=pd.to_datetime(datetime.datetime.now())
            force_now=round(float(recv[-11:-4])*9.8,3)
            print('Time:',time_now,
                'Force:',force_now,'N')
            time_now=pd.to_datetime(time_now)
            time_list.append(time_now.strftime("%H:%M:%S.%f"))
            force_list.append(force_now)
        keyboard.add_hotkey(hotkey='esc',callback=csv_save)
        time.sleep(0.01)
        #keyboard.on_press(on_key_press)
    #keyboard.wait()

def test_com5():
    over_time=60
    start_time=time.time()
    while True:
        end_time=time.time()
        if end_time-start_time<over_time:
            data=data_ser.read(data_ser.in_Waiting())
            data=str(data)
            if data!='':
                print (data)

def csv_save():
    path='weight_data_1109_second.csv'
    time_force_data=list(zip(time_list,force_list))
    df=pd.DataFrame(data=time_force_data, 
                    columns=['Time','Force'])
    df.to_csv(path,index=False)

if __name__ == '__main__':
    get_data()
    sys.exit()
    #csv_save()
    # _thread.start_new_thread(get_data,()) # 开启线程，执行get_data方法
    # while 1:
    #     time.sleep(0.01)






        # time.sleep(2)
        # data_ser.write(b'1') # 发送二进制1
        # time.sleep(2)
        # data_ser.write(b'0') # 发送二进制0
