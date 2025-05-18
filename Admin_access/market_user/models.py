from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    info = models.TextField()
    bid = models.CharField(max_length=255)
    img = models.URLField()

    class Meta:
        db_table = 'user_info'
        managed = False

    def __str__(self):
        return self.email


