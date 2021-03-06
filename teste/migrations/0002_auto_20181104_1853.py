# Generated by Django 2.0 on 2018-11-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruta',
            fields=[
                ('nome', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='segundo_nome',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tam_roupa',
            field=models.CharField(choices=[('P', 'PEQUENA'), ('M', 'MEDIA'), ('G', 'GRANDE')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='primeiro_nome',
            field=models.CharField(max_length=60),
        ),
    ]
