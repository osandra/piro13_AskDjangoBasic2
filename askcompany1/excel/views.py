import os
from urllib.parse import quote
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
#엑셀파일 다운로드 응답. 즉 해당 url에 들어가면 파일이 자동 다운로드 됨
def excel_file(request):
    filepath = 'C:/Users/User/Desktop/mara.xls'
    filename = os.path.basename(filepath)

    with open(filepath,'rb') as f:
        response = HttpResponse(f,content_type='application/vnd.ms-excel')
    #파일을 저장한 이름 그래도 다운받도록. 아래 두 줄 코드 사용안하면 다운로드라는 이름으로 다운받게 됨
    encoded_filename = quote(filename)
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)
    return response

def test(request):
    item = get_object_or_404(Itme, pk=pk)