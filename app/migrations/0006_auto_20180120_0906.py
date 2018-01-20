# Generated by Django 2.0.1 on 2018-01-20 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180119_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='information',
            name='society',
        ),
        migrations.RenameField(
            model_name='society',
            old_name='name',
            new_name='building_name',
        ),
        migrations.RemoveField(
            model_name='society',
            name='locality',
        ),
        migrations.AddField(
            model_name='society',
            name='Locality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Locality'),
        ),
        migrations.AddField(
            model_name='society',
            name='option',
            field=models.CharField(choices=[('buy', 'Buy'), ('rent', 'Rent')], default='buy', max_length=9),
        ),
        migrations.AddField(
            model_name='society',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='society',
            name='sq_ft',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Information',
        ),
        migrations.AddField(
            model_name='society',
            name='property_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PropertyType'),
        ),
    ]
