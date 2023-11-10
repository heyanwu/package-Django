# Generated by Django 2.2.6 on 2023-09-12 03:10

import app_bot.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255, verbose_name='图标')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('introduction', models.TextField(blank=True, null=True, verbose_name='简介')),
                ('created_User', models.CharField(max_length=255, verbose_name='创建人员')),
                ('created_Date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '机器人',
                'verbose_name_plural': '机器人',
            },
        ),
        migrations.CreateModel(
            name='FormInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='表单名')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.Bot', verbose_name='bot引用')),
            ],
            options={
                'verbose_name': '表单',
                'verbose_name_plural': '表单',
            },
        ),
        migrations.CreateModel(
            name='Utterance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[app_bot.models.validate_utter_field], verbose_name='响应名字')),
                ('example', models.TextField(default='', help_text='列表格式', null=True, verbose_name='样例')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.Bot', verbose_name='bot引用')),
            ],
            options={
                'verbose_name': '响应',
                'verbose_name_plural': '响应',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255, verbose_name='图标')),
                ('name', models.CharField(max_length=255, verbose_name='故事名字')),
                ('story_type', models.CharField(max_length=50, verbose_name='类型')),
                ('example', models.TextField(default='', help_text='列表格式', null=True, verbose_name='样例')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.Bot', verbose_name='bot引用')),
            ],
            options={
                'verbose_name': '故事',
                'verbose_name_plural': '故事',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[app_bot.models.validate_english], verbose_name='槽名')),
                ('slot_type', models.TextField(blank=True, default='', help_text='槽类型信息，请填写槽的具体信息', verbose_name='槽类型')),
                ('influence', models.BooleanField(default=True, verbose_name='影响对话')),
                ('mapping', models.TextField(blank=True, default='', help_text='槽映射信息，请填写槽的具体信息', verbose_name='槽映射')),
                ('initial_value', models.CharField(blank=True, max_length=20, null=True, verbose_name='初始值')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.Bot', verbose_name='bot引用')),
            ],
            options={
                'verbose_name': '槽',
                'verbose_name_plural': '槽',
            },
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[app_bot.models.validate_english], verbose_name='意图名字')),
                ('example', models.TextField(default='', help_text='列表格式', null=True, verbose_name='样例')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.Bot', verbose_name='bot引用')),
            ],
            options={
                'verbose_name': '意图',
                'verbose_name_plural': '意图',
            },
        ),
        migrations.CreateModel(
            name='FormSlotInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, default='', help_text='bot回复的提示', verbose_name='询问列表')),
                ('valid_prompts', models.CharField(blank=True, max_length=200, null=True, verbose_name='有效提示')),
                ('invalid_prompts', models.CharField(blank=True, max_length=200, null=True, verbose_name='无效提示')),
                ('forminfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.FormInfo', verbose_name='表单引用')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_bot.Slot', verbose_name='槽')),
            ],
            options={
                'verbose_name': '表单中槽详细信息',
                'verbose_name_plural': '表单中槽详细信息',
            },
        ),
        migrations.AddField(
            model_name='forminfo',
            name='slots',
            field=models.ManyToManyField(to='app_bot.Slot'),
        ),
        migrations.AddConstraint(
            model_name='bot',
            constraint=models.UniqueConstraint(fields=('name', 'created_User'), name='unique_name_per_user'),
        ),
        migrations.AddConstraint(
            model_name='utterance',
            constraint=models.UniqueConstraint(fields=('name', 'bot'), name='unique_name_per_bot'),
        ),
        migrations.AddConstraint(
            model_name='story',
            constraint=models.UniqueConstraint(fields=('name', 'bot'), name='unique_name_per_bot'),
        ),
        migrations.AddConstraint(
            model_name='slot',
            constraint=models.UniqueConstraint(fields=('name', 'bot'), name='unique_name_per_bot'),
        ),
        migrations.AddConstraint(
            model_name='intent',
            constraint=models.UniqueConstraint(fields=('name', 'bot'), name='unique_name_per_bot'),
        ),
        migrations.AddConstraint(
            model_name='forminfo',
            constraint=models.UniqueConstraint(fields=('name', 'bot'), name='unique_name_per_bot'),
        ),
    ]
