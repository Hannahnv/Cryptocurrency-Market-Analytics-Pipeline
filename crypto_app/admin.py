from django.contrib import admin

# Register your models here.
from .models import Coin, HistoricalData, GithubInfo, ProgrammingLanguage

# Đăng ký các model với trang admin
admin.site.register(Coin)
admin.site.register(HistoricalData)
admin.site.register(GithubInfo)
admin.site.register(ProgrammingLanguage)