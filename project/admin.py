from django.contrib import admin
from project.models import *
from django.utils.html import mark_safe

class StudentGroupextra(admin.StackedInline):
    model = StudentGroup
    extra = 1

class Lessonextra(admin.StackedInline):
    model = Lesson
    extra = 1

class HomeWorkResultextra(admin.StackedInline):
    model = HomeWorkResult
    extra = 1
    
class Attendenceextra(admin.StackedInline):
    model = Attendence
    extra = 1
    readonly_fields = ['create_data']
       
class HomeWorkEvaluationextra(admin.StackedInline):
    model = HomeWorkEvaluation
    extra = 1



class StudyYearAdmin(admin.ModelAdmin):
    list_display = ["date"]
admin.site.register(StudyYear,StudyYearAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_filter=('user','surname','tel_num')
    list_display = ['user','surname','image_tag','tel_num']
    list_per_page = 5
    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100"/>')
        image_tag.short_description = 'Image'
admin.site.register(Teacher,TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_filter=('user','surname','tel_num','create_data')
    list_display = ['user','surname','image_tag','tel_num','create_data']
    list_per_page = 5
    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100"/>')
        image_tag.short_description = 'Image'
admin.site.register(Student,StudentAdmin)

class GroupsAdmin(admin.ModelAdmin):
    inlines = [StudentGroupextra,Lessonextra]
    list_display = ["title", "teacher", "study_year"]
    list_filter=("title", "teacher", "study_year",)
    list_display_links=("title",)
    save_on_top=True
    list_per_page = 5
admin.site.register(Groups,GroupsAdmin)

class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ['student','group','create_data']
    inlines = [Attendenceextra]
admin.site.register(StudentGroup,StudentGroupAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_filter=('daily_material', 'group','create_data')
    fields = ['daily_material', 'group',]
    list_display = ['group','create_data']
    filter_horizontal=["daily_material"]
    list_per_page = 5
    search_fields = ['group']

    def get_daily_material(self):
        return "\n".join([p.daily_materials for p in self.daily_material.all()])

admin.site.register(Lesson,LessonAdmin)

class HomeWorkAdmin(admin.ModelAdmin):
    list_filter=('tema','text','create_data')
    fields = ['tema','text',"lesson"]
    list_display = ['tema','create_data']
    filter_horizontal=["lesson"]
    inlines = [HomeWorkResultextra]
    list_per_page = 5
    # def text_tag(self, obj):
    #     return mark_safe(f'{text|safe}')
    #     text_tag.short_description = 'Text'
admin.site.register(HomeWork,HomeWorkAdmin)

# class AttendenceAdmin(admin.ModelAdmin):
#     list_display = []
# admin.site.register(Attendence)

class HomeWorkResultAdmin(admin.ModelAdmin):
    fields = ['student','home_work','create_home_work']
    list_display = ['student','home_work','create_data']
    readonly_fields = ['student','home_work','text_tag']
    inlines = [HomeWorkEvaluationextra]
    def text_tag(self, obj):
        return '{{create_home_work|safe}}'
admin.site.register(HomeWorkResult,HomeWorkResultAdmin)

class DailyMaterialAdmin(admin.ModelAdmin):
    list_display = ['tema','create_data']
admin.site.register(DailyMaterial,DailyMaterialAdmin)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = []
# admin.site.register(Comment,CommentAdmin)

class HomeWorkEvaluationAdmin(admin.ModelAdmin):
    list_display = []
admin.site.register(HomeWorkEvaluation)
# admin.site.register(Dayball)
# django-admin-tools collectstatic