from django.db import models
from django.urls import reverse


class Tag(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'tag': self.slug})


class Writeup(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    description = models.CharField(max_length=500, blank=True)
    body = models.TextField()
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='writeups')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('writeup_detail', kwargs={'slug': self.slug})

    @property
    def primary_tag(self):
        tags = sorted(self.tags.all(), key=lambda t: t.slug)
        if not tags:
            return ''
        specific = [t for t in tags if t.slug != 'project']
        return (specific[0] if specific else tags[0]).slug

    @property
    def reading_time(self):
        return max(1, round(len(self.body.split()) / 200))
