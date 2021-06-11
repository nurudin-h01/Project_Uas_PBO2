# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Panel_home
###########################################################################

class Panel_home ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 843,588 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer8.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook2.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		self.anggota = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.anggota.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self.anggota, wx.ID_ANY, u"Data Anggota Perpustakaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer10.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.anggota, wx.ID_ANY, u"Tambah Anggota", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button6.SetDefault() 
		self.m_button6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer10.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_grid3 = wx.grid.Grid( self.anggota, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 4, 4 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.AutoSizeRows()
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer10.Add( self.m_grid3, 0, wx.ALL, 5 )
		
		
		self.anggota.SetSizer( bSizer10 )
		self.anggota.Layout()
		bSizer10.Fit( self.anggota )
		self.m_notebook2.AddPage( self.anggota, u"Data Anggota", False )
		self.buku = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText12 = wx.StaticText( self.buku, wx.ID_ANY, u"Daftar Data Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer9.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self.buku, wx.ID_ANY, u"Tambah Buku", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer9.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_grid2 = wx.grid.Grid( self.buku, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 5, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer9.Add( self.m_grid2, 0, wx.ALL, 5 )
		
		
		self.buku.SetSizer( bSizer9 )
		self.buku.Layout()
		bSizer9.Fit( self.buku )
		self.m_notebook2.AddPage( self.buku, u"Data Buku", False )
		self.peminjaman = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.peminjaman, wx.ID_ANY, u"Peminjaman" ), wx.VERTICAL )
		
		self.m_button10 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tambah Peminjaman", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		sbSizer2.Add( self.m_button10, 0, wx.ALL, 5 )
		
		self.m_grid31 = wx.grid.Grid( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid31.CreateGrid( 5, 5 )
		self.m_grid31.EnableEditing( True )
		self.m_grid31.EnableGridLines( True )
		self.m_grid31.EnableDragGridSize( False )
		self.m_grid31.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid31.EnableDragColMove( False )
		self.m_grid31.EnableDragColSize( True )
		self.m_grid31.SetColLabelSize( 30 )
		self.m_grid31.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid31.EnableDragRowSize( True )
		self.m_grid31.SetRowLabelSize( 80 )
		self.m_grid31.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid31.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer2.Add( self.m_grid31, 0, wx.ALL, 5 )
		
		
		self.peminjaman.SetSizer( sbSizer2 )
		self.peminjaman.Layout()
		sbSizer2.Fit( self.peminjaman )
		self.m_notebook2.AddPage( self.peminjaman, u"Data Peminjaman", True )
		self.pengembalian = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook2.AddPage( self.pengembalian, u"Data Pengembalian", False )
		
		bSizer8.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 821,519 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_login = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_login.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self.panel_login, wx.ID_ANY, u"Sistem Administrasi Perpustakaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "BigNoodleTitling" ) )
		
		bSizer5.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText33 = wx.StaticText( self.panel_login, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		self.m_staticText33.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )
		
		gSizer1.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl25 = wx.TextCtrl( self.panel_login, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 155,30 ), 0 )
		gSizer1.Add( self.m_textCtrl25, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText34 = wx.StaticText( self.panel_login, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		self.m_staticText34.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )
		
		gSizer1.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( self.panel_login, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 155,30 ), 0 )
		gSizer1.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button28 = wx.Button( self.panel_login, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button28.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Berlin Sans FB" ) )
		self.m_button28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button28.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer61.Add( self.m_button28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer5.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		
		self.panel_login.SetSizer( bSizer5 )
		self.panel_login.Layout()
		bSizer5.Fit( self.panel_login )
		bSizer6.Add( self.panel_login, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1066,699 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class InPeminjaman
###########################################################################

class InPeminjaman ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,327 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input Peminjaman" ), wx.VERTICAL )
		
		
		self.SetSizer( sbSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class InBuku
###########################################################################

class InBuku ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,327 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input Data Buku" ), wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"No. Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Jenis Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Pengarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button11 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.m_button11OnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.m_button12OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button11OnButtonClick( self, event ):
		event.Skip()
	
	def m_button12OnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class InAnggota
###########################################################################

class InAnggota ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,327 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input Anggota baru" ), wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"No. Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nama Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"No. Handphone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button11 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.m_button11OnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.m_button12OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button11OnButtonClick( self, event ):
		event.Skip()
	
	def m_button12OnButtonClick( self, event ):
		event.Skip()
	

