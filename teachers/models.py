from django.db import models


# from .validators import validate_phone


class Teachers(models.Model):
    class TeacherManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=True)

    science = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    objects = models.Manager()
    teacher_manager = TeacherManager()

    def __str__(self):
        return self.science


class Students(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.ForeignKey('Teachers', on_delete=models.PROTECT, verbose_name="sciense")
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.teachers
