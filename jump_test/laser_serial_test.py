import serial
import time
import datetime
import _thread # 导入线程包
import pandas as pd
import keyboard
import sys
# ZERO METHOD:
#  SW,00,001,0
#  SW,00,001,1

# def on_key_press(event):
#     if event.name=='esc':
#         csv_save()
       

# def get_data():

#     while True:
#         # normal
#         data_count = data_ser.inWaiting()
#         if data_count !=0 :
#             recv = data_ser.readline().decode("ascii")
#             #print(datetime.datetime.now(),"data_recv->", recv)
#             time_now=datetime.datetime.now()
#             #time_now=pd.to_datetime(datetime.datetime.now())
#             force_now=round(float(recv[-11:-4])*9.8,3)
#             print('Time:',time_now,
#                 'Force:',force_now,'N')
#             time_now=pd.to_datetime(time_now)
#             time_list.append(time_now.strftime("%H:%M:%S.%f"))
#             force_list.append(force_now)
#         keyboard.add_hotkey(hotkey='esc',callback=csv_save)
#         time.sleep(0.01)

def test_com6():
    over_time=60
    start_time=time.time()
    while True:
        end_time=time.time()
        if end_time-start_time<over_time:
            data=data_ser.read(data_ser.in_Waiting())
            data=str(data)
            if data!='':
                print (data)

# def csv_save():
#     path='weight_data_1108_second.csv'
#     time_force_data=list(zip(time_list,force_list))
#     df=pd.DataFrame(data=time_force_data, 
#                     columns=['Time','Force'])
#     df.to_csv(path,index=False)

if __name__ == '__main__':
    #get_data()
    # test_com6()
    data_ser = serial.Serial("COM6",9600)  
    #print(data_ser.is_open)    
    while True:
        send_data='M0\r'
        #send_data_ctrl=''
        data_ser.write(send_data.encode())  
        #data_ser.write(send_data_ctrl.encode())
        data_ser.flushInput()
        rec_data=data_ser.readline() #data_ser.inWaiting())#.decode('ascii')#('ascii')
        rec_data=str(rec_data,encoding='ascii')
        time_now=datetime.datetime.now()
        print("receive laser_data",float(rec_data[-9:]))
        time.sleep(0.01)
        # if rec_data!='':
        #     break
    sys.exit()
    # time_list=[]
    # height_list=[]

    #sys.exit()
    #csv_save()
    # _thread.start_new_thread(get_data,()) # 开启线程，执行get_data方法
    # while 1:
    #     time.sleep(0.01)






        # time.sleep(2)
        # data_ser.write(b'1') # 发送二进制1
        # time.sleep(2)
        # data_ser.write(b'0') # 发送二进制0
