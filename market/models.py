from django.db import models

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    info = models.TextField()
    bid = models.CharField(max_length=255)
    img = models.BinaryField()

    class Meta:
        db_table = 'market_userinfo'
        managed = True

    def __str__(self):
        return self.email


