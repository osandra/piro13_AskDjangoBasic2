from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Item


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')  # 값이 없으면 빈 문자열을 갖는다
    if q:  # 빈문자열이면 false
        qs = qs.filter(name__icontains=q)  # icontains는 대소문자 구분X

    return render(request, 'shop/item_list.html',
                  {'item_list': qs,
                   'q': q
                   })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })
