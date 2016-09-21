# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='名称', max_length=50)),
                ('slug', models.CharField(help_text='根据name生成的，用于URL,必须唯一', max_length=50, unique=True)),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.IntegerField(verbose_name='是否激活', default=True)),
                ('meta_keywords', models.CharField(help_text='meta关键字，有利于SEO,用逗号分隔', verbose_name='Meta 关键字', max_length=255)),
                ('meta_description', models.CharField(help_text='meta\u3000描述', verbose_name='Meta 描述', max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='名称', max_length=255, unique=True)),
                ('slug', models.CharField(verbose_name='Slug', max_length=255, unique=True)),
                ('brand', models.CharField(verbose_name='品牌', max_length=50)),
                ('sku', models.CharField(verbose_name='计量单位', max_length=50)),
                ('price', models.DecimalField(verbose_name='价格', max_digits=9, decimal_places=2)),
                ('old_price', models.DecimalField(verbose_name='旧价格', max_digits=9, decimal_places=2)),
                ('image', models.CharField(verbose_name='图片', max_length=50)),
                ('is_active', models.IntegerField(verbose_name='设为激活', default=True)),
                ('is_bestseller', models.IntegerField(verbose_name='设为畅销', default=False)),
                ('is_featured', models.IntegerField(verbose_name='设为推荐', default=False)),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述')),
                ('meta_keywords', models.CharField(verbose_name='meta\u3000描述标签', max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
                'ordering': ['-created_at'],
            },
        ),
    ]
