# Generated by Django 2.2 on 2021-06-04 16:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0007_auto_20210603_1526'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('blogpost', models.ManyToManyField(to='blog.BlogPost')),
                ('user', models.ForeignKey(on_delete='auth.User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]