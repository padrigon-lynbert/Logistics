from django.db import models

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    info = models.TextField()
    bid = models.CharField(max_length=255)
    img = models.BinaryField(null=True, blank=True)
    # activation_status = models.CharField(default='pending')

    class Meta:
        db_table = 'market_userinfo'
        managed = True

    def __str__(self):
        return self.email
    
    
class Vendor_history(models.Model):
    id = models.AutoField(primary_key=True)
    vendor_id = models.IntegerField() 
    event_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'l2_vendor_history'
        managed = True

    def __str__(self):
        return f"{self.vendor_id} - {self.event_type} @ {self.created_at}"


