# Generated by Django 4.0.2 on 2022-04-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPannel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_info',
            name='author',
            field=models.CharField(default='NULL', max_length=150),
        ),
    ]