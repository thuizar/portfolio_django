from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(verbose_name='Project Image', blank=True, null = True, upload_to='Projects')
    link = models.URLField(verbose_name='Project URL')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created']

    def __str__(self):
	    return self.title