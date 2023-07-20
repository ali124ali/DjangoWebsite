from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null= False, blank=False)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name