from django.db import models


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(Timestamp):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True, max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return '[{2}] {0} - {1}'.format(
            self.title,
            self.description,
            self.is_done
            )

