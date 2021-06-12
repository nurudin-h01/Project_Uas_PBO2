# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 821,519 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Sistem Administrasi Perpustakaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 10, 70, 90, 90, False, "Amaranth" ) )
		
		bSizer5.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		self.m_staticText33.SetFont( wx.Font( 11, 70, 90, 90, False, "Amaranth" ) )
		
		gSizer1.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_textCtrl25.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		gSizer1.Add( self.m_textCtrl25, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		self.m_staticText34.SetFont( wx.Font( 11, 70, 90, 90, False, "Amaranth" ) )
		
		gSizer1.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_PASSWORD )
		self.m_textCtrl26.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		gSizer1.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button28 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button28.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button28.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer61.Add( self.m_button28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer5.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button28.Bind( wx.EVT_BUTTON, self.button_login )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def button_login( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 843,588 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 843,588 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 12, 70, 90, 90, False, "Amaranth" ) )
		
		bSizer8.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer8.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook2.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_notebook2.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		self.m_scrolledWindow5 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow5, wx.ID_ANY, u"Data Anggota" ), wx.VERTICAL )
		
		self.m_grid3121 = wx.grid.Grid( sbSizer221.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), 0 )
		
		# Grid
		self.m_grid3121.CreateGrid( 5, 4 )
		self.m_grid3121.EnableEditing( True )
		self.m_grid3121.EnableGridLines( True )
		self.m_grid3121.EnableDragGridSize( False )
		self.m_grid3121.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3121.SetColSize( 0, 91 )
		self.m_grid3121.SetColSize( 1, 158 )
		self.m_grid3121.SetColSize( 2, 105 )
		self.m_grid3121.SetColSize( 3, 114 )
		self.m_grid3121.EnableDragColMove( True )
		self.m_grid3121.EnableDragColSize( True )
		self.m_grid3121.SetColLabelSize( 30 )
		self.m_grid3121.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3121.AutoSizeRows()
		self.m_grid3121.EnableDragRowSize( True )
		self.m_grid3121.SetRowLabelSize( 120 )
		self.m_grid3121.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3121.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.m_grid3121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sbSizer221.Add( self.m_grid3121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button1021 = wx.Button( sbSizer221.GetStaticBox(), wx.ID_ANY, u"Tambah Anggota", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button1021.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1021.SetBackgroundColour( wx.Colour( 117, 234, 0 ) )
		
		gbSizer1.Add( self.m_button1021, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button10211 = wx.Button( sbSizer221.GetStaticBox(), wx.ID_ANY, u"Edit Anggota", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button10211.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button10211.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		
		gbSizer1.Add( self.m_button10211, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button10212 = wx.Button( sbSizer221.GetStaticBox(), wx.ID_ANY, u"Hapus Anggota", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button10212.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button10212.SetBackgroundColour( wx.Colour( 232, 39, 23 ) )
		
		gbSizer1.Add( self.m_button10212, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer221.Add( gbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE, 5 )
		
		
		self.m_scrolledWindow5.SetSizer( sbSizer221 )
		self.m_scrolledWindow5.Layout()
		sbSizer221.Fit( self.m_scrolledWindow5 )
		self.m_notebook2.AddPage( self.m_scrolledWindow5, u"Data Anggota", False )
		self.m_scrolledWindow6 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		sbSizer211 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow6, wx.ID_ANY, u"Data Buku" ), wx.VERTICAL )
		
		self.m_grid3111 = wx.grid.Grid( sbSizer211.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		
		# Grid
		self.m_grid3111.CreateGrid( 5, 4 )
		self.m_grid3111.EnableEditing( True )
		self.m_grid3111.EnableGridLines( True )
		self.m_grid3111.EnableDragGridSize( False )
		self.m_grid3111.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3111.SetColSize( 0, 80 )
		self.m_grid3111.SetColSize( 1, 154 )
		self.m_grid3111.SetColSize( 2, 80 )
		self.m_grid3111.SetColSize( 3, 98 )
		self.m_grid3111.EnableDragColMove( True )
		self.m_grid3111.EnableDragColSize( True )
		self.m_grid3111.SetColLabelSize( 30 )
		self.m_grid3111.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3111.AutoSizeRows()
		self.m_grid3111.EnableDragRowSize( True )
		self.m_grid3111.SetRowLabelSize( 80 )
		self.m_grid3111.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3111.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		sbSizer211.Add( self.m_grid3111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button1011 = wx.Button( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Tambah Buku", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button1011.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1011.SetBackgroundColour( wx.Colour( 117, 234, 0 ) )
		
		gbSizer2.Add( self.m_button1011, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button10111 = wx.Button( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Edit Buku", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button10111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button10111.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		
		gbSizer2.Add( self.m_button10111, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button10112 = wx.Button( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Hapus Buku", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button10112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button10112.SetBackgroundColour( wx.Colour( 232, 39, 23 ) )
		
		gbSizer2.Add( self.m_button10112, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		sbSizer211.Add( gbSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE, 5 )
		
		
		self.m_scrolledWindow6.SetSizer( sbSizer211 )
		self.m_scrolledWindow6.Layout()
		sbSizer211.Fit( self.m_scrolledWindow6 )
		self.m_notebook2.AddPage( self.m_scrolledWindow6, u"Data Buku", False )
		self.m_scrolledWindow7 = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow7.SetScrollRate( 5, 5 )
		sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow7, wx.ID_ANY, u"Peminjaman" ), wx.VERTICAL )
		
		self.m_grid312 = wx.grid.Grid( sbSizer22.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), 0 )
		
		# Grid
		self.m_grid312.CreateGrid( 5, 6 )
		self.m_grid312.EnableEditing( True )
		self.m_grid312.EnableGridLines( True )
		self.m_grid312.EnableDragGridSize( False )
		self.m_grid312.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid312.SetColSize( 0, 90 )
		self.m_grid312.SetColSize( 1, 102 )
		self.m_grid312.SetColSize( 2, 80 )
		self.m_grid312.SetColSize( 3, 112 )
		self.m_grid312.SetColSize( 4, 114 )
		self.m_grid312.SetColSize( 5, 108 )
		self.m_grid312.EnableDragColMove( True )
		self.m_grid312.EnableDragColSize( True )
		self.m_grid312.SetColLabelSize( 30 )
		self.m_grid312.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid312.AutoSizeRows()
		self.m_grid312.EnableDragRowSize( True )
		self.m_grid312.SetRowLabelSize( 80 )
		self.m_grid312.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid312.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.m_grid312.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		sbSizer22.Add( self.m_grid312, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button102 = wx.Button( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Tambah Peminjaman", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button102.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button102.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button102.SetBackgroundColour( wx.Colour( 117, 234, 0 ) )
		
		gbSizer3.Add( self.m_button102, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button1022 = wx.Button( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Edit Peminjaman", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button1022.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button1022.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1022.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		
		gbSizer3.Add( self.m_button1022, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button1023 = wx.Button( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Delete Peminjaman", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button1023.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button1023.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button1023.SetBackgroundColour( wx.Colour( 232, 39, 23 ) )
		
		gbSizer3.Add( self.m_button1023, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		sbSizer22.Add( gbSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE, 5 )
		
		
		self.m_scrolledWindow7.SetSizer( sbSizer22 )
		self.m_scrolledWindow7.Layout()
		sbSizer22.Fit( self.m_scrolledWindow7 )
		self.m_notebook2.AddPage( self.m_scrolledWindow7, u"Data Peminjaman", True )
		
		bSizer8.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer8.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button12.Bind( wx.EVT_BUTTON, self.Keluar )
		self.m_button1021.Bind( wx.EVT_BUTTON, self.anggota )
		self.m_button10211.Bind( wx.EVT_BUTTON, self.edit )
		self.m_button10212.Bind( wx.EVT_BUTTON, self.hapus )
		self.m_button1011.Bind( wx.EVT_BUTTON, self.buku )
		self.m_button10111.Bind( wx.EVT_BUTTON, self.edit_2 )
		self.m_button10112.Bind( wx.EVT_BUTTON, self.hapus_2 )
		self.m_button102.Bind( wx.EVT_BUTTON, self.pinjam )
		self.m_button1022.Bind( wx.EVT_BUTTON, self.edit_3 )
		self.m_button1023.Bind( wx.EVT_BUTTON, self.hapus_3 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Keluar( self, event ):
		event.Skip()
	
	def anggota( self, event ):
		event.Skip()
	
	def edit( self, event ):
		event.Skip()
	
	def hapus( self, event ):
		event.Skip()
	
	def buku( self, event ):
		event.Skip()
	
	def edit_2( self, event ):
		event.Skip()
	
	def hapus_2( self, event ):
		event.Skip()
	
	def pinjam( self, event ):
		event.Skip()
	
	def edit_3( self, event ):
		event.Skip()
	
	def hapus_3( self, event ):
		event.Skip()
	

###########################################################################
## Class InPeminjaman
###########################################################################

class InPeminjaman ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,400 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Input Peminjaman Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		self.m_staticText50.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_staticText50.SetMinSize( wx.Size( -1,35 ) )
		
		bSizer8.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Id Peminjaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		self.m_staticText45.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.noanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.noanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.noanggota, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"No Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		self.m_staticText46.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.namaanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaanggota.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		fgSizer14.Add( self.namaanggota, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"No Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		self.m_staticText47.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.nobuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nobuku.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.nobuku, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		self.m_staticText48.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.judul = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.judul.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.judul, 0, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Pinjam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		self.m_staticText49.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.pinjam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pinjam.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.pinjam, 0, wx.ALL, 5 )
		
		self.m_staticText491 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText491.Wrap( -1 )
		self.m_staticText491.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText491, 0, wx.ALL, 5 )
		
		self.kembali = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kembali.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.kembali, 0, wx.ALL, 5 )
		
		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button33.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer14.Add( self.m_button33, 0, wx.ALL, 5 )
		
		self.m_button34 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button34.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button34.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button34.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer14.Add( self.m_button34, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( fgSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button33.Bind( wx.EVT_BUTTON, self.save_pinjam )
		self.m_button34.Bind( wx.EVT_BUTTON, self.cancel_pinjam )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def save_pinjam( self, event ):
		event.Skip()
	
	def cancel_pinjam( self, event ):
		event.Skip()
	

###########################################################################
## Class InBuku
###########################################################################

class InBuku ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,327 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"Input Data Buku", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.m_staticText82.Wrap( -1 )
		self.m_staticText82.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		bSizer14.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"No. Buku", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.nobuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nobuku.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.nobuku, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.judul = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.judul.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.judul, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Jenis Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.jenisbuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenisbuku.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.jenisbuku, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Pengarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.pengarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pengarang.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.pengarang, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.save_buku )
		self.m_button12.Bind( wx.EVT_BUTTON, self.cancel_buku )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def save_buku( self, event ):
		event.Skip()
	
	def cancel_buku( self, event ):
		event.Skip()
	

###########################################################################
## Class InAnggota
###########################################################################

class InAnggota ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,327 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Input Data Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_staticText44.SetMinSize( wx.Size( -1,35 ) )
		
		bSizer7.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"No. Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.noanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.noanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.noanggota, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nama Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.namaanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.namaanggota, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.alamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alamat.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.alamat, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"No. Handphone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.nohp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nohp.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.nohp, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.save_anggota )
		self.m_button12.Bind( wx.EVT_BUTTON, self.cancel_anggota )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def save_anggota( self, event ):
		event.Skip()
	
	def cancel_anggota( self, event ):
		event.Skip()
	

###########################################################################
## Class InEditAnggota
###########################################################################

class InEditAnggota ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,429 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Edit Data Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_staticText44.SetMinSize( wx.Size( -1,35 ) )
		
		bSizer7.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"No. Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.noanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.noanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.noanggota, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nama Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.namaanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.namaanggota, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.alamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alamat.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.alamat, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"No. Handphone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.nohp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nohp.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.nohp, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.edit_anggota )
		self.m_button12.Bind( wx.EVT_BUTTON, self.cancel_anggota )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def edit_anggota( self, event ):
		event.Skip()
	
	def cancel_anggota( self, event ):
		event.Skip()
	

###########################################################################
## Class InEditBuku
###########################################################################

class InEditBuku ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,427 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"Edit Data Buku", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.m_staticText82.Wrap( -1 )
		self.m_staticText82.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		bSizer14.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"No. Buku", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.nobuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nobuku.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.nobuku, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.judul = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.judul.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.judul, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Jenis Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.jenisbuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenisbuku.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.jenisbuku, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Pengarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.pengarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pengarang.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.pengarang, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.edit_buku )
		self.m_button12.Bind( wx.EVT_BUTTON, self.cancel_buku )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def edit_buku( self, event ):
		event.Skip()
	
	def cancel_buku( self, event ):
		event.Skip()
	

###########################################################################
## Class InEditPeminjaman
###########################################################################

class InEditPeminjaman ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,502 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Edit Peminjaman Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		self.m_staticText50.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_staticText50.SetMinSize( wx.Size( -1,35 ) )
		
		bSizer8.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Id Peminjaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		self.m_staticText45.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.noanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.noanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.noanggota, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"No Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		self.m_staticText46.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.namaanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaanggota.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		fgSizer14.Add( self.namaanggota, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"No Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		self.m_staticText47.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.nobuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nobuku.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.nobuku, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		self.m_staticText48.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.judul = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.judul.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.judul, 0, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Pinjam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		self.m_staticText49.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.pinjam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pinjam.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.pinjam, 0, wx.ALL, 5 )
		
		self.m_staticText491 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText491.Wrap( -1 )
		self.m_staticText491.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText491, 0, wx.ALL, 5 )
		
		self.kembali = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kembali.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.kembali, 0, wx.ALL, 5 )
		
		self.m_button331 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button331.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button331.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button331.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer14.Add( self.m_button331, 0, wx.ALL, 5 )
		
		self.m_button332 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button332.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button332.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button332.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer14.Add( self.m_button332, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( fgSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button331.Bind( wx.EVT_BUTTON, self.edit_pinjam )
		self.m_button332.Bind( wx.EVT_BUTTON, self.cancel_pinjam )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def edit_pinjam( self, event ):
		event.Skip()
	
	def cancel_pinjam( self, event ):
		event.Skip()
	

###########################################################################
## Class InDeletePeminjaman
###########################################################################

class InDeletePeminjaman ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,502 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Delete Peminjaman Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		self.m_staticText50.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_staticText50.SetMinSize( wx.Size( -1,35 ) )
		
		bSizer8.Add( self.m_staticText50, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Id Peminjaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		self.m_staticText45.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.noanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.noanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer14.Add( self.noanggota, 0, wx.ALL, 5 )
		
		self.m_button331 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button331.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button331.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button331.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer14.Add( self.m_button331, 0, wx.ALL, 5 )
		
		self.m_button332 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button332.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button332.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button332.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer14.Add( self.m_button332, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( fgSizer14, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button331.Bind( wx.EVT_BUTTON, self.delete_pinjam )
		self.m_button332.Bind( wx.EVT_BUTTON, self.cancel_pinjam )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def delete_pinjam( self, event ):
		event.Skip()
	
	def cancel_pinjam( self, event ):
		event.Skip()
	

###########################################################################
## Class InDeleteAnggota
###########################################################################

class InDeleteAnggota ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,429 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Delete Data Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_staticText44.SetMinSize( wx.Size( -1,35 ) )
		
		bSizer7.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"No. Anggota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.noanggota = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.noanggota.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.noanggota, 0, wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.delete_anggota )
		self.m_button12.Bind( wx.EVT_BUTTON, self.cancel_anggota )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def delete_anggota( self, event ):
		event.Skip()
	
	def cancel_anggota( self, event ):
		event.Skip()
	

###########################################################################
## Class InDeleteBuku
###########################################################################

class InDeleteBuku ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 493,427 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.SetBackgroundColour( wx.Colour( 209, 208, 244 ) )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"Delete Data Buku", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.m_staticText82.Wrap( -1 )
		self.m_staticText82.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		bSizer14.Add( self.m_staticText82, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"No. Buku", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.nobuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nobuku.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		
		fgSizer3.Add( self.nobuku, 0, wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button11.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.m_button12.SetFont( wx.Font( 9, 70, 90, 90, False, "Amaranth" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button11.Bind( wx.EVT_BUTTON, self.delete_buku )
		self.m_button12.Bind( wx.EVT_BUTTON, self.cancel_buku )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def delete_buku( self, event ):
		event.Skip()
	
	def cancel_buku( self, event ):
		event.Skip()
	

