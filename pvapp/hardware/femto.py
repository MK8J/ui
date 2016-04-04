

import ctypes
import collections

femto = ctypes.cdll.LoadLibrary(
    r'C:\Program Files (x86)\FEMTO\LUCI-10\Driver\LUCI_10.dll')

# prints the number of attached devices
# returns -1 on error


class DLPCA_200():
    '''
    This is a class to control the DLPCA 200 from femto.de
    For full controls the hardward needs to be in the state:
        + gain switch set to remote
        + insert high low setting
        + insert ac/dc setting
        + insert bandwidth setting
    '''

    overload_command = 'GetStatusPin5'
    signal_command = 'GetStatusPin6'
    nothing_command = 'GetStatusPin7'

    data_low_dic = {
        'pin_10': 'gain_LSB',
        'pin_11': 'gain',
        'pin_12': 'gain_MSB',
        'pin_13': 'acdc',
        'pin_14': 'voltage_amp',
        'pin_15': 'NA',
        'pin_16': 'NA',
        'pin_17': 'NA',
    }

    data_high_dic = {
        'pin_17': 'NA',
        'pin_18': 'NA',
        'pin_19': 'NA',
        'pin_20': 'NA',
        'pin_21': 'NA',
        'pin_22': 'NA',
        'pin_23': 'NA',
        'pin_24': 'NA',
    }

    # defult settngs
    NA = '0'
    gain_LSB = '0'  # pin 10
    gain = '0'     # pin 11
    gain_MSB = '0'  # pin 12
    acdc = '1'     # pin 13
    voltage_amp = '1'  # pin 14

    # dic for settings
    gain_settings = {
        3: '000',
        4: '001',
        5: '010',
        6: '011',
        7: '100',
        8: '101',
        9: '110',
    }
    acdc_setting = {'ac': '0',
                    'dc': '1'}

    voltage_amp_setting = {True: '0',
                           False: '1'}

    # from the DLPCA_200 data sheet
    # Pin 1: +12 V (stabilized power supply output)
    # Pin 2: -12 V (stabilized power supply output)
    # Pin 3: AGND (analog ground)
    # Pin 4: +5 V (stabilized power supply output)
    # Pin 5: digital output: overload (referred to pin 3)
    # Pin 6: signal output (connected to BNC)
    # Pin 7: NC
    # Pin 8: input offset control voltage
    # Pin 9: DGND (ground for digital control pins 10 - 14)
    # Pin 10: digital control input: gain, LSB
    # Pin 11: digital control input: gain
    # Pin 12: digital control input: gain, MSB
    # Pin 13: digital control input: AC/DC
    # Pin 14: digital control input: high speed / low noise

    def __init__(self, index):
        if index <= self.num_attached_device(False):

            self.index = index

            self.create_inverse_dictionaries()
            self.light_up()

            self.data_low_dic = collections.OrderedDict(
                sorted(self.data_low_dic.items()))
            self.data_high_dic = collections.OrderedDict(
                sorted(self.data_high_dic.items()))
        else:
            print 'that is not  a device'
            self.index = -1

    def create_inverse_dictionaries(self):
        '''
        Creats some inverse dictionaries
        So the codition of the femto can be found
        '''
        self.acdc_setting_i = {v: k for k, v in self.acdc_setting.items()}
        self.voltage_amp_setting_i = {
            v: k for k, v in self.voltage_amp_setting.items()}
        self.gain_settings_i = {v: k for k, v in self.gain_settings.items()}

    def num_attached_device(self, Print=True):

        if Print:
            if femto.EnumerateUsbDevices() < 1:
                print 'no device attached'

            else:
                print 'There is {0} device attached'.format(
                    femto.EnumerateUsbDevices())

        return femto.EnumerateUsbDevices()

    def light_up(self):
        # print 'light on'
        error = femto.LedOn(self.index)
        if int(error) == -1:
            print 'Error'

    def light_down(self):
        # print 'light off'
        error = femto.LedOff(self.index)
        if int(error) == -1:
            print 'Error'

    def is_overloaded(self):
        status = ctypes.c_int()
        error = getattr(femto, self.overload_command)(
            self.index, ctypes.byref(status))
        if int(error) == -1:
            print 'Error'

        return status

    def signal_level(self):
        status = ctypes.c_int()
        error = getattr(femto, self.signal_command)(
            self.index, ctypes.byref(status))
        if int(error) == -1:
            print 'Error'

        return status

    def get_info(self):
        '''
        grabs all the info it can from the attached devces

        don't know if this works
        '''
        print 'the info is'
        # char = ctypes.c_char()
        # print femto.GetProductString(self.index, ctypes.byref(char),
        # ctypes.c_int(10))
        ID = ctypes.c_int()
        femto.ReadAdapterID(self.index, ctypes.byref(ID))
        print 'the device id is:', ID.value

    def set_voltage_amplification(self, voltage_amp):
        '''
        Controls if the voltage amplifaction is turned on or off
        voltage_amp: {'True', 'False'}
                If  *True* the voltage amplification is turned on. 
                If *False* the voltage amplifer is turned off
        '''
        try:
            self.voltage_amp = self.voltage_amp_setting[voltage_amp]
        except:

            print 'invalid paramter, \'', str(voltage_amp), '\''
            print 'parameter ignored'

    def set_acdc_coupling(self, coupling):
        '''
        Controls if the coupling used is AC or DC
        voltage_amp: (dic {'ac', 'dc'})
                If  *ac*, AC coupling is used
                If *dc*, DC coupling is used
        '''
        try:
            self.acdc = self.acdc_setting[coupling]
        except:
            print 'invalid paramter, \'', str(coupling), '\''
            print 'parameter ignored'

    def set_gain(self, gain):
        '''
        sets the gain
            gain: (int)
                sets the gain to the provided value
        '''
        try:

            # print gain
            if self.voltage_amp_setting_i[self.voltage_amp]:
                factor = 2
            else:
                factor = 0

            gain -= factor

            # print 'here here', gain
            gain = self.gain_settings[gain]
            self.gain_LSB = str(gain[2])
            self.gain = str(gain[1])
            self.gain_MSB = str(gain[0])


        except:
            print 'invalid paramter, \'', str(gain), '\''
            print 'parameter ignored'

    def config_femto(self, gain=None, voltage_amp=None, acdc=None):
        '''
        sets the gain on the amplifer

        inputs:
            gain: {None, int}
                If None, does nothing, else passes value to set_gain
            voltage_amp: {None, bol}
                If None, does nothing, else passes value to set_voltage_amplification
            acdc: {None, str}
                If None, does nothing, else passes str to set_acdc_coupling
        '''

        if voltage_amp is not None:
            self.set_voltage_amplification(voltage_amp)

        if gain is not None:
            self.set_gain(gain)

        if acdc is not None:
            self.set_acdc_coupling(acdc)

        self.set_values()

    def data_8bit(self, level):
        '''
        creates data to send to femo.write
            inputs
            level: {'high', 'low'}
                the option determines if it created data_high
                or data_low
            output:
                an 8 bit ctypes intenger
        '''

        data_dic = getattr(self, ''.join(['data_', level, '_dic']))
        data = ''.join(getattr(self, v)
                       for v in data_dic.values()[:: -1])

        # print data, 'should be 00000010'
        # print 'data_8bit:', data
        return ctypes.c_uint8(int(data, 2))


    def set_values(self, data_low=None, data_high=None):
        '''
        Write two 8 bit data words to the 16 output pins of LUCI-10
        interface with number "index".

        num: (optional number)
        '''

        if data_low is None:
            data_low = self.data_8bit('low')
        if data_high is None:
            data_high = self.data_8bit('high')

        # print data_low, data_high
        # data_low = 'a'
        # print'writing: returns',
        # print data_high, data_low
        # print '\t low', data_low, data_low.value, ctypes.sizeof(data_low)
        # print '\t high', data_high, data_high.value
        print femto.WriteData(self.index, data_low, data_high)
        # print 'written'


print 'Testing:'
dev1 = DLPCA_200(1)
dev1.light_up()

dev1.config_femto(gain=9, voltage_amp=True, acdc='dc')

dev1.light_down()
