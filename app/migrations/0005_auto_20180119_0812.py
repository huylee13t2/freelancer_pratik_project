# Generated by Django 2.0.1 on 2018-01-19 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180119_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.AlterField(
            model_name='locality',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.City'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
