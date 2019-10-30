# Generated by Django 2.2.6 on 2019-10-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('post', models.CharField(max_length=1024)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
