
# For your use case, the simplest way is to use the VirtualHub
# application to assign a logical name  to each generic sensor.
# For instance radar1, radar2, radar3, radar4. see screenshot
# below:
 

# Then your code become dead simple:
from yocto_api import *
from yocto_genericsensor import *

errmsg = YRefParam()
# Setup the API to use local USB devices
if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
    sys.exit("init error" + errmsg.value)

r1 = YGenericSensor.FindGenericSensor( 'RX420MA1-1D978F.genericSensor1')
r2 = YGenericSensor.FindGenericSensor( 'RX420MA1-1D978F.genericSensor2')
r3 = YGenericSensor.FindGenericSensor( 'RX420MA1-1D9761.genericSensor1')
r4 = YGenericSensor.FindGenericSensor( 'RX420MA1-1D9761.genericSensor2')

if not r1.isOnline() :  sys.exit("radar1 is offline")
if not r2.isOnline() :  sys.exit("radar2 is offline")
if not r3.isOnline() :  sys.exit("radar3 is offline")
if not r4.isOnline() :  sys.exit("radar4 is offline")

# while True:
# #     # print("Radar 1:  %f %s" % (r1.get_currentValue(), r1.get_unit()))
# #     # print("Radar 2:  %f %s" % (r2.get_currentValue(), r2.get_unit()))
#     print("Radar 3:  %f %s" % (r3.get_currentValue(), r3.get_unit()))
#     print("Radar 4:  %f %s" % (r4.get_currentValue(), r4.get_unit()))
#     YAPI.Sleep(1000, errmsg)
