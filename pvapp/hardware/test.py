
from ConfigParser import SafeConfigParser
import json

config = SafeConfigParser()
config.read('nidaq.ini')


print json.loads(config.get("NI-DAQ", "InputVoltageRange")), type(json.loads(config.get("NI-DAQ", "InputVoltageRange")))
print config._sections["NI-DAQ"]['device_name']