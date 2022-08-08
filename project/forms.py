from django.contrib.auth.models import User
from django import forms
from project.models import *
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password',]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["surname","image","tel_num"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update'))

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["surname","image","tel_num"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update'))

class HomeWorkResultkForm(forms.ModelForm):
    class Meta:
        model = HomeWorkResult
        # exclude = ['home_work']
        fields = ["create_home_work",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create'))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text",]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create'))

class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ["title","study_year"]

class StudyYearForm(forms.ModelForm):
    class Meta:
        model = StudyYear
        fields = ["date"]

class StudentGroupForm(forms.ModelForm):
    class Meta:
        model = StudentGroup
        fields = ["student"]

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["daily_material"]
        
class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ["tema","text","lesson"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create'))