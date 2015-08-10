# -*- coding: utf-8 -*- ############################################################################# Python code generated with wxFormBuilder (version Sep 12 2010)## http://www.wxformbuilder.org/#### PLEASE DO "NOT" EDIT THIS FILE!###########################################################################import wx############################################################################# Class FrameSkeleton###########################################################################class FrameSkeleton ( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PVapp ", pos = wx.DefaultPosition, size = wx.Size( 1255,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )				bSizer1 = wx.BoxSizer( wx.HORIZONTAL )				self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )		self.m_scrolledWindow1.SetScrollRate( 5, 5 )		bSizer3 = wx.BoxSizer( wx.VERTICAL )				sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Waveform Parameters" ), wx.VERTICAL )				fgSizer2 = wx.FlexGridSizer( 8, 4, 5, 5 )		fgSizer2.SetFlexibleDirection( wx.BOTH )		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )				self.m_staticText1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Intensity (V)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText1.Wrap( -1 )		fgSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Intensity = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"0.5", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer2.Add( self.m_Intensity, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText10 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Waveform", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText10.Wrap( -1 )		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )				m_WaveformChoices = [ u"Cos", u"Sin", u"Square", u"Triangle", u"MattiasCustom", u"FrequencyScan" ]		self.m_Waveform = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_WaveformChoices, 0 )		self.m_Waveform.SetSelection( 0 )		fgSizer2.Add( self.m_Waveform, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )				self.m_staticText9 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"LED threshold\nCurrent (mA)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText9.Wrap( -1 )		fgSizer2.Add( self.m_staticText9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )				self.m_Threshold = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"150", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer2.Add( self.m_Threshold, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText11 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Voltage Current\nConverter", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText11.Wrap( -1 )		fgSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )				m_OutputChoices = [ u"High (2A/V)", u"Low (50mA/V)" ]		self.m_Output = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_OutputChoices, 0 )		self.m_Output.SetSelection( 0 )		fgSizer2.Add( self.m_Output, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )				self.m_staticText5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Illumination\nperiod (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText5.Wrap( -1 )		fgSizer2.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Period = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer2.Add( self.m_Period, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText6 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Delay before\nillumination (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText6.Wrap( -1 )		fgSizer2.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.ALIGN_RIGHT, 5 )				self.m_Offset_Before = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer2.Add( self.m_Offset_Before, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText12 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Frequency (Hz)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText12.Wrap( -1 )		fgSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_Frequency = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )		self.m_Frequency.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )				fgSizer2.Add( self.m_Frequency, 0, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText7 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Delay after\nillumination (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText7.Wrap( -1 )		fgSizer2.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.ALIGN_RIGHT, 5 )				self.m_Offset_After = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer2.Add( self.m_Offset_After, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				sbSizer2.Add( fgSizer2, 0, wx.EXPAND, 5 )				bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )				sbSizer_Processing = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Data Collection Parameters" ), wx.VERTICAL )				fgSizer1 = wx.FlexGridSizer( 3, 4, 0, 0 )		fgSizer1.SetFlexibleDirection( wx.BOTH )		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )				self.m_Name = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Data Points to collect", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_Name.Wrap( -1 )		fgSizer1.Add( self.m_Name, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_DataPoint = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )		self.m_DataPoint.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )				fgSizer1.Add( self.m_DataPoint, 0, wx.ALL, 5 )				self.m_staticText8 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Samples to Average", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText8.Wrap( -1 )		fgSizer1.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Averaging = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer1.Add( self.m_Averaging, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText3 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Data Bin Width", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText3.Wrap( -1 )		fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )				self.m_Binning = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer1.Add( self.m_Binning, 0, wx.ALIGN_CENTER_VERTICAL, 5 )				self.m_staticText121 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Sampling Frequency", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText121.Wrap( -1 )		fgSizer1.Add( self.m_staticText121, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )				self.m_samplingFreq = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer1.Add( self.m_samplingFreq, 0, wx.ALL, 5 )				self.m_StaticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Voltage Range", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_StaticText.Wrap( -1 )		fgSizer1.Add( self.m_StaticText, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )				m_voltageRangeChoices = []		self.m_voltageRange = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_voltageRangeChoices, 0 )		self.m_voltageRange.SetSelection( 0 )		fgSizer1.Add( self.m_voltageRange, 0, wx.ALL, 5 )				sbSizer_Processing.Add( fgSizer1, 0, wx.EXPAND, 5 )				bSizer5 = wx.BoxSizer( wx.HORIZONTAL )				self.GoButton = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Perform Measurement", wx.DefaultPosition, wx.DefaultSize, 0 )		self.GoButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )		self.GoButton.SetBackgroundColour( wx.Colour( 98, 211, 22 ) )				bSizer5.Add( self.GoButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )				sbSizer_Processing.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )				fgSizer3 = wx.FlexGridSizer( 2, 3, 0, 0 )		fgSizer3.SetFlexibleDirection( wx.BOTH )		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )				self.m_PCCalibration = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"PC calibration", wx.DefaultPosition, wx.DefaultSize, 0 )		fgSizer3.Add( self.m_PCCalibration, 0, wx.ALL, 5 )				self.m_staticText14 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"PC Mean", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText14.Wrap( -1 )		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )				self.m_pcCalibrationMean = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )		self.m_pcCalibrationMean.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )				fgSizer3.Add( self.m_pcCalibrationMean, 0, wx.ALL, 5 )						fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )				self.m_staticText15 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"PC Std", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText15.Wrap( -1 )		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )				self.m_pcCalibrationStd = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )		self.m_pcCalibrationStd.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )				fgSizer3.Add( self.m_pcCalibrationStd, 0, wx.ALL, 5 )				sbSizer_Processing.Add( fgSizer3, 1, wx.EXPAND, 5 )				bSizer3.Add( sbSizer_Processing, 0, wx.EXPAND, 5 )				bSizer4 = wx.BoxSizer( wx.HORIZONTAL )				self.m_Save = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Save Settings", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer4.Add( self.m_Save, 0, wx.ALL, 5 )				self.m_button6 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Save Data", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer4.Add( self.m_button6, 0, wx.ALL, 5 )				self.m_Load = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Load Settings", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer4.Add( self.m_Load, 0, wx.ALL, 5 )				self.m_LoadData = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Load Data", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer4.Add( self.m_LoadData, 0, wx.ALL, 5 )				bSizer3.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )				self.m_scrolledWindow1.SetSizer( bSizer3 )		self.m_scrolledWindow1.Layout()		bSizer3.Fit( self.m_scrolledWindow1 )		self.m_notebook1.AddPage( self.m_scrolledWindow1, u"Raw Measurement", True )				bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )				bSizer2 = wx.BoxSizer( wx.VERTICAL )				self.Figure1_Panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer2.Add( self.Figure1_Panel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )				bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )				self.SetSizer( bSizer1 )		self.Layout()				self.Centre( wx.BOTH )				# Connect Events		self.m_scrolledWindow1.Bind( wx.EVT_CHAR, self.Run_Me )		self.m_Intensity.Bind( wx.EVT_TEXT, self.CurrentLimits )		self.m_Output.Bind( wx.EVT_CHOICE, self.CurrentLimits )		self.m_Period.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_Offset_Before.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_Offset_After.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_Binning.Bind( wx.EVT_CHAR, self.onChar_int )		self.m_Binning.Bind( wx.EVT_KILL_FOCUS, self.Num_Data_Points_Update )		self.m_samplingFreq.Bind( wx.EVT_KILL_FOCUS, self.onSamplingFreq )		self.m_voltageRange.Bind( wx.EVT_CHOICE, self.onVoltageRange )		self.GoButton.Bind( wx.EVT_BUTTON, self.Perform_Measurement )		self.m_Save.Bind( wx.EVT_BUTTON, self.onSave )		self.m_button6.Bind( wx.EVT_BUTTON, self.onSaveData )		self.m_Load.Bind( wx.EVT_BUTTON, self.onLoad )		self.m_LoadData.Bind( wx.EVT_BUTTON, self.onLoadData )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def Run_Me( self, event ):		event.Skip()		def CurrentLimits( self, event ):		event.Skip()			def Num_Data_Points_Update( self, event ):		event.Skip()				def onChar_int( self, event ):		event.Skip()			def onSamplingFreq( self, event ):		event.Skip()		def onVoltageRange( self, event ):		event.Skip()		def Perform_Measurement( self, event ):		event.Skip()		def onSave( self, event ):		event.Skip()		def onSaveData( self, event ):		event.Skip()		def onLoad( self, event ):		event.Skip()		def onLoadData( self, event ):		event.Skip()	