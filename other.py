import os
import can

os.system( 'sudo /sbin/ip link set can0 down' )
os.system( 'sudo /sbin/ip link set can0 up type can bitrate 1000000' )
bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native
while 1:
    message = bus.recv(10.0)
    print (message)
    
    if message is None:
        print('Timeout occurred, no message received.')

    os.system('sudo ifconfig can0 down')  #Disable can0