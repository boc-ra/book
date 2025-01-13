from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth import get_user_model

class Bookdiary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    writer = models.CharField(verbose_name='作者', max_length=40)
    text = models.CharField(verbose_name='本文', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='ユーザー')

