from django.db import models


# Create your models here.
class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent=None)


class Category(models.Model):
    objects = models.Manager()
    tops = CategoryManager()

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('web.Category', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_children(self):
        return self.category_set.all()

    def get_parents(self):
        b = self
        a = []
        while b.parent is not None:
            b = b.parent
            a.append(b)
        return a

    @property
    def get_full_url(self):
        url = '/'
        for i in reversed(self.get_parents()):
            url += i.url + '/'
        url += self.url
        return url
