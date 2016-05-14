#!/usr/bin/python
# -*- coding: utf-8 -*-


# import os
# import ctypes

import binascii
import sys
import numpy as np
import time
import struct
# reload(sys)

import visa
import pyvisa


class mk2000():
    '''
    A class that talks to the mk2000
        The name of the instrument in the view
        is defined below
    '''

    my_instrument_name = 'mk1000'

    set_string = '7f 01 07 01 {0} 04 '
    run_string = '7f 01 04 01 01 01 {0}'
    get_string = '7F 10 03 02 f5 2f'

    set_dic = {
        'pp': '06',
        'TT': '08',
        'RT': '12',
        }

    get_string = '7F 10 03 02 f5 2f'

    run_dic = {
        'reset': '00',
        'ramp': '02',
        'pause': '03',
        'stop': '05',
        'pp': '15',
        'hold': '0f',
        }

    def __init__(self, instname=None):

        file32 = 'C:/Windows/System32/visa32.dll'
        self.rm = visa.ResourceManager(file32)
        # print rm.list_resources()
        # print rm.resource_info('mk1000')
        self.my_instrument_name = instname or self.my_instrument_name
        # print self.my_instrument_name
        self._checknum()
        # self.dev = self.rm.open_resource(self.my_instrument_name)

    def _writeandread(self, string):
        output = ''
        counter =0
        while output == '' or counter ==10:
            try:
                self.dev.write_raw(string)
                output = self.dev.read_raw(55)
            except:
                output = ''
                counter+=1
                # print output

        return output

    def _checknum(self):
        self.status = False
        while self.status is False:
            try:
                self.dev = self.rm.open_resource(self.my_instrument_name,
                                                open_timeout=100,
                                                query_delay =5,
                                                resource_pyclass=pyvisa.resources.USBRaw)
                self.dev.write_termination = ''
                self.dev.read_termination = ''
                self.status = True
                # print('Instrument connected')
            except(visa.VisaIOError):
                print 'Instrument not connected (timeout error)\r',

    def _read(self):
        return self.dev.read_raw(55)

    def set(self, temp=None, ramp=None, pp=None):
        '''
<<<<<<< HEAD
        sets values things!
=======
        things!
>>>>>>> e54aba85b2f16f0d109bf24afaae1896925d481f
        '''
        if temp is not None:
            self._set_val('TT', temp)

        if ramp is not None:
            self._set_val('RT', ramp)

        if pp is not None:
            self._set_val('pp', float(pp)/100)

    def run(self, option = 'ramp'):
        '''
        run the tool
            input: (string)
                any value that is in run_dic.
                the defult is for a ramp run
        '''
        if option in self.run_dic.keys():
            self._run(option)
        else:
            print 'Not an option'

    def _run(self, var):
        '''
        Runs the different modes of the driver
        '''

        writestring = self.run_string.format(self.run_dic[var])

        writestring = hex2ascii(writestring)
        self._checknum()
        self._writeandread(writestring)

    def _set_val(self, var, val):
        '''
        A function that sets the provided values to the device
        '''
        # print val
        hex_val = adjust(sp_to_hex(val))
        # print hex_val
        writestring = self.set_string.format(self.set_dic[var]) + hex_val
        # print writestring
        writestring = hex2ascii(writestring)
        # print writestring.encode('hex')
        self._checknum()
        print 'writing'
        self._writeandread(writestring)
        print 'done'

    def get_inf(self):
        '''
        A function to get all the data it can from
        the tool
        '''

        writestring = hex2ascii(self.get_string)

        crap = self._writeandread(writestring)
        while len(crap) == 0:
            crap = self.read_raw(55)

        Hex_code = crap.encode('hex')
        Hex_code = " ".join(Hex_code[i:i+2] for i in range(0, len(Hex_code), 2))
        Hex_code = Hex_code.split('7f')[1]


        try:
            self.settings_dic = {
                'TC': hexstr_2_decimal(''.join(Hex_code.split(' ')[7:7+4])),
                'TT': hexstr_2_decimal(''.join(Hex_code.split(' ')[13:13+4])),
                'pp': hexstr_2_decimal(''.join(Hex_code.split(' ')[17:17+4])),
                'TF': hexstr_2_decimal(''.join(Hex_code.split(' ')[21:21+4])),
                'RT': hexstr_2_decimal(''.join(Hex_code.split(' ')[25:25+4])),
                'MT': hexstr_2_decimal(''.join(Hex_code.split(' ')[29:29+4])),
                }
            return self.settings_dict
        except:
            return 0


def hex2ascii(s, chk1=3):
    '''
    Conversts a list strning of hex code
    into deciaml and then into ascii
    '''
    # print [i for i in s.split(' ')]
    data_list = [int(i, 16) for i in s.split(' ')]

    data_list.insert(chk1, sum(data_list[:chk1]))
    data_list.append(sum(data_list[chk1+1:]))
    # print 'the sum is', chk1+1, data_list[chk1+1:], sum(data_list[chk1+1:])

    data_list = np.array(data_list)

    while np.any(data_list > 255):
        index = data_list > 255
        data_list[index] -= 256

    # if you want to check the hex uncomment the next line
    # print 'print this', [hex(int(i))[2:] for i in data_list]

    # turn in ascii
    ascii_str = ''.join(chr(i) for i in data_list)

    return ascii_str


def sp_to_hex(f):
    ''''
    '''
    f = round(float(f),1 )
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])[:10]

def adjust(string):
    string = string[2:]

    # inserve spaces
    # print string
    string = " ".join(string[i:i+2][::-1] for i in range(0, len(string), 2))
    # print string
    return string[::-1]

def hexstr_2_decimal(Hexstring):
    # print 'The hex string is', Hexstring
    return  struct.unpack('<f',binascii.unhexlify(Hexstring))[0]


if __name__ == '__main__':
    print adjust(sp_to_hex(-20.0))
    print adjust(sp_to_hex(20.0))
    print sp_to_hex(-20.0)
