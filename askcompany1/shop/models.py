from django.db import models
from django.urls import reverse

from .utils import uuid_upload_to


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)

    def __str__(self):
        return self.name  # 데이터베이스에 바로 보이게
        # return f'<{self.pk}> {self.name}'

    class Meta:
        ordering = ['id']  # 쿼리셋에 order_by지정안해도 자동 지정
        # 이 코드 삭제시 쿼리셋에서 order_by로 호출

    def get_absolute_url(self):  # item_detail로 url보내기
        return reverse('shop:item_detail', args=[self.pk])
        # return reverse('shop:item_detail', kwargs={'pk' : self.pk})
