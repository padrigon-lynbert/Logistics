from django.db import models

# Create your models here.

class Audit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    organization_id = models.IntegerField()
    title = models.CharField(max_length=256)

    # Choices for audit types.
    class Audit_Types(models.TextChoices):
        INTERNAL = 'INT', 'Internal'
        EXTERNAL = 'EXT', 'External'
        COMPLIANCE = 'COM', 'Compliance'

    audit_type = models.CharField(max_length=3,
                                  choices=Audit_Types.choices, 
                                  default=Audit_Types.INTERNAL)
    
    # Choices for status types.
    class Status(models.Choices):
        PLANNED = 'PLN', 'Planned'
        IN_PROGRESS = 'INP', 'In Progress'
        COMPLETED = 'CMP', 'Completed'
    
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.PLANNED)
    scheduled_date = models.DateField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)