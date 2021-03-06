# Generated by Django 3.2.4 on 2021-06-27 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0007_rename_user1_pokemonslist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonslist',
            name='author',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='pokemonslist',
            name='user',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
