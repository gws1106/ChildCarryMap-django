# 로컬
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 엔진
        "NAME": "childcarrymap",  # 데이터베이스 이름
        "USER": "root",  # 사용자
        "PASSWORD": "Pa55w.rd1234",  # 비밀번호
        "HOST": "localhost",  # 호스트
        "PORT": "3306",  # 포트번호
    }
}
SECRET_KEY = 'django-insecure-3cj!a+t*htma7m7f6xc!u^xou-&)hx7d3)c-8#-uwyj&#p)_ob'

#클라우드
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",  # 엔진
#         "NAME": "childcarrymap",  # 데이터베이스 이름
#         "USER": "admin",  # 사용자
#         "PASSWORD": "Pa55w.rd1234",  # 비밀번호
#         "HOST": "demo-db-1.cyf8tnql7evk.us-east-2.rds.amazonaws.com",  # 호스트
#         "PORT": "3306",  # 포트번호
#     }
# }

# SECRET_KEY = 'django-insecure-3cj!a+t*htma7m7f6xc!u^xou-&)hx7d3)c-8#-uwyj&#p)_ob'
