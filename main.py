import wx
import wx.grid
from data import Data
import Perpus

import sqlite3


class GUI1(Perpus.MyFrame1):
    def __init__(self, parent):
        Perpus.MyFrame1.__init__(self,parent)
    def button_login(self, event):
        username = str(self.m_textCtrl25.GetValue())
        password = str(self.m_textCtrl26.GetValue())
        if username == "admin" and password == "admin" :
            wx.MessageBox('Login Berhasil', 'informasi',wx.OK | wx.ICON_INFORMATION)
            print('Login Berhasil')
            frame = GUI2(parent=None)
            frame.Show()
            self.Destroy()

        
class GUI2(Data, Perpus.MyFrame2):
    def __init__(self, parent):
        Perpus.MyFrame2.__init__(self,parent)
        self.m_grid3121.SetColLabelValue(0, "No Anggota")
        self.m_grid3121.SetColLabelValue(1, "Nama Anggota")
        self.m_grid3121.SetColLabelValue(2, "Alamat")
        self.m_grid3121.SetColLabelValue(3, "No Handphone")
        self.m_grid3121.SetColLabelValue(4, "Aksi")
        self.m_grid3111.SetColLabelValue(0, "No Buku")
        self.m_grid3111.SetColLabelValue(1, "Judul")
        self.m_grid3111.SetColLabelValue(2, "Jenis Buku")
        self.m_grid3111.SetColLabelValue(3, "Pengarang")
        self.m_grid3111.SetColLabelValue(4, "Aksi")
        self.m_grid312.SetColLabelValue(0, "Id Peminjaman")
        self.m_grid312.SetColLabelValue(1, "No Anggota")
        self.m_grid312.SetColLabelValue(2, "No Buku")
        self.m_grid312.SetColLabelValue(3, "Judul")
        self.m_grid312.SetColLabelValue(4, "Tanggal Pinjam")
        self.m_grid312.SetColLabelValue(5, "Tanggal kembali")
        self.m_grid312.SetColLabelValue(6, "Aksi")
        self.execute = Data()  
        self.query = 'SELECT * FROM Anggota'
        self.query1 = 'SELECT * FROM Buku'
        self.query2 = 'SELECT * FROM Peminjaman'
        hasil = self.execute.Run(self.query, returnData=True)
        hasil1 = self.execute.Run(self.query1, returnData=True)
        hasil2 = self.execute.Run(self.query2, returnData=True)
        
        if len(hasil)>5:
            self.m_grid3121.AppendRows(len(hasil)-5)
        if len(hasil1)>5:
            self.m_grid3111.AppendRows(len(hasil1)-5)
        if len(hasil2)>5:
            self.m_grid312.AppendRows(len(hasil2)-5)
            
        for i in range(len(hasil)):
            for j in range(len(hasil[i])):
                 self.m_grid3121.SetCellValue(i, j, str(hasil[i][j]))
        for k in range(len(hasil1)):
            for l in range(len(hasil1[k])):
                 self.m_grid3111.SetCellValue(k, l, str(hasil1[k][l]))
        for i in range(len(hasil2)):
            for j in range(len(hasil2[i])):
                 self.m_grid312.SetCellValue(i, j, str(hasil2[i][j])) 
    def anggota(self, event):
        modal =Modal1(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def edit(self, event):
        modal =edit_anggota(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def edit_2(self, event):
        modal = edit_buku(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def edit_3(self,event):
        modal = edit_peminjaman(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def hapus(self, event):
        modal = delete_Anggota(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def hapus_2(self, event):
        modal = delete_buku(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def hapus_3(self, event):
        modal = delete_peminjaman(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def buku(self, event):
        modal =Modal2(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def pinjam(self, event):
        modal =Modal3(parent=None)
        modal.ShowModal()
        if modal.Destroy() == True:
            self.Destroy()
    def Keluar(self, event):
        self.Destroy()
        frame= GUI1(parent=None)
        frame.Show()
    


class Modal1(Data,Perpus.InAnggota):
    def __init__(self, parent):
        Perpus.InAnggota.__init__(self,parent)
        self.execute = Data()
    def cancel_anggota(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()
    def save_anggota(self, event):
        no = self.noanggota.GetValue()
        nama = self.namaanggota.GetValue()
        alamat = self.alamat.GetValue()
        nohp = self.nohp.GetValue()
        if len(no)>0 and len(nama)>0 and len(alamat)>0 and len(nohp)>0:
            self.query = "INSERT INTO Anggota (No_Anggota, Nama_Anggota, Alamat, No_Handphone) VALUES (\'%s\', \'%s\', \'%s\', \'%s\')"
            self.query = self.query % (no, nama, alamat, nohp)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()           
class Modal2(Data,Perpus.InBuku):
    def __init__(self, parent):
        Perpus.InBuku.__init__(self,parent)
        self.execute = Data()
    def cancel_buku(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()
    def save_buku(self, event):
        no = self.nobuku.GetValue()
        judul = self.judul.GetValue()
        jenis = self.jenisbuku.GetValue()
        pengarang = self.pengarang.GetValue()
        if "" not in(no,judul,jenis,pengarang):
            self.query = "INSERT INTO Buku (No_Buku, Judul, Jenis_Buku, Pengarang) VALUES (\'%s\', \'%s\', \'%s\', \'%s\')"
            self.query = self.query % (no, judul, jenis, pengarang)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()
class Modal3(Data, Perpus.InPeminjaman):
    def __init__(self, parent):
        Perpus.InPeminjaman.__init__(self,parent)
        self.execute = Data()
    def cancel_pinjam(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()
    def save_pinjam(self, event):
        noanggota = self.noanggota.GetValue()
        nama = self.namaanggota.GetValue()
        nobuku = self.nobuku.GetValue()
        judul = self.judul.GetValue()
        pinjam = self.pinjam.GetValue()
        kembali = self.pinjam.GetValue()
        if "" not in(noanggota,nama,nobuku,judul,pinjam,kembali):
            self.query = "INSERT INTO Peminjaman (Id_Peminjaman, No_Anggota, No_Buku, Judul, Tanggal_Pinjam, Tanggal_Kembali) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')"
            self.query = self.query % (noanggota,nama,nobuku,judul,pinjam,kembali)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()


class edit_anggota(Data,Perpus.InEditAnggota):
    def __init__(self, parent):
        Perpus.InEditAnggota.__init__(self,parent)
        self.execute = Data()
    def edit_anggota(self, event):
        noanggota = self.noanggota.GetValue()
        self.query = "SELECT * FROM Anggota WHERE No_Anggota = (\'%s\')"
        self.query = self.query % (noanggota)
        hasil = self.execute.Run(self.query, returnData=True)
        if len(hasil)>0:
            nama = self.namaanggota.GetValue()
            alamat = self.alamat.GetValue()
            no = self.nohp.GetValue()
            self.query = "Update Anggota set Nama_Anggota = (\'%s\'), Alamat = (\'%s\'), No_Handphone = (\'%s\') WHERE No_Anggota = (\'%s\')"
            self.query = self.query % (nama,alamat,no,noanggota)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()
    def cancel_anggota(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()
        


class edit_buku(Data, Perpus.InEditBuku):
    def __init__(self, parent):
        Perpus.InEditBuku.__init__(self,parent)
        self.execute = Data()
    def edit_buku(self, event):
        nobuku = self.nobuku.GetValue()
        self.query = "SELECT * FROM Buku WHERE No_Buku = (\'%s\')"
        self.query = self.query % (nobuku)
        hasil = self.execute.Run(self.query, returnData=True)
        if len(hasil)>0:
            judul = self.judul.GetValue()
            jenis = self.jenisbuku.GetValue()
            pengarang = self.pengarang.GetValue()
            self.query = "Update Buku set Judul = (\'%s\'), Jenis_Buku = (\'%s\'), Pengarang = (\'%s\') WHERE No_Buku = (\'%s\')"
            self.query = self.query % (judul,jenis,pengarang,nobuku)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()
    def cancel_buku(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()

class edit_peminjaman(Data, Perpus.InEditPeminjaman):
    def __init__(self, parent):
       Perpus.InEditPeminjaman.__init__(self,parent)
       self.execute = Data()
    def edit_pinjam(self, event):
        no = self.noanggota.GetValue()
        self.query = "SELECT * FROM Peminjaman WHERE Id_Peminjaman = (\'%s\')"
        self.query = self.query % (no)
        hasil = self.execute.Run(self.query, returnData=True)
        if len(hasil)>0:
            nama = self.namaanggota.GetValue()
            nobuku = self.nobuku.GetValue()
            judul = self.judul.GetValue()
            pinjam = self.pinjam.GetValue()
            kembali = self.pinjam.GetValue()
            self.query = "Update Peminjaman set No_Anggota = (\'%s\'), No_Buku = (\'%s\'), Judul = (\'%s\'), Tanggal_Pinjam = (\'%s\'), Tanggal_Kembali = (\'%s\') WHERE Id_Peminjaman = (\'%s\')"
            self.query = self.query % (nama, nobuku, judul, pinjam, kembali, no)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()
    def cancel_pinjam(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()

        

class delete_Anggota(Data, Perpus.InDeleteAnggota):
    def __init__(self, parent):
        Perpus.InDeleteAnggota.__init__(self,parent)
        self.execute = Data()
    def delete_anggota(self, event):
        no = self.noanggota.GetValue()
        self.query = "SELECT * FROM Anggota WHERE No_Anggota = (\'%s\')"
        self.query = self.query % (no)
        hasil = self.execute.Run(self.query, returnData=True)
        if len(hasil)>0:
            self.query = "DELETE FROM Anggota WHERE No_Anggota = (\'%s\')"
            self.query = self.query % (no)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()
    def cancel_anggota(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()
class delete_buku(Data, Perpus.InDeleteBuku):
    def __init__(self, parent):
        Perpus.InDeleteBuku.__init__(self,parent)
        self.execute = Data()
    def delete_buku(self, event):
        no = self.nobuku.GetValue()
        self.query = "SELECT * FROM Buku WHERE No_Buku = (\'%s\')"
        self.query = self.query % (no)
        hasil = self.execute.Run(self.query, returnData=True)
        if len(hasil)>0:
            self.query = "DELETE FROM Buku WHERE No_Buku = (\'%s\')"
            self.query = self.query % (no)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()
    def cancel_buku(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()
        
class delete_peminjaman(Data, Perpus.InDeletePeminjaman):
    def __init__(self, parent):
        Perpus.InDeletePeminjaman.__init__(self,parent)
        self.execute = Data()
    def delete_pinjam(self, event):
        no = self.noanggota.GetValue()
        self.query = "SELECT * FROM Peminjaman WHERE Id_Peminjaman = (\'%s\')"
        self.query = self.query % (no)
        hasil = self.execute.Run(self.query, returnData=True)
        if len(hasil)>0:
            self.query = "DELETE FROM Peminjaman WHERE Id_Peminjaman = (\'%s\')"
            self.query = self.query % (no)
            self.execute.Run(self.query)
            self.Destroy()
            frame= GUI2(parent=None)
            frame.Show()
    def cancel_pinjam(self, event):
        self.Destroy()
        frame= GUI2(parent=None)
        frame.Show()

        
            
app = wx.App()
frame = GUI1(parent=None)
frame.Show()
app.MainLoop()
