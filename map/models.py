     
# from django.db import models


# class Waterplay(models.Model):
#     waterplayname = models.CharField(primary_key=True, max_length=30)
#     waterplayimgurl = models.TextField(blank=True, null=True)
#     waterplayaddrold = models.TextField(blank=True, null=True)
#     waterplayaddrnew = models.TextField(blank=True, null=True)
#     waterplaytelno = models.TextField(blank=True, null=True)
#     waterplayurl = models.TextField(blank=True, null=True)
#     waterplayname01 = models.TextField(blank=True, null=True)
#     waterplayvalue01 = models.TextField(blank=True, null=True)
#     waterplayname02 = models.TextField(blank=True, null=True)
#     waterplayvalue02 = models.TextField(blank=True, null=True)
#     waterplayname03 = models.TextField(blank=True, null=True)
#     waterplayvalue03 = models.TextField(blank=True, null=True)
#     waterplayname04 = models.TextField(blank=True, null=True)
#     waterplayvalue04 = models.TextField(blank=True, null=True)
#     waterplayname05 = models.TextField(blank=True, null=True)
#     waterplayvalue05 = models.TextField(blank=True, null=True)
#     waterplayname06 = models.TextField(blank=True, null=True)
#     waterplayvalue06 = models.TextField(blank=True, null=True)
#     waterplayname07 = models.TextField(blank=True, null=True)
#     waterplayvalue07 = models.TextField(blank=True, null=True)
#     waterplaytypeid = models.TextField(blank=True, null=True)
#     waterplaytype = models.TextField(blank=True, null=True)
#     waterplayla = models.FloatField(blank=True, null=True)
#     waterplaylo = models.FloatField(blank=True, null=True)
#     waterplayscoretoilet = models.FloatField(blank=True, null=True)
#     waterplayscoreconv = models.FloatField(blank=True, null=True)
#     waterplayscoredrug = models.FloatField(blank=True, null=True)
#     waterplayscoremedi = models.FloatField(blank=True, null=True)
#     waterplayscoresafe112 = models.FloatField(blank=True, null=True)
#     waterplayscoresafe119 = models.FloatField(blank=True, null=True)
#     waterplayscoreparking = models.FloatField(blank=True, null=True)
#     waterplayscorefaci = models.IntegerField(blank=True, null=True)
#     waterplayscorefacidesc = models.TextField(blank=True, null=True)
#     waterplayscorereview = models.IntegerField(blank=True, null=True)
#     waterplayshortvalue01 = models.TextField(blank=True, null=True)
#     waterplayscoremean = models.IntegerField(blank=True, null=True)
#     waterplaywordcloudurl = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'waterplay'


# class Toilet(models.Model):
#     toiletid = models.CharField(primary_key=True, max_length=30)
#     toiletname = models.TextField(blank=True, null=True)
#     toiletsido = models.TextField(blank=True, null=True)
#     toiletsigngu = models.TextField(blank=True, null=True)
#     toiletdongcode = models.TextField(blank=True, null=True)
#     toiletdong = models.TextField(blank=True, null=True)
#     toiletaddrnew = models.TextField(blank=True, null=True)
#     toiletaddrold = models.TextField(blank=True, null=True)
#     toiletla = models.FloatField(blank=True, null=True)
#     toiletlo = models.FloatField(blank=True, null=True)
#     toilettype = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'toilet'


# class Conv(models.Model):
#     convid = models.CharField(primary_key=True, max_length=30)
#     convname = models.TextField(blank=True, null=True)
#     convsido = models.TextField(blank=True, null=True)
#     convsigngu = models.TextField(blank=True, null=True)
#     convdong = models.TextField(blank=True, null=True)
#     convdongcode = models.TextField(blank=True, null=True)
#     convlo = models.FloatField(blank=True, null=True)
#     convla = models.FloatField(blank=True, null=True)
#     convtype = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'conv'


# class Medi(models.Model):
#     mediid = models.CharField(primary_key=True, max_length=30)
#     mediname = models.TextField(blank=True, null=True)
#     medisido = models.TextField(blank=True, null=True)
#     medisigngu = models.TextField(blank=True, null=True)
#     medidong = models.TextField(blank=True, null=True)
#     medidongcode = models.TextField(blank=True, null=True)
#     medilo = models.FloatField(blank=True, null=True)
#     medila = models.FloatField(blank=True, null=True)
#     meditype = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'medi'


# class Safe112(models.Model):
#     safe112id = models.CharField(primary_key=True, max_length=30)
#     safe112subtype = models.TextField(blank=True, null=True)
#     safe112name = models.TextField(blank=True, null=True)
#     safe112sido = models.TextField(blank=True, null=True)
#     safe112signgu = models.TextField(blank=True, null=True)
#     safe112dongcode = models.TextField(blank=True, null=True)
#     safe112dong = models.TextField(blank=True, null=True)
#     safe112lo = models.FloatField(blank=True, null=True)
#     safe112la = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'safe112'


# class Safe119(models.Model):
#     safe119id = models.CharField(primary_key=True, max_length=30)
#     safe119name = models.TextField(blank=True, null=True)
#     safe119subtype = models.TextField(blank=True, null=True)
#     safe119lo = models.FloatField(blank=True, null=True)
#     safe119la = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'safe119'


# class Parking(models.Model):
#     parkingid = models.CharField(primary_key=True, max_length=30)
#     parkingname = models.TextField(blank=True, null=True)
#     parkingsido = models.TextField(blank=True, null=True)
#     parkingsigngu = models.TextField(blank=True, null=True)
#     parkingdongcode = models.TextField(blank=True, null=True)
#     parkingdong = models.TextField(blank=True, null=True)
#     parkingaddrnew = models.TextField(blank=True, null=True)
#     parkinglo = models.FloatField(blank=True, null=True)
#     parkingla = models.FloatField(blank=True, null=True)
#     parkingtype = models.TextField(blank=True, null=True)
#     parkingspceco = models.IntegerField(blank=True, null=True)
#     parkingutiliizalmttflagnm = models.TextField(blank=True, null=True)
#     parkingwkdaynm = models.TextField(blank=True, null=True)
#     parkingworkdayopnbsnstime = models.TextField(blank=True, null=True)
#     parkingworkdayclostime = models.TextField(blank=True, null=True)
#     parkingsatopnbsnstime = models.TextField(blank=True, null=True)
#     parkingsatclostime = models.TextField(blank=True, null=True)
#     parkingsunopnbsnstime = models.TextField(blank=True, null=True)
#     parkingsunclostime = models.TextField(blank=True, null=True)
#     parkingutiliizachrgecn = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'parking'


# class User(models.Model):
#     userid = models.CharField(primary_key=True, max_length=30)
#     userpw = models.CharField(max_length=30)

#     class Meta:
#         managed = False
#         db_table = 'user'

from django.db import models


class Waterplay(models.Model):
    waterplayname = models.CharField(primary_key=True, max_length=30)
    waterplayimgurl = models.TextField(blank=True, null=True)
    waterplayaddrold = models.TextField(blank=True, null=True)
    waterplayaddrnew = models.TextField(blank=True, null=True)
    waterplaytelno = models.TextField(blank=True, null=True)
    waterplayurl = models.TextField(blank=True, null=True)
    waterplayname01 = models.TextField(blank=True, null=True)
    waterplayvalue01 = models.TextField(blank=True, null=True)
    waterplayname02 = models.TextField(blank=True, null=True)
    waterplayvalue02 = models.TextField(blank=True, null=True)
    waterplayname03 = models.TextField(blank=True, null=True)
    waterplayvalue03 = models.TextField(blank=True, null=True)
    waterplayname04 = models.TextField(blank=True, null=True)
    waterplayvalue04 = models.TextField(blank=True, null=True)
    waterplayname05 = models.TextField(blank=True, null=True)
    waterplayvalue05 = models.TextField(blank=True, null=True)
    waterplayname06 = models.TextField(blank=True, null=True)
    waterplayvalue06 = models.TextField(blank=True, null=True)
    waterplayname07 = models.TextField(blank=True, null=True)
    waterplayvalue07 = models.TextField(blank=True, null=True)
    waterplaytypeid = models.TextField(blank=True, null=True)
    waterplaytype = models.TextField(blank=True, null=True)
    waterplayla = models.FloatField(blank=True, null=True)
    waterplaylo = models.FloatField(blank=True, null=True)
    waterplayscoretoilet = models.FloatField(blank=True, null=True)
    waterplayscoreconv = models.FloatField(blank=True, null=True)
    waterplayscoredrug = models.FloatField(blank=True, null=True)
    waterplayscoremedi = models.FloatField(blank=True, null=True)
    waterplayscoresafe112 = models.FloatField(blank=True, null=True)
    waterplayscoresafe119 = models.FloatField(blank=True, null=True)
    waterplayscoreparking = models.FloatField(blank=True, null=True)
    waterplayscorefaci = models.IntegerField(blank=True, null=True)
    waterplayscorefacidesc = models.TextField(blank=True, null=True)
    waterplayscorereview = models.IntegerField(blank=True, null=True)
    waterplayshortvalue01 = models.TextField(blank=True, null=True)
    waterplayscoremean = models.IntegerField(blank=True, null=True)
    waterplaywordcloudurl = models.TextField(blank=True, null=True)
    waterplayscoretoiletmean = models.FloatField(blank=True, null=True)
    waterplayscoreconvmean = models.FloatField(blank=True, null=True)
    waterplayscoredrugmean = models.FloatField(blank=True, null=True)
    waterplayscoremedimean = models.FloatField(blank=True, null=True)
    waterplayscoresafe112mean = models.FloatField(blank=True, null=True)
    waterplayscoresafe119mean = models.FloatField(blank=True, null=True)
    waterplayscoreparkingmean = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'waterplay'


class Toilet(models.Model):
    toiletid = models.CharField(primary_key=True, max_length=30)
    toiletname = models.TextField(blank=True, null=True)
    toiletsido = models.TextField(blank=True, null=True)
    toiletsigngu = models.TextField(blank=True, null=True)
    toiletdongcode = models.TextField(blank=True, null=True)
    toiletdong = models.TextField(blank=True, null=True)
    toiletaddrnew = models.TextField(blank=True, null=True)
    toiletaddrold = models.TextField(blank=True, null=True)
    toiletla = models.FloatField(blank=True, null=True)
    toiletlo = models.FloatField(blank=True, null=True)
    toilettype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toilet'


class Conv(models.Model):
    convid = models.CharField(primary_key=True, max_length=30)
    convname = models.TextField(blank=True, null=True)
    convsido = models.TextField(blank=True, null=True)
    convsigngu = models.TextField(blank=True, null=True)
    convdong = models.TextField(blank=True, null=True)
    convdongcode = models.TextField(blank=True, null=True)
    convlo = models.FloatField(blank=True, null=True)
    convla = models.FloatField(blank=True, null=True)
    convtype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conv'


class Medi(models.Model):
    mediid = models.CharField(primary_key=True, max_length=30)
    mediname = models.TextField(blank=True, null=True)
    medisido = models.TextField(blank=True, null=True)
    medisigngu = models.TextField(blank=True, null=True)
    medidong = models.TextField(blank=True, null=True)
    medidongcode = models.TextField(blank=True, null=True)
    medilo = models.FloatField(blank=True, null=True)
    medila = models.FloatField(blank=True, null=True)
    meditype = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medi'


class Safe112(models.Model):
    safe112id = models.CharField(primary_key=True, max_length=30)
    safe112subtype = models.TextField(blank=True, null=True)
    safe112name = models.TextField(blank=True, null=True)
    safe112sido = models.TextField(blank=True, null=True)
    safe112signgu = models.TextField(blank=True, null=True)
    safe112dongcode = models.TextField(blank=True, null=True)
    safe112dong = models.TextField(blank=True, null=True)
    safe112lo = models.FloatField(blank=True, null=True)
    safe112la = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safe112'


class Safe119(models.Model):
    safe119id = models.CharField(primary_key=True, max_length=30)
    safe119name = models.TextField(blank=True, null=True)
    safe119subtype = models.TextField(blank=True, null=True)
    safe119lo = models.FloatField(blank=True, null=True)
    safe119la = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safe119'


class Parking(models.Model):
    parkingid = models.CharField(primary_key=True, max_length=30)
    parkingname = models.TextField(blank=True, null=True)
    parkingsido = models.TextField(blank=True, null=True)
    parkingsigngu = models.TextField(blank=True, null=True)
    parkingdongcode = models.TextField(blank=True, null=True)
    parkingdong = models.TextField(blank=True, null=True)
    parkingaddrnew = models.TextField(blank=True, null=True)
    parkinglo = models.FloatField(blank=True, null=True)
    parkingla = models.FloatField(blank=True, null=True)
    parkingtype = models.TextField(blank=True, null=True)
    parkingspceco = models.IntegerField(blank=True, null=True)
    parkingutiliizalmttflagnm = models.TextField(blank=True, null=True)
    parkingwkdaynm = models.TextField(blank=True, null=True)
    parkingworkdayopnbsnstime = models.TextField(blank=True, null=True)
    parkingworkdayclostime = models.TextField(blank=True, null=True)
    parkingsatopnbsnstime = models.TextField(blank=True, null=True)
    parkingsatclostime = models.TextField(blank=True, null=True)
    parkingsunopnbsnstime = models.TextField(blank=True, null=True)
    parkingsunclostime = models.TextField(blank=True, null=True)
    parkingutiliizachrgecn = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parking'


class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=30)
    userpw = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user'
