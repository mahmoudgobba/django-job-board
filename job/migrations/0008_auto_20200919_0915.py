# Generated by Django 3.0.3 on 2020-09-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_remove_categories_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ManyToManyField(null=True, related_name='jobs', to='job.Categories'),
        ),
    ]
