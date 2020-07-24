from django.urls import path

from excel import views

urlpatterns =[
    path('',views.excel_file),
    path('24',views.tag),
]