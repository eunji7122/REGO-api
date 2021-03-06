# Generated by Django 2.2.4 on 2019-11-07 06:49

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('user', '0003_auto_20190815_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='auth_number',
            field=models.IntegerField(default=0, verbose_name='인증 번호'),
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=11, verbose_name='휴대폰 번호'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
