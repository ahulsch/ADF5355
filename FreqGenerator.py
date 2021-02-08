import wx
import gui
import Freq
from NumDlg import NumDlg

class FreqGen (gui.FreqFrame):

	def OnStartFreq( self, event ):
		dlg=NumDlg(self)
		dlg.ShowModal()
		if (dlg.ok):
			self.SetFrequency(int(dlg.val),dlg.m_textFreq.Value)

	def OnStopFreq( self, event ):
		dlg=NumDlg(self)
		dlg.ShowModal()
		if (dlg.ok):
			self.StopFrequency(int(dlg.val),dlg.m_textFreq.Value)


	def OnFreqStep( self, event ):
		dlg=NumDlg(self)
		dlg.ShowModal()
		if (dlg.ok):
			self.StepFrequency(int(dlg.val),dlg.m_textFreq.Value)


	def OnCheckMTL( self, event ):
		self.SetMTL(self.m_checkMTL.Value)

	def OnTimer(self,event):
		self.ShowFrequency()

	def OnStartSweep( self, event):
		self.StartSweep(self.m_checkWobb.Value)

