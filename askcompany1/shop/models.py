from django.utils import timezone

from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name #데이터베이스에 바로 보이게
        #return f'<{self.pk}> {self.name}'

    class Meta:
        ordering = ['id'] #쿼리셋에 order_by지정안해도 자동 지정
        #이 코드 삭제시 쿼리셋에서 order_by로 호출
