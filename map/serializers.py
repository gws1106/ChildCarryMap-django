
# from rest_framework import serializers
# from .models import Waterplay
# from .models import Toilet, Conv, Medi, Safe112, Safe119, Parking, User


# class WaterplaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Waterplay
#         fields = [
#             "waterplayname",
#             "waterplayimgurl",
#             "waterplayaddrold",
#             "waterplayaddrnew",
#             "waterplaytelno",
#             "waterplayurl",
#             "waterplayname01",
#             "waterplayvalue01",
#             "waterplayname02",
#             "waterplayvalue02",
#             "waterplayname03",
#             "waterplayvalue03",
#             "waterplayname04",
#             "waterplayvalue04",
#             "waterplayname05",
#             "waterplayvalue05",
#             "waterplayname06",
#             "waterplayvalue06",
#             "waterplayname07",
#             "waterplayvalue07",
#             "waterplaytypeid",
#             "waterplaytype",
#             "waterplayla",
#             "waterplaylo",
#             "waterplayscoretoilet",
#             "waterplayscoreconv",
#             "waterplayscoredrug",
#             "waterplayscoremedi",
#             "waterplayscoresafe112",
#             "waterplayscoresafe119",
#             "waterplayscoreparking",
#             "waterplayscorefaci",
#             "waterplayscorefacidesc",
#             "waterplayscorereview",
#             "waterplayshortvalue01",
#             "waterplayscoremean",
#             "waterplaywordcloudurl",
#         ]


# class ToiletSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Toilet
#         fields = [
#             "toiletid",
#             "toiletname",
#             "toiletsido",
#             "toiletsigngu",
#             "toiletdongcode",
#             "toiletdong",
#             "toiletaddrnew",
#             "toiletaddrold",
#             "toiletla",
#             "toiletlo",
#             "toilettype",
#         ]


# class ConvSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Conv
#         fields = [
#             "convid",
#             "convname",
#             "convsido",
#             "convsigngu",
#             "convdong",
#             "convdongcode",
#             "convlo",
#             "convla",
#             "convtype",
#         ]


# class MediSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Medi
#         fields = [
#             "mediid",
#             "mediname",
#             "medisido",
#             "medisigngu",
#             "medidong",
#             "medidongcode",
#             "medilo",
#             "medila",
#             "meditype",
#         ]


# class Safe112Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Safe112
#         fields = [
#             "safe112id",
#             "safe112subtype",
#             "safe112name",
#             "safe112sido",
#             "safe112signgu",
#             "safe112dongcode",
#             "safe112dong",
#             "safe112lo",
#             "safe112la",
#         ]


# class Safe119Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Safe119
#         fields = [
#             "safe119id",
#             "safe119name",
#             "safe119subtype",
#             "safe119lo",
#             "safe119la",
#         ]


# class ParkingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Parking
#         fields = [
#             "parkingid",
#             "parkingname",
#             "parkingsido",
#             "parkingsigngu",
#             "parkingdongcode",
#             "parkingdong",
#             "parkingaddrnew",
#             "parkinglo",
#             "parkingla",
#             "parkingtype",
#             "parkingspceco",
#             "parkingutiliizalmttflagnm",
#             "parkingwkdaynm",
#             "parkingworkdayopnbsnstime",
#             "parkingworkdayclostime",
#             "parkingsatopnbsnstime",
#             "parkingsatclostime",
#             "parkingsunopnbsnstime",
#             "parkingsunclostime",
#             "parkingutiliizachrgecn",
#         ]


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "userid",
#             "userpw",
#         ]

from rest_framework import serializers
from .models import Waterplay
from .models import Toilet, Conv, Medi, Safe112, Safe119, Parking, User


class WaterplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Waterplay
        fields = [
            "waterplayname",
            "waterplayimgurl",
            "waterplayaddrold",
            "waterplayaddrnew",
            "waterplaytelno",
            "waterplayurl",
            "waterplayname01",
            "waterplayvalue01",
            "waterplayname02",
            "waterplayvalue02",
            "waterplayname03",
            "waterplayvalue03",
            "waterplayname04",
            "waterplayvalue04",
            "waterplayname05",
            "waterplayvalue05",
            "waterplayname06",
            "waterplayvalue06",
            "waterplayname07",
            "waterplayvalue07",
            "waterplaytypeid",
            "waterplaytype",
            "waterplayla",
            "waterplaylo",
            "waterplayscoretoilet",
            "waterplayscoreconv",
            "waterplayscoredrug",
            "waterplayscoremedi",
            "waterplayscoresafe112",
            "waterplayscoresafe119",
            "waterplayscoreparking",
            "waterplayscorefaci",
            "waterplayscorefacidesc",
            "waterplayscorereview",
            "waterplayshortvalue01",
            "waterplayscoremean",
            "waterplaywordcloudurl",
            "waterplayscoretoiletmean",
            "waterplayscoreconvmean",
            "waterplayscoredrugmean",
            "waterplayscoremedimean",
            "waterplayscoresafe112mean",
            "waterplayscoresafe119mean",
            "waterplayscoreparkingmean",
        ]


class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = [
            "toiletid",
            "toiletname",
            "toiletsido",
            "toiletsigngu",
            "toiletdongcode",
            "toiletdong",
            "toiletaddrnew",
            "toiletaddrold",
            "toiletla",
            "toiletlo",
            "toilettype",
        ]


class ConvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conv
        fields = [
            "convid",
            "convname",
            "convsido",
            "convsigngu",
            "convdong",
            "convdongcode",
            "convlo",
            "convla",
            "convtype",
        ]


class MediSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medi
        fields = [
            "mediid",
            "mediname",
            "medisido",
            "medisigngu",
            "medidong",
            "medidongcode",
            "medilo",
            "medila",
            "meditype",
        ]


class Safe112Serializer(serializers.ModelSerializer):
    class Meta:
        model = Safe112
        fields = [
            "safe112id",
            "safe112subtype",
            "safe112name",
            "safe112sido",
            "safe112signgu",
            "safe112dongcode",
            "safe112dong",
            "safe112lo",
            "safe112la",
        ]


class Safe119Serializer(serializers.ModelSerializer):
    class Meta:
        model = Safe119
        fields = [
            "safe119id",
            "safe119name",
            "safe119subtype",
            "safe119lo",
            "safe119la",
        ]


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = [
            "parkingid",
            "parkingname",
            "parkingsido",
            "parkingsigngu",
            "parkingdongcode",
            "parkingdong",
            "parkingaddrnew",
            "parkinglo",
            "parkingla",
            "parkingtype",
            "parkingspceco",
            "parkingutiliizalmttflagnm",
            "parkingwkdaynm",
            "parkingworkdayopnbsnstime",
            "parkingworkdayclostime",
            "parkingsatopnbsnstime",
            "parkingsatclostime",
            "parkingsunopnbsnstime",
            "parkingsunclostime",
            "parkingutiliizachrgecn",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "userid",
            "userpw",
        ]