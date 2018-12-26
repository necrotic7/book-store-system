from django.db import models


class Author(models.Model):
    name = models.CharField('名字',max_length = 20)
    email = models.EmailField('電子郵件', unique = True)

    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField('出版社名稱', max_length = 50, unique = True)
    address = models.CharField('地址', max_length = 225)

    def __str__(self):
        return self.name


class Classification(models.Model):
    name = models.CharField('分類名稱', max_length = 50, unique = True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('標籤名稱', max_length = 50, unique = True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField('書名',max_length = 50)
    price = models.PositiveIntegerField('價格')
    author = models.ManyToManyField(Author, verbose_name = '作者')
    publish = models.ForeignKey(Publish, models.PROTECT, verbose_name = '出版社')
    classification = models.ForeignKey(Classification, models.PROTECT, verbose_name = '分類')
    tags = models.ManyToManyField(Tag, verbose_name = '標籤')
    introduction = models.TextField('簡介')

    def __str__(self):
        return self.name    