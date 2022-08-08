from django.contrib import admin
from project.models import *

admin.site.register(StudyYear)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Groups)
admin.site.register(StudentGroup)
admin.site.register(Lesson)
admin.site.register(HomeWork)
admin.site.register(Attendence)
admin.site.register(HomeWorkResult)
admin.site.register(DailyMaterial)
admin.site.register(Comment)
admin.site.register(HomeWorkEvaluation)
# admin.site.register(Dayball)
# django-admin-tools collectstatic