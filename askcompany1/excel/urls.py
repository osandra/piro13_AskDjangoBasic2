from django.urls import path

from excel import views

urlpatterns =[
    path('',views.excel_file),
    path('06/test_404/',views.test),
]