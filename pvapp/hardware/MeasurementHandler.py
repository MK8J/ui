import numpy as np
import logging

from collections import deque

from ConfigParser import SafeConfigParser

from hardware.daq import WaveformThread
from hardware.femto import DLPCA_200
from models.LightPulse import LightPulse
from util.utils import bin_data



class MeasurementHandler():

    def __init__(self):

        self.config = SafeConfigParser()
        self.config.read('hardware.cfg')

        # print config.sections()
        # self.config = config()

        self._queue = deque()
        self.preamps = FemtoMeasurementHandler(self.config._sections['reference_preamp'],
                                            self.config._sections['sample_preamp'])
        self.daq = DAQMeasurementHandler()


    def is_queue_empty(self):
        return True if len(self._queue) == 0 else False

    def clear_queue(self):
        '''
        clears the queue
        '''
        self._queue = deque()

    def add_to_queue(self, metadata):
        '''
        Add the metadata to the que
        '''
        print 'the metal data is', metadata
        self._queue.append(metadata)

    def pc_calibration_measurement(self, calibration_settings):
        '''
            This should append data that can provide
            the calibration numbers?.
            This currently does not work.
        '''

        self.add_to_queue(
            calibration_settings
        )

        return self.single_measurement()

    def single_measurement(self):
        '''
        This runs a single measurements:
            1. Sets the femto gain
            2. Generatres a waveform
            3. Sends command to DAQ
            4. Does next item
        '''
        # get measurement from list
        measurement_settings = self._queue.popleft()
        print 'The measurement settings are', type(measurement_settings)
        print measurement_settings.ref_gain
        print measurement_settings.pl_gain

        # set preamp gains
        self.preamps.configure(measurement_settings)

        # gets the voltage pulse to control the waveform
        waveform_array = LightPulse(measurement_settings).create_waveform()
        print waveform_array

        # initalises the DAQ ready for a measurement
        thread = self.daq._int_thread(waveform_array, measurement_settings)

        # lets get the averaging
        averaging = measurement_settings.averaging

        # set the variables before they are created?
        thread_time = None
        measurement_data = []

        # perform a measurement
        measurement_data, thread_time = self.daq.run_thread(thread)

        # make sure the length makes sense
        data_len = measurement_data.shape[0] / self.daq.NUM_CHANNELS
        # print type(data_len), data_len
        # print
        assert (
            data_len.is_integer(), "No of points per channel={0}".format(
                data_len)
        )
        data_len = int(data_len)


        # if more averages were requested
        if averaging > 1:
            for i in range(averaging - 1):
                thread_data, thread_time = self.daq.run_thread(thread)
                # stack the data
                measurement_data = np.vstack((thread_data,
                                              measurement_data))
                # average the data, weighting it towards
                # running total
                measurement_data = np.average(measurement_data,
                                              axis=0,
                                              weights=(1, i + 1))

        # convert into columns, putting the right data
        # in the right place
        measurement_data = measurement_data[:data_len*int(self.daq.NUM_CHANNELS)]
        measurement_data = measurement_data.reshape(
            (data_len, int(self.daq.NUM_CHANNELS)),
            order = 'F')

        assert measurement_data.shape[0] == thread_time.shape[0], 'data Length differ {0} {1}'.format( measurement_data.shape, thread_time.shape[0])

        measurement_data = np.vstack((thread_time, measurement_data.T)).T
        measurement_data = bin_data(measurement_data,measurement_settings.binning)

        return measurement_data


class FemtoMeasurementHandler():
    """
    Controller to handle IO from NI datacard
    """

    def __init__(self, reference_inf, sample_inf):
        # need to pass an index
        # need a way to determine which is the ref, and sample
        # can put this in the hardware config
        assert reference_inf['model'] =='DLPCA_200'
        assert sample_inf['model'] =='DLPCA_200'

        self.preamps = {
        'ref': DLPCA_200(int(reference_inf['index'])),
            'pl': DLPCA_200(int(sample_inf['index'])),
        }

        # sets the safe values for the preamps

    def set_safe_values(self):
        '''
        Sets the preamps to a state where they are unlikely to
        be damaged. This should be used when a measurement is not in
        progress.
        '''
        self.preamps['ref'].config_femto(
            gain=1e3,
            voltage_amp=False,
            acdc='dc'
        )
        self.preamps['pl'].config_femto(
            gain=1e3,
            voltage_amp=False,
            acdc='dc'
        )

    def configure(self, measurement_settings):
        """
        Sets the gain of the femtos
        """
        print 'The femto gain is', measurement_settings.ref_gain
        self.preamps['ref'].config_femto(gain=measurement_settings.ref_gain)
        self.preamps['pl'].config_femto(gain=measurement_settings.pl_gain)


class DAQMeasurementHandler(object):
    """
    Controller to handle IO from NI datacard
    """

    def __init__(self):

        self._queue = deque()
        self.NUM_CHANNELS = 3.
        self._logger = logging.getLogger()

    def _int_thread(self, waveform_array, experiment_settings):
        '''
        initalises the thread?
        '''
        daq_io_thread = WaveformThread(
            waveform=waveform_array,
            Channel=experiment_settings.channel_name,
            Time=np.float64(experiment_settings.get_total_time()),
            input_voltage_range=experiment_settings.input_voltage_range,
            output_voltage_range=experiment_settings.output_voltage_range,
            input_sample_rate=experiment_settings.sample_rate,
            output_sample_rate=experiment_settings.output_sample_rate
        )

        return daq_io_thread

    def run_thread(self, daq_io_thread):
        """
        Sends a single version of waveform to the specified channel
        Returns:
        """

        daq_io_thread.setup()
        daq_io_thread.run()
        daq_io_thread.stop()

        return daq_io_thread.Read_Data, daq_io_thread.time

    def as_list(self):
        experiment_list = []
        for experiment in self._queue:
            experiment_list.append(experiment[1].as_dict())
        return experiment_list
