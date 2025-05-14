from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    info = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_info'  # This matches the table in the database

    def __str__(self):
        return f"{self.name} ({self.email})"
