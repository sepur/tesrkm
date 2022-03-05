from django.db import models

class TblTes(models.Model):
    nama_barang = models.CharField(max_length=50,blank=True,null=True)
    kode_barang = models.CharField(max_length=2,blank=True,null=True)
    tanggal = models.DateField(blank=True,null=True)
    harga = models.FloatField()

    class Meta:
        db_table = 'tbltes'
        verbose_name ='TblTes'
        verbose_name_plural = verbose_name

# Create your models here.
