import wx
import gui

class NumDlg (gui.NumDialog):
    
	val = 0
	komma = 0
	ok = False

	def addval(self,i):
		if (self.komma>0):
			self.val=(self.val)+i/self.komma
			self.komma=self.komma*10
		else:
			self.val=(self.val*10)+i
		self.m_textFreq.Value=str(self.val)

	def On7( self, event ):
		self.addval(7)
	def On8( self, event ):
		self.addval(8)
	def On9( self, event ):
		self.addval(9)
	def On4( self, event ):
		self.addval(4)
	def On5( self, event ):
		self.addval(5)
	def On6( self, event ):
		self.addval(6)
	def On1( self, event ):
		self.addval(1)
	def On2( self, event ):
		self.addval(2)
	def On3( self, event ):
		self.addval(3)
	def On0( self, event ):
		self.addval(0)
	def Onk( self, event ):
		self.komma=10
		self.m_textFreq.Value=str(self.val)+"."

	def OnDel( self, event ):
		self.val=0;
		self.komma=0;
		self.m_textFreq.Value=""

	def OnGHz( self, event ):
		self.m_textFreq.Value+=" GHz"
		self.val*=1000000000.0
		self.ok=True
		self.Close()
	def OnMHz( self, event ):
		self.m_textFreq.Value+=" MHz"
		self.val*=1000000.0
		self.ok=True
		self.Close()

	def OnHz( self, event ):
		self.m_textFreq.Value+=" Hz"
		self.ok=True
		self.Close()

	def OnCancel( self, event ):
		self.Close()



