from django.db import models

# Create your models here.

class TodoModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_complete = models.BooleanField(null=True, blank=True)
    parent = models.ForeignKey(
        'TodoModel',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "todo"

    def __str__(self):
        return "{} - (Is Complete: {}) [{}]".format(self.name, self.is_complete, self.id)