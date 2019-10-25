from django.db import models
from pytils.translit import slugify
from django.utils import timezone

from time import time


def gen_slug(s):
    new_slug = slugify(s)
    # time_slug = str(int(time()))
    # return new_slug + '-' + time_slug
    return new_slug


class Item(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    img = models.ImageField(upload_to='items_img', blank=False)
    tag = models.ManyToManyField('Tag', related_name='items')
    body = models.TextField(db_index=True)
    pub_date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:  # сохранение сгенерированного slug
            self.slug = gen_slug(self.title)
        return super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:  # сохранение сгенерированного slug
            self.slug = gen_slug(self.title)
        return super().save(*args, **kwargs)

