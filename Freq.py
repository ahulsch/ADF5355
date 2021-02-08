import wx
import gui
import Freq
import FreqGenerator
from adf5355 import adf5355

try:
	import spidev
	spi = spidev.SpiDev()
	spi.open(0, 0)
	d = adf5355(spi)

except ImportError:

	d = adf5355(0)

from math import ceil
def DIV_ROUND_UP(x, y):
    return int(ceil(x / y))


class SetFreqGen (FreqGenerator.FreqGen):
	class p:
		StartFreq=0
		StopFreq=0
		StepFreq=0
		sweep=False
		freq=0;


	def ShowParameters(self):
		self.m_gridRegs.SetCellValue(0,0,"INT")
		self.m_gridRegs.SetCellValue(0,1,str(d.st.integer))

		self.m_gridRegs.SetCellValue(1,0,"FRAC1")
		self.m_gridRegs.SetCellValue(1,1,str(d.st.fract1))

		self.m_gridRegs.SetCellValue(2,0,"FRAC2")
		self.m_gridRegs.SetCellValue(2,1,str(d.st.fract2))

		self.m_gridRegs.SetCellValue(3,0,"MOD2")
		self.m_gridRegs.SetCellValue(3,1,str(d.st.mod2))

		self.m_gridRegs.SetCellValue(4,0,"Register 3")
		self.m_gridRegs.SetCellValue(4,1,str(d.st.regs[3]))

		self.m_gridRegs.SetCellValue(5,0,"R-Counter")
		self.m_gridRegs.SetCellValue(5,1,str(d.ref_div_factor))

		self.m_gridRegs.SetCellValue(6,0,"Phase Detector Polarity")
		self.m_gridRegs.SetCellValue(6,1,str(d.phase_detector_polarity_neg))

		self.m_gridRegs.SetCellValue(7,0,"mux_out_3V3_en")
		self.m_gridRegs.SetCellValue(7,1,str(d.mux_out_3V3_en))

		self.m_gridRegs.SetCellValue(8,0,"ref_diff_en")
		self.m_gridRegs.SetCellValue(8,1,str(d.ref_diff_en))

		self.m_gridRegs.SetCellValue(9,0,"ref_div2_en")
		self.m_gridRegs.SetCellValue(9,1,str(d.ref_div2_en))

		self.m_gridRegs.SetCellValue(10,0,"ref_doubler_en")
		self.m_gridRegs.SetCellValue(10,1,str(d.ref_doubler_en))

		self.m_gridRegs.SetCellValue(11,0,"outa_power")
		self.m_gridRegs.SetCellValue(11,1,str(d.outa_power))

		self.m_gridRegs.SetCellValue(12,0,"outa_enable")
		self.m_gridRegs.SetCellValue(12,1,str(d.outa_en))

		self.m_gridRegs.SetCellValue(13,0,"outb_enable")
		self.m_gridRegs.SetCellValue(13,1,str(d.outb_en))

		self.m_gridRegs.SetCellValue(14,0,"mute_till_lock_detect_en")
		self.m_gridRegs.SetCellValue(14,1,str(d.mute_till_lock_detect_en))
		self.m_checkMTL.Value=d.mute_till_lock_detect_en

		self.m_gridRegs.SetCellValue(15,0,"cp_bleed")
		self.m_gridRegs.SetCellValue(15,1,str(d.cp_bleed))

		self.m_gridRegs.SetCellValue(16,0,"rf_div_sel")
		self.m_gridRegs.SetCellValue(16,1,str(d.st.rf_div_sel))

		self.m_gridRegs.SetCellValue(17,0,"cp_neg_bleed_en")
		self.m_gridRegs.SetCellValue(17,1,str(d.cp_neg_bleed_en))

		self.m_gridRegs.SetCellValue(18,0,"cp_gated_bleed_en")
		self.m_gridRegs.SetCellValue(18,1,str(d.cp_gated_bleed_en))


		self.m_gridRegs.SetCellValue(19,0,"VCO_BAND_DIV")
		self.m_gridRegs.SetCellValue(19,1,str(DIV_ROUND_UP(d.st.fpfd, 2400000)))



	def SetFrequency( self, f , strval):
		if (f > d.st.max_out_freq):
			d.set_freq(f, 1)
			self.m_radioBtnCh2.Value=True
		else:
			d.set_freq(f, 0)
			self.m_radioBtnCh1.Value=True
		self.ShowParameters()
		self.m_textStartF.Value=strval
		self.p.StartFreq=f

	def StopFrequency( self, f , strval):
		self.m_textStopF.Value=strval
		self.p.StopFreq=f

	def StepFrequency( self, f , strval):
		self.m_textStepF.Value=strval
		self.p.StepFreq=f


	def SetMTL( self, mtl):
		d.set_mtl(mtl)
		self.ShowParameters()

	def ShowFrequency(self):
		if (self.p.sweep):
			if (self.p.freq==0)|(self.p.freq>=self.p.StopFreq):
				self.p.freq=self.p.StartFreq;
			self.p.freq+=self.p.StepFreq
			if (self.m_radioBtnCh1.Value):
				d.set_freq(self.p.freq, 0)
			else:
				d.set_freq(self.p.freq, 1)
		self.m_textActFreq.Value=str(d.act_frequency)

	
	def StartSweep(self, wobOn):
		self.p.sweep=wobOn


app = wx.App(False)

frame=SetFreqGen(wx.Frame(None, wx.ID_ANY, "Hello World"))
frame.Show(True)
app.MainLoop()
