# Generated by Django 4.1.5 on 2023-01-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]