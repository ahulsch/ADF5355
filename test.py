import FreqGenerator
import wx


class SetFreqGen (FreqGenerator.FreqGen):
	def SetFrequency( self, f, ch ):
		print(f,ch)


app = wx.App(False)

frame=SetFreqGen(wx.Frame(None, wx.ID_ANY, "Hello World"))
frame.Show(True)
app.MainLoop()

