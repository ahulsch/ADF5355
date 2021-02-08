# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FreqFrame
###########################################################################

class FreqFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 549,567 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 100 )

		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, wx.ID_ANY )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_radioBtnCh1 = wx.RadioButton( self, wx.ID_ANY, u"Channel 1", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtnCh1.SetValue( True )
		self.m_radioBtnCh1.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer42.Add( self.m_radioBtnCh1, 0, wx.ALL, 5 )

		self.m_radioBtnCh2 = wx.RadioButton( self, wx.ID_ANY, u"Channel 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtnCh2.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer42.Add( self.m_radioBtnCh2, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkMTL = wx.CheckBox( self, wx.ID_ANY, u"Mute Till Lock Detect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkMTL.SetValue(True)
		bSizer42.Add( self.m_checkMTL, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Start Frequenz", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textStartF = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		bSizer6.Add( self.m_textStartF, 0, wx.ALL, 5 )

		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Stop Frequenz", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer6.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_textStopF = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		bSizer6.Add( self.m_textStopF, 0, wx.ALL, 5 )

		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Frequenz Schritt", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer6.Add( self.m_staticText42, 0, wx.ALL, 5 )

		self.m_textStepF = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		bSizer6.Add( self.m_textStepF, 0, wx.ALL, 5 )

		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_checkWobb = wx.CheckBox( self, wx.ID_ANY, u"Wobbeln", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkWobb.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.m_checkWobb, 0, wx.ALL, 5 )

		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer42.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer42.Add( ( 0, 200), 1, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer4.Add( bSizer42, 0, 0, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_gridRegs = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_gridRegs.CreateGrid( 20, 2 )
		self.m_gridRegs.EnableEditing( True )
		self.m_gridRegs.EnableGridLines( True )
		self.m_gridRegs.EnableDragGridSize( False )
		self.m_gridRegs.SetMargins( 0, 0 )

		# Columns
		self.m_gridRegs.SetColSize( 0, 131 )
		self.m_gridRegs.SetColSize( 1, 115 )
		self.m_gridRegs.EnableDragColMove( False )
		self.m_gridRegs.EnableDragColSize( True )
		self.m_gridRegs.SetColLabelSize( 30 )
		self.m_gridRegs.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_gridRegs.EnableDragRowSize( True )
		self.m_gridRegs.SetRowLabelSize( 80 )
		self.m_gridRegs.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_gridRegs.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer5.Add( self.m_gridRegs, 0, wx.ALL, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Actuelle Frequenz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_textActFreq = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		bSizer5.Add( self.m_textActFreq, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_TIMER, self.OnTimer, id=wx.ID_ANY )
		self.m_checkMTL.Bind( wx.EVT_CHECKBOX, self.OnCheckMTL )
		self.m_textStartF.Bind( wx.EVT_LEFT_DOWN, self.OnStartFreq )
		self.m_textStopF.Bind( wx.EVT_LEFT_DOWN, self.OnStopFreq )
		self.m_textStepF.Bind( wx.EVT_LEFT_DOWN, self.OnFreqStep )
		self.m_checkWobb.Bind( wx.EVT_CHECKBOX, self.OnStartSweep )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnTimer( self, event ):
		event.Skip()

	def OnCheckMTL( self, event ):
		event.Skip()

	def OnStartFreq( self, event ):
		event.Skip()

	def OnStopFreq( self, event ):
		event.Skip()

	def OnFreqStep( self, event ):
		event.Skip()

	def OnStartSweep( self, event ):
		event.Skip()


###########################################################################
## Class NumDialog
###########################################################################

class NumDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 474,438 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_textFreq = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,40 ), 0 )
		bSizer41.Add( self.m_textFreq, 0, wx.ALL|wx.EXPAND, 5 )

		gNumPad = wx.GridSizer( 4, 3, 0, 0 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button7.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button8.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button9.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button4.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button5.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button6.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button1.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button2.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button3.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_button0.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_button0, 0, wx.ALL, 5 )

		self.m_buttonk = wx.Button( self, wx.ID_ANY, u",", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_buttonk.SetFont( wx.Font( 50, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_buttonk, 0, wx.ALL, 5 )

		self.m_buttondel = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 80,80 ), 0 )
		self.m_buttondel.SetFont( wx.Font( 40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gNumPad.Add( self.m_buttondel, 0, wx.ALL, 5 )


		bSizer41.Add( gNumPad, 0, 0, 5 )


		gSizer4.Add( bSizer41, 0, 0, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_buttonGHz = wx.Button( self, wx.ID_ANY, u"GHz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonGHz.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.m_buttonGHz, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonMHz = wx.Button( self, wx.ID_ANY, u"MHz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonMHz.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.m_buttonMHz, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_buttonHz = wx.Button( self, wx.ID_ANY, u"Hz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonHz.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.m_buttonHz, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button60 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button60.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.m_button60, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer4.Add( bSizer14, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( gSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.On7 )
		self.m_button8.Bind( wx.EVT_BUTTON, self.On8 )
		self.m_button9.Bind( wx.EVT_BUTTON, self.On9 )
		self.m_button4.Bind( wx.EVT_BUTTON, self.On4 )
		self.m_button5.Bind( wx.EVT_BUTTON, self.On5 )
		self.m_button6.Bind( wx.EVT_BUTTON, self.On6 )
		self.m_button1.Bind( wx.EVT_BUTTON, self.On1 )
		self.m_button2.Bind( wx.EVT_BUTTON, self.On2 )
		self.m_button3.Bind( wx.EVT_BUTTON, self.On3 )
		self.m_button0.Bind( wx.EVT_BUTTON, self.On0 )
		self.m_buttonk.Bind( wx.EVT_BUTTON, self.Onk )
		self.m_buttondel.Bind( wx.EVT_BUTTON, self.OnDel )
		self.m_buttonGHz.Bind( wx.EVT_BUTTON, self.OnGHz )
		self.m_buttonMHz.Bind( wx.EVT_BUTTON, self.OnMHz )
		self.m_buttonHz.Bind( wx.EVT_BUTTON, self.OnHz )
		self.m_button60.Bind( wx.EVT_BUTTON, self.OnCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def On7( self, event ):
		event.Skip()

	def On8( self, event ):
		event.Skip()

	def On9( self, event ):
		event.Skip()

	def On4( self, event ):
		event.Skip()

	def On5( self, event ):
		event.Skip()

	def On6( self, event ):
		event.Skip()

	def On1( self, event ):
		event.Skip()

	def On2( self, event ):
		event.Skip()

	def On3( self, event ):
		event.Skip()

	def On0( self, event ):
		event.Skip()

	def Onk( self, event ):
		event.Skip()

	def OnDel( self, event ):
		event.Skip()

	def OnGHz( self, event ):
		event.Skip()

	def OnMHz( self, event ):
		event.Skip()

	def OnHz( self, event ):
		event.Skip()

	def OnCancel( self, event ):
		event.Skip()


