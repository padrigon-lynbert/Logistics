from django.db import models

# Create your models here.

class Audit(models.Model):
    """Record for audit transaction."""
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
    class Status(models.TextChoices):
        PLANNED = 'PLN', 'Planned'
        IN_PROGRESS = 'INP', 'In Progress'
        COMPLETED = 'CMP', 'Completed'
    
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.PLANNED)
    scheduled_date = models.DateField()
    created_by = models.IntegerField() # This is supposed to be a foreign key, subjected for changes.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns audit title."""
        return self.title

class Scheduling(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    audit_id = models.ForeignKey(Audit, on_delete=models.CASCADE)
    schedule_start = models.DateField()
    schedule_end = models.DateField()
    location = models.CharField(max_length=255)
    time_zone = models.CharField(max_length=50)
    
    # Status types for schedule
    class Status(models.TextChoices):
        SCHEDULED = 'SCHED', 'Scheduled'
        RESCHED = 'RESCH', 'Rescheduled'
        CANCELLED = 'CNCLD', 'Cancelled'
        COMPLETED = 'CMPLT', 'Completed'

    status = models.CharField(max_length=5,
                              choices=Status.choices,
                              default=Status.SCHEDULED)
    notes = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        """Returns schedule start."""
        return self.schedule_start
    
class Logistics(models.Model):
    """Defines entity details."""
    entity_id = models.AutoField(primary_key=True)

    class Entity_Type(models.TextChoices):
        WAREHOUSE = 'WAR', 'Warehousing'
        VEHICLE = 'VEH', 'Vehicle'
        SUPPLIER = 'SUP', 'Supplier'
    # Choices for entity type.
    entity_type = models.CharField(max_length=3,
                                   choices=Entity_Type.choices)
    
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        """Display name of logistic data."""
        return self.name