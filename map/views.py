# from rest_framework import mixins, generics
# from django.http import JsonResponse

# from .models import Waterplay, Toilet, Conv, Medi, Safe112, Safe119, Parking
# from .serializers import WaterplaySerializer, ToiletSerializer, ConvSerializer, MediSerializer, Safe112Serializer, Safe119Serializer, ParkingSerializer


# class WpAllsAPIMixins(
#     mixins.ListModelMixin, 
#     mixins.CreateModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Waterplay.objects.all()
#     serializer_class = WaterplaySerializer
    
#     # 모든 물놀이장 정보 출력 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    

# class WpTypeidsAPIMixins(
#     generics.ListAPIView
# ):
#     serializer_class = WaterplaySerializer
#     lookup_field = "waterplaytypeid"
    
#     # 종류별 물놀이장 정보 출력 
#     # 선택 종류 : 1(물놀이장), 2((야외)수영장), 3(바닥분수)
#     def get_queryset(self):
#         print(self.kwargs["waterplaytypeid"])
        
#         if self.kwargs["waterplaytypeid"] == 1:
#             return Waterplay.objects.filter(
#                 waterplaytypeid = 1
#             )
#         elif self.kwargs["waterplaytypeid"] == 2:
#             return Waterplay.objects.filter(
#                 waterplaytypeid = 2
#             )
#         else:
#             return Waterplay.objects.filter(
#                 waterplaytypeid = 3
#             )


# class WpNameAPIMixins(
#     mixins.RetrieveModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.DestroyModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Waterplay.objects.all()
#     serializer_class = WaterplaySerializer
#     lookup_field = "waterplayname"
    
#     # 물놀이장 1개 정보 출력 
#     # 선택 기준 : 물놀이장 이름 
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ToiletTypesAPIMixins(
#     generics.ListAPIView
# ):
#     serializer_class = ToiletSerializer
#     lookup_field = "toilettype"
    
#     # 종류별 화장실 정보 출력 
#     # 선택 종류 : 수유실, 그 외(공중/간이...등 화장실 )
#     def get_queryset(self):
#         print(self.kwargs["toilettype"])
        
#         if self.kwargs["toilettype"] == "수유실":
#             return Toilet.objects.filter(
#                 toilettype = "수유실"
#             )
#         else:
#             return Toilet.objects.exclude(
#                 toilettype = "수유실"
#             )


# class ToiletIdAPIMixins(
#     mixins.RetrieveModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.DestroyModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Toilet.objects.all()
#     serializer_class = ToiletSerializer
#     lookup_field = "toiletid"
    
#     # 화장실 1개 정보 출력 
#     # 선택 기준 : 화장실 id
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ConvTypesAPIMixins(
#     generics.ListAPIView
# ):
#     serializer_class = ConvSerializer
#     lookup_field = "convtype"
    
#     # 종류별 생활편의시설 정보 출력 
#     # 선택 종류 : 편의점, 그 외(드럭스토어, 다이소)
#     def get_queryset(self):
#         print(self.kwargs["convtype"])
        
#         if self.kwargs["convtype"] == "편의점":
#             return Conv.objects.filter(
#                 convtype = "편의점"
#             )
#         else:
#             return Conv.objects.exclude(
#                 convtype = "편의점"
#             )


# class ConvIdAPIMixins(
#     mixins.RetrieveModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.DestroyModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Conv.objects.all()
#     serializer_class = ConvSerializer
#     lookup_field = "convid"
    
#     # 생활편의시설 1개 정보 출력 
#     # 선택 기준 : 생활편의시설 id
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class MediTypesAPIMixins(
#     generics.ListAPIView
# ):
#     serializer_class = MediSerializer
#     lookup_field = "meditype"
    
#     # 종류별 의료시설 정보 출력 
#     # 선택 종류 : 병원, 약국 
#     def get_queryset(self):
#         print(self.kwargs["meditype"])
        
#         if self.kwargs["meditype"] == "병원":
#             return Medi.objects.filter(
#                 meditype = "병원"
#             )
#         else:
#             return Medi.objects.filter(
#                 meditype = "약국"
#             )


# class MediIdAPIMixins(
#     mixins.RetrieveModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.DestroyModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Medi.objects.all()
#     serializer_class = MediSerializer
#     lookup_field = "mediid"
    
#     # 의료시설 1개 정보 출력 
#     # 선택 기준 : 의료시설 id
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class Safe112AllsAPIMixins(
#     mixins.ListModelMixin, 
#     mixins.CreateModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Safe112.objects.all()
#     serializer_class = Safe112Serializer
    
#     # 모든 경찰서 정보 출력 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class Safe112IdAPIMixins(
#     mixins.RetrieveModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.DestroyModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Safe112.objects.all()
#     serializer_class = Safe112Serializer
#     lookup_field = "safe112id"
    
#     # 경찰서 1개 정보 출력 
#     # 선택 기준 : 경찰서 id
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class Safe119AllsAPIMixins(
#     mixins.ListModelMixin, 
#     mixins.CreateModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Safe119.objects.all()
#     serializer_class = Safe119Serializer
    
#     # 모든 소방서 정보 출력 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class Safe119IdAPIMixins(
#     mixins.RetrieveModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.DestroyModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Safe119.objects.all()
#     serializer_class = Safe119Serializer
#     lookup_field = "safe119id"
    
#     # 소방서 1개 정보 출력 
#     # 선택 기준 : 소방서 id
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ParkingTypesAPIMixins(
#     generics.ListAPIView
# ):
#     serializer_class = ParkingSerializer
#     lookup_field = "parkingtype"
    
#     # 종류별 주차장 정보 출력 
#     # 선택 종류 : 공영, 민영 
#     def get_queryset(self):
#         print(self.kwargs["parkingtype"])
        
#         if self.kwargs["parkingtype"] == "공영":
#             return Parking.objects.filter(
#                 parkingtype = "공영"
#             )
#         else:
#             return Parking.objects.filter(
#                 parkingtype = "민영"
#             )


# class ParkingIdAPIMixins(
#     mixins.RetrieveModelMixin, 
#     mixins.UpdateModelMixin, 
#     mixins.DestroyModelMixin, 
#     generics.GenericAPIView
# ):
#     queryset = Parking.objects.all()
#     serializer_class = ParkingSerializer
#     lookup_field = "parkingid"
    
#     # 주차장 1개 정보 출력 
#     # 선택 기준 : 주차장 id
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# def detail_stat(request, waterplayname):
#     wp = Waterplay.objects.get(waterplayname = waterplayname)
#     wpaddrold = wp.waterplayaddrold
#     wpsigngu = wpaddrold.split()[1]
    
    
#     # wps_score_sum : 같은 행정구역 내 물놀이장의 index list
#     wps = Waterplay.objects.all()
#     wps_score_sum = 0
#     wps_score_num = 0
    
#     # wps_score_sum 계산 
#     for i in range(len(wps)):
#         wpsaddrold = wps[i].waterplayaddrold
#         wpssigngu = wpsaddrold.split()[1]
#         if wpsigngu == wpssigngu:
#             wps_score_sum += wps[i].waterplayscorefaci
#             wps_score_num += 1
    
#     result_dict = {
#         "wp_score" : int(wp.waterplayscorefaci),
#         "wps_score_mean" : int(wps_score_sum / wps_score_num),
#     }
    
#     return JsonResponse(result_dict)


# # 팝업 창에 쓰일 정보만 출력 
# def mappopup(request, waterplayname):
#     wp = Waterplay.objects.get(waterplayname = waterplayname)
    
#     waterplayvalue01 = wp.waterplayvalue01.split("<br>")[0]
    
#     result_dict = {
#         "waterplayname" : wp.waterplayname,
#         "waterplayname01" : wp.waterplayname01,
#         "waterplayvalue01" : waterplayvalue01,
#         "waterplaytelno" : wp.waterplaytelno,
#     }
    
#     return JsonResponse(result_dict)

from rest_framework import mixins, generics
from django.http import JsonResponse

from .models import Waterplay, Toilet, Conv, Medi, Safe112, Safe119, Parking
from .serializers import WaterplaySerializer, ToiletSerializer, ConvSerializer, MediSerializer, Safe112Serializer, Safe119Serializer, ParkingSerializer


class WpAllsAPIMixins(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Waterplay.objects.all()
    serializer_class = WaterplaySerializer
    
    # 모든 물놀이장 정보 출력 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class WpTypeidsAPIMixins(
    generics.ListAPIView
):
    serializer_class = WaterplaySerializer
    lookup_field = "waterplaytypeid"
    
    # 종류별 물놀이장 정보 출력 
    # 선택 종류 : 1(물놀이장), 2((야외)수영장), 3(바닥분수)
    def get_queryset(self):
        print(self.kwargs["waterplaytypeid"])
        
        if self.kwargs["waterplaytypeid"] == 1:
            return Waterplay.objects.filter(
                waterplaytypeid = 1
            )
        elif self.kwargs["waterplaytypeid"] == 2:
            return Waterplay.objects.filter(
                waterplaytypeid = 2
            )
        else:
            return Waterplay.objects.filter(
                waterplaytypeid = 3
            )


class WpNameAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Waterplay.objects.all()
    serializer_class = WaterplaySerializer
    lookup_field = "waterplayname"
    
    # 물놀이장 1개 정보 출력 
    # 선택 기준 : 물놀이장 이름 
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ToiletTypesAPIMixins(
    generics.ListAPIView
):
    serializer_class = ToiletSerializer
    lookup_field = "toilettype"
    
    # 종류별 화장실 정보 출력 
    # 선택 종류 : 수유실, 그 외(공중/간이...등 화장실 )
    def get_queryset(self):
        print(self.kwargs["toilettype"])
        
        if self.kwargs["toilettype"] == "수유실":
            return Toilet.objects.filter(
                toilettype = "수유실"
            )
        else:
            return Toilet.objects.exclude(
                toilettype = "수유실"
            )


class ToiletIdAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Toilet.objects.all()
    serializer_class = ToiletSerializer
    lookup_field = "toiletid"
    
    # 화장실 1개 정보 출력 
    # 선택 기준 : 화장실 id
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ConvTypesAPIMixins(
    generics.ListAPIView
):
    serializer_class = ConvSerializer
    lookup_field = "convtype"
    
    # 종류별 생활편의시설 정보 출력 
    # 선택 종류 : 편의점, 그 외(드럭스토어, 다이소)
    def get_queryset(self):
        print(self.kwargs["convtype"])
        
        if self.kwargs["convtype"] == "편의점":
            return Conv.objects.filter(
                convtype = "편의점"
            )
        else:
            return Conv.objects.exclude(
                convtype = "편의점"
            )


class ConvIdAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Conv.objects.all()
    serializer_class = ConvSerializer
    lookup_field = "convid"
    
    # 생활편의시설 1개 정보 출력 
    # 선택 기준 : 생활편의시설 id
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MediTypesAPIMixins(
    generics.ListAPIView
):
    serializer_class = MediSerializer
    lookup_field = "meditype"
    
    # 종류별 의료시설 정보 출력 
    # 선택 종류 : 병원, 약국 
    def get_queryset(self):
        print(self.kwargs["meditype"])
        
        if self.kwargs["meditype"] == "병원":
            return Medi.objects.filter(
                meditype = "병원"
            )
        else:
            return Medi.objects.filter(
                meditype = "약국"
            )


class MediIdAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Medi.objects.all()
    serializer_class = MediSerializer
    lookup_field = "mediid"
    
    # 의료시설 1개 정보 출력 
    # 선택 기준 : 의료시설 id
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class Safe112AllsAPIMixins(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Safe112.objects.all()
    serializer_class = Safe112Serializer
    
    # 모든 경찰서 정보 출력 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Safe112IdAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Safe112.objects.all()
    serializer_class = Safe112Serializer
    lookup_field = "safe112id"
    
    # 경찰서 1개 정보 출력 
    # 선택 기준 : 경찰서 id
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class Safe119AllsAPIMixins(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Safe119.objects.all()
    serializer_class = Safe119Serializer
    
    # 모든 소방서 정보 출력 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Safe119IdAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Safe119.objects.all()
    serializer_class = Safe119Serializer
    lookup_field = "safe119id"
    
    # 소방서 1개 정보 출력 
    # 선택 기준 : 소방서 id
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ParkingTypesAPIMixins(
    generics.ListAPIView
):
    serializer_class = ParkingSerializer
    lookup_field = "parkingtype"
    
    # 종류별 주차장 정보 출력 
    # 선택 종류 : 공영, 민영 
    def get_queryset(self):
        print(self.kwargs["parkingtype"])
        
        if self.kwargs["parkingtype"] == "공영":
            return Parking.objects.filter(
                parkingtype = "공영"
            )
        else:
            return Parking.objects.filter(
                parkingtype = "민영"
            )


class ParkingIdAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    lookup_field = "parkingid"
    
    # 주차장 1개 정보 출력 
    # 선택 기준 : 주차장 id
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


def detail_stat(request, waterplayname):
    wp = Waterplay.objects.get(waterplayname = waterplayname)
    wpaddrold = wp.waterplayaddrold
    wpsigngu = wpaddrold.split()[1]
    
    
    # wps_score_sum : 같은 행정구역 내 물놀이장의 index list
    wps = Waterplay.objects.all()
    wps_score_sum = 0
    wps_score_num = 0
    
    # wps_score_sum 계산 
    for i in range(len(wps)):
        wpsaddrold = wps[i].waterplayaddrold
        wpssigngu = wpsaddrold.split()[1]
        if wpsigngu == wpssigngu:
            wps_score_sum += wps[i].waterplayscorefaci
            wps_score_num += 1
    
    result_dict = {
        "wp_score" : int(wp.waterplayscorefaci),
        "wps_score_mean" : int(wps_score_sum / wps_score_num),
    }
    
    return JsonResponse(result_dict)


class seoultop10(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Waterplay.objects.all().order_by('-waterplayscorefaci')[:10]
    serializer_class = WaterplaySerializer
    
    # 서울시 편의 점수 TOP10 물놀이장 정보 출력 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# 모든 물놀이장 리뷰 워드클라우드 url 출력 
def seoulwordcloud(request):
    result_dict = {
        "url" : "https://ibb.co/X8PmcZY",
    }
    
    return JsonResponse(result_dict)


# 행정구역별 물놀이장 점수 평균 수평막대그래프 url 출력 
def seoulmeanscoreplt(request):
    result_dict = {
        "url" : "https://ibb.co/nM3K9dY",
    }
    
    return JsonResponse(result_dict)


# 행정구역별 물놀이장 점수 평균 지도 url 출력 
def seoulmeanscorefolium(request):
    result_dict = {
        "url" : "https://ibb.co/SXqfJyy",
    }
    
    return JsonResponse(result_dict)


# 팝업 창에 쓰일 정보만 출력 
def mappopup(request, waterplayname):
    wp = Waterplay.objects.get(waterplayname = waterplayname)
    
    waterplayvalue01 = wp.waterplayvalue01.split("<br>")[0]
    
    result_dict = {
        "waterplayname" : wp.waterplayname,
        "waterplayname01" : wp.waterplayname01,
        "waterplayvalue01" : waterplayvalue01,
        "waterplaytelno" : wp.waterplaytelno,
    }
    
    return JsonResponse(result_dict)
