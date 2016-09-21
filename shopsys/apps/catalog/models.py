# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField("名称", max_length=50)
    slug = models.CharField(unique=True, max_length=50, help_text='根据name生成的，用于URL,必须唯一')
    description = models.TextField("描述")
    is_active = models.BooleanField("是否激活", default=True)
    meta_keywords = models.CharField("Meta 关键字", max_length=255, help_text="meta关键字，有利于SEO,用逗号分隔")
    meta_description = models.CharField("Meta 描述", max_length=255, help_text="meta　描述")
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        managed = False
        ordering = ['-created_at']
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_category', args=(self.slug,))


class Product(models.Model):
    name = models.CharField("名称", unique=True, max_length=255)
    slug = models.CharField("Slug", unique=True, max_length=255)
    brand = models.CharField("品牌", max_length=50)
    sku = models.CharField("计量单位", max_length=50)
    price = models.DecimalField("价格", max_digits=9, decimal_places=2)
    old_price = models.DecimalField("旧价格", max_digits=9, decimal_places=2)
    image = models.CharField('图片', max_length=50)
    is_active = models.BooleanField("设为激活", default=True)
    is_bestseller = models.BooleanField("设为畅销", default=False)
    is_featured = models.BooleanField("设为推荐", default=False)
    quantity = models.IntegerField("数量")
    description = models.TextField("描述")
    meta_keywords = models.CharField("meta　描述标签", max_length=255)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    categories = models.ManyToManyField('Category')

    class Meta:
        managed = False
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args=(self.slug,))

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
