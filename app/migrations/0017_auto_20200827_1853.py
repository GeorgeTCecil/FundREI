# Generated by Django 2.2.4 on 2020-08-28 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200827_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='app.User'),
        ),
    ]
