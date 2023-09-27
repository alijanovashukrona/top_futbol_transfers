from django.db import models

class Club(models.Model):
    nom=models.CharField(max_length=200,blank=True,null=True)
    logo=models.FileField()
    davlat=models.CharField(max_length=100,blank=True,null=True)
    prezident=models.CharField(max_length=100,blank=True,null=True)
    murabbiy=models.CharField(max_length=100,blank=True,null=True)
    yil=models.DateTimeField()

class Player(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    age=models.SmallIntegerField()
    position=models.CharField(max_length=100,blank=True,null=True)
    klub=models.ForeignKey(Club,on_delete=models.CASCADE)
    narx=models.IntegerField()
    davlat=models.CharField(max_length=100,blank=True,null=True)
    t_yil=models.CharField(max_length=20,blank=True,null=True)

class Transfer(models.Model):
    eski=models.ForeignKey(Club,on_delete=models.CASCADE,related_name='sotganlari')
    yangi=models.ForeignKey(Club,on_delete=models.CASCADE)
    narx=models.ForeignKey(Club,on_delete=models.CASCADE)
