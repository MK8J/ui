from util.Exceptions import PVInputError
import numpy as np


class TemperatureSettings(object):
    """
    Contains information for temperature change for a series of experiments
    Takes input in any form and converts to Celcius for sending to the
    Instec Temp controller
    """


    units_change = {
    'Celsius': 0,
    'Kelvin': -273
    }
    ramp = 100
    pp = 1

    def __init__(self, start_temp, step_wait, temperature_scale, end_temp=1, step_temp=1):

        super(TemperatureSettings, self).__init__()

        temp_diff = abs(start_temp - end_temp)
        if step_temp == 0:
            raise PVInputError(
                "Step size can not be 0."
            )

        # this are required for the gui of multimeasure
        self.start_temp = start_temp
        self.step_wait = step_wait
        self.end_temp = end_temp
        self.step_temp = step_temp

        # this is a list of temps for the temp controller
        temps = np.arange(start_temp, end_temp, step_temp)
        self.temps = temps + self.units_change[temperature_scale]
        self.temperature_scale = 'Celcius'

        print step_wait
        print np.asarray(temps).shape
        print np.asarray(step_wait).shape, np.asarray(step_wait)
        # this is making sure we get a list of waits
        if np.asarray(temps).shape == np.asarray(step_wait).shape:
            self.waits = np.asarray(step_wait)
        # if its not, make it so
        else:
            self.waits = np.ones(np.asarray(temps).shape[0])*step_wait



    def as_dict(self):
        return {
            "temps": self.temps,
            "waits": self.waits,
            "start_temp" : self.start_temp,
            "step_wait" : self.step_wait,
            "end_temp" : self.end_temp,
            "step_temp" : self.step_temp,
            "temperature_scale": self.temperature_scale
        }

    def __repr__(self):
        return "{0}".format(self.__dict__())
