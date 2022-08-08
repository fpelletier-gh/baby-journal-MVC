from django.db import models
from django.contrib.auth.models import User


class Baby(models.Model):
    """A baby for the baby log"""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    """Something specific learned about a baby."""

    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # date_added = models.DateTimeField(auto_now_add=True)
    date_of_event = models.DateTimeField()

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) <= 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
