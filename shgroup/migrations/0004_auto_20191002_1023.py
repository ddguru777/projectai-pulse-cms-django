# Generated by Django 2.2.5 on 2019-10-02 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shgroup', '0003_shmapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shmapping',
            name='subjectUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subjectUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shmapping',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
