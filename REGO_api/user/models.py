from django.contrib.auth.models import AbstractUser
import requests
from random import randint
from django.db import models
from model_utils.models import TimeStampedModel
import datetime
from django.utils import timezone


class User(AbstractUser, TimeStampedModel):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, unique=True)
    phone = models.CharField(verbose_name='휴대폰 번호', blank=True, help_text='Contact phone number', max_length=11)
    auth_number = models.IntegerField(verbose_name='인증 번호', default=0)
    private_key = models.CharField(max_length=100, default=0)
    address = models.CharField(max_length=100, default=0)

    class Meta:
        db_table = 'User'

    def save(self, *args, **kwargs):
        self.auth_number = randint(1000, 10000)
        super().save(*args, **kwargs)
        self.send_sms()  # 인증번호가 담긴 SMS를 전송

    def send_sms(self):
        url = 'https://api-sens.ncloud.com/v1/sms/services/ncp:sms:kr:257319716069:sms_service/messages/'

        data = {
            "type": "SMS",
            "from": "01043167122",
            "to": [self.phone],
            "content": "[테스트] 인증 번호 [{}]를 입력해주세요.".format(self.auth_number)
        }
        headers = {
            "Content-Type": "application/json",
            "x-ncp-auth-key": "yC7JhEfOLrBH8fFSCbjQ",
            "x-ncp-service-secret": "352539b52d56417798981d128dd3d8ed",
        }
        requests.post(url, json=data, headers=headers)

    @classmethod
    def check_auth_number(cls, p_num, c_num):
        time_limit = timezone.now() - datetime.timedelta(minutes=5)

        result = cls.objects.filter(
            phone=p_num,
            auth_number=c_num,
            modified__gte=time_limit
        )
        if result:
            return True
        return False
