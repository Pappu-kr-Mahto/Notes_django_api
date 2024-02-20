# Generated by Django 4.2.10 on 2024-02-19 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=1000)),
                ('shared', models.BooleanField(default=False)),
                ('versions', models.TextField(default=[])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
