# Generated by Django 2.2.12 on 2020-05-30 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20200530_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testtt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testt', models.BinaryField()),
            ],
        ),
        migrations.AddField(
            model_name='customtext',
            name='emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_emp', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customtext',
            name='name',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='subpage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_subpage', to='home.CustomText'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_test', to=settings.AUTH_USER_MODEL),
        ),
    ]