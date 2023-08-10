# from django.urls import path
# from . import views

# app_name = 'map'


# urlpatterns = [
#     ### url 구성 ###
#     # 테이블 이름 / 선택 기준 / 복수형이면 s
    
#     ### 기본 정보 출력 ###
#     # 모든 물놀이장 정보 출력 
#     path('wpalls/', views.WpAllsAPIMixins.as_view()),

#     # 종류별 물놀이장 정보 출력 
#     # 선택 종류 : 1(물놀이장), 2((야외)수영장), 3(바닥분수)
#     path('wptypeids/<int:waterplaytypeid>/', views.WpTypeidsAPIMixins.as_view()),

#     # 물놀이장 1개 정보 출력 
#     # 선택 기준 : 물놀이장 이름 
#     path('wpname/<str:waterplayname>/', views.WpNameAPIMixins.as_view()),
    
#     # 종류별 화장실 정보 출력 
#     # 선택 종류 : 수유실, 그 외(공중/간이...등 화장실 )
#     path('toilettypes/<str:toilettype>/', views.ToiletTypesAPIMixins.as_view()),

#     # 화장실 1개 정보 출력 
#     # 선택 기준 : 화장실 id
#     path('toiletid/<str:toiletid>/', views.ToiletIdAPIMixins.as_view()),

    
#     # 종류별 생활편의시설 정보 출력 
#     # 선택 종류 : 편의점, 그 외(드럭스토어, 다이소)
#     path('convtypes/<str:convtype>/', views.ConvTypesAPIMixins.as_view()),

#     # 생활편의시설 1개 정보 출력 
#     # 선택 기준 : 생활편의시설 id
#     path('convid/<str:convid>/', views.ConvIdAPIMixins.as_view()),

    
#     # 종류별 의료시설 정보 출력 
#     # 선택 종류 : 병원, 약국 
#     path('meditypes/<str:meditype>/', views.MediTypesAPIMixins.as_view()),

#     #  1개 정보 출력 
#     # 선택 기준 :  id
#     path('mediid/<str:mediid>/', views.MediIdAPIMixins.as_view()),

    
#     # 모든 경찰서 정보 출력 
#     path('safe112alls/', views.Safe112AllsAPIMixins.as_view()),

#     # 경찰서 1개 정보 출력 
#     # 선택 기준 : 경찰서 id
#     path('safe112id/<str:safe112id>/', views.Safe112IdAPIMixins.as_view()),

    
#     # 모든 소방서 정보 출력 
#     path('safe119alls/', views.Safe119AllsAPIMixins.as_view()),

#     # 소방서 1개 정보 출력 
#     # 선택 기준 : 소방서 id
#     path('safe119id/<str:safe119id>/', views.Safe119IdAPIMixins.as_view()),

    
#     # 종류별 주차장 정보 출력 
#     # 선택 종류 : 공영, 민영  
#     path('parkingtypes/<str:parkingtype>/', views.ParkingTypesAPIMixins.as_view()),
    
#     # 주차장 1개 정보 출력 
#     # 선택 기준 : 주차장 id
#     path('parkingid/<str:parkingid>/', views.ParkingIdAPIMixins.as_view()),
#     #####################
    
    
#     ### 통계 정보 출력 ###
#     # 상세 페이지 - 제공 서비스
#     # 5. 해당 물놀이 시설과 행정구역 내 물놀이장의 점수 평균과 비교
#     # path('detailstat/<str:waterplayname>/', views.DetailStatMixins.as_view()),
#     path('detailstat/<str:waterplayname>/', views.detail_stat, name='detail_stat'),
#     #####################
#     path('mappopup/<str:waterplayname>/', views.mappopup),
# ]

from django.urls import path
from . import views

app_name = 'map'


urlpatterns = [
    ### url 구성 ###
    # 테이블 이름 / 선택 기준 / 복수형이면 s
    
    ### 기본 정보 출력 ###
    # 모든 물놀이장 정보 출력 
    path('wpalls/', views.WpAllsAPIMixins.as_view()),
    # 종류별 물놀이장 정보 출력 
    # 선택 종류 : 1(물놀이장), 2((야외)수영장), 3(바닥분수)
    path('wptypeids/<int:waterplaytypeid>/', views.WpTypeidsAPIMixins.as_view()),
    # 물놀이장 1개 정보 출력 
    # 선택 기준 : 물놀이장 이름 
    path('wpname/<str:waterplayname>/', views.WpNameAPIMixins.as_view()),
    
    # 종류별 화장실 정보 출력 
    # 선택 종류 : 수유실, 그 외(공중/간이...등 화장실 )
    path('toilettypes/<str:toilettype>/', views.ToiletTypesAPIMixins.as_view()),
    # 화장실 1개 정보 출력 
    # 선택 기준 : 화장실 id
    path('toiletid/<str:toiletid>/', views.ToiletIdAPIMixins.as_view()),
    
    # 종류별 생활편의시설 정보 출력 
    # 선택 종류 : 편의점, 그 외(드럭스토어, 다이소)
    path('convtypes/<str:convtype>/', views.ConvTypesAPIMixins.as_view()),
    # 생활편의시설 1개 정보 출력 
    # 선택 기준 : 생활편의시설 id
    path('convid/<str:convid>/', views.ConvIdAPIMixins.as_view()),
    
    # 종류별 의료시설 정보 출력 
    # 선택 종류 : 병원, 약국 
    path('meditypes/<str:meditype>/', views.MediTypesAPIMixins.as_view()),
    #  1개 정보 출력 
    # 선택 기준 :  id
    path('mediid/<str:mediid>/', views.MediIdAPIMixins.as_view()),
    
    # 모든 경찰서 정보 출력 
    path('safe112alls/', views.Safe112AllsAPIMixins.as_view()),
    # 경찰서 1개 정보 출력 
    # 선택 기준 : 경찰서 id
    path('safe112id/<str:safe112id>/', views.Safe112IdAPIMixins.as_view()),
    
    # 모든 소방서 정보 출력 
    path('safe119alls/', views.Safe119AllsAPIMixins.as_view()),
    # 소방서 1개 정보 출력 
    # 선택 기준 : 소방서 id
    path('safe119id/<str:safe119id>/', views.Safe119IdAPIMixins.as_view()),
    
    # 종류별 주차장 정보 출력 
    # 선택 종류 : 공영, 민영  
    path('parkingtypes/<str:parkingtype>/', views.ParkingTypesAPIMixins.as_view()),
    # 주차장 1개 정보 출력 
    # 선택 기준 : 주차장 id
    path('parkingid/<str:parkingid>/', views.ParkingIdAPIMixins.as_view()),
    #####################
    
    
    ### 통계 정보 출력 ###
    # 상세 페이지 - 제공 서비스
    # 5. 해당 물놀이 시설과 행정구역 내 물놀이장의 점수 평균과 비교
    path('detailstat/<str:waterplayname>/', views.detail_stat),
    #####################
    
    ### 통계 한눈에 보기 ###
    # 서울시 편의 점수 TOP10 물놀이장 정보 출력 
    path('seoultop10/', views.seoultop10.as_view()),
    
    # 모든 물놀이장 리뷰 워드클라우드 url 출력 
    path('seoulwordcloud/', views.seoulwordcloud),
    
    # 행정구역별 물놀이장 점수 평균 수평막대그래프 url 출력 
    path('seoulmeanscoreplt/', views.seoulmeanscoreplt),
    
    # 행정구역별 물놀이장 점수 평균 지도 url 출력 
    path('seoulmeanscorefolium/', views.seoulmeanscorefolium),
    #####################
    
    
    ### 팝업 창에 쓰일 정보만 출력 ###
    path('mappopup/<str:waterplayname>/', views.mappopup),
    #####################
]
