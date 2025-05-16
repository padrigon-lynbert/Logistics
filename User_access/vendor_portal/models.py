from django.db import models

class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    info = models.CharField(max_length=300)
    password = models.CharField(max_length=255)
    bid = models.CharField(max_length=255)
    img = models.BinaryField()

    class Meta:
        db_table = 'market_userinfo'

    def __str__(self):
        return f"{self.name} ({self.email})"
