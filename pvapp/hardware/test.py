from ConfigParser import SafeConfigParser
import json
import numpy as np

# config = SafeConfigParser()
# config.read('hardware.cfg')

# device = 'testdevice'


# deviceinf = config._sections[device]
# a = deviceinf['max_output_samplerate']
# print type(a)
# print deviceinf['name']
# print json.loads(deviceinf['max_output_samplerate'])+1


a = np.linspace(0, 29, 30)
t = np.linspace(0, 10, 10)
print a.shape
print
print 
b = np.reshape(a, newshape=(3, 10), order='F')

print np.vstack((t,b)).T
