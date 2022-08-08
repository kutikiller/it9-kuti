from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class StudyYear(models.Model):
    class Meta:
        verbose_name = "Учебный Год"
        verbose_name_plural = "Учебный Год"

    date = models.CharField(max_length=250, verbose_name="Год")

    def __str__(self):
        return self.date


class Teacher(models.Model):
    class Meta:
        verbose_name = "Преподователь"
        verbose_name_plural = "Преподователь"

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="Имя")
    surname = models.CharField(max_length=250, verbose_name="Фамилия", blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Фото")
    tel_num = models.CharField(max_length=250, verbose_name="Телефонный номер", blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студент"

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="Имя")
    surname = models.CharField(max_length=250, verbose_name="Фамилия", blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Фото")
    tel_num = models.CharField(max_length=250, verbose_name="Телефонный номер", blank=True, null=True)
    create_data = models.DateField(auto_now=True, verbose_name="Дата регистрации")

    def __str__(self):
        return str(self.user)


class Groups(models.Model):
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группа"

    title = models.CharField(max_length=250, verbose_name="Названия")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподователь")
    study_year = models.ForeignKey(StudyYear, on_delete=models.CASCADE, verbose_name="Учебный Год")

    def __str__(self):
        return self.title


class StudentGroup(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name="Группа")
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.student)
        
    class Meta:
        verbose_name = "Студент группа"
        verbose_name_plural = "Студент группа"
        unique_together = ('student','group')


class DailyMaterial(models.Model):
    class Meta:
        verbose_name = "Ежедневный матерял"
        verbose_name_plural = "Ежедневный матерял"

    tema = models.CharField(max_length=250, verbose_name="Тема")
    text = RichTextField(verbose_name="Текст")
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return self.tema


class Lesson(models.Model):
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Урок"

    daily_material = models.ManyToManyField(DailyMaterial, verbose_name="Ежедневный матерял")
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name="Группа")
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.group)


class HomeWork(models.Model):
    class Meta:
        verbose_name = "Домашняя работа"
        verbose_name_plural = "Домашняя работа"

    tema = models.CharField(max_length=255, blank=True, null=True, verbose_name="Домашняя работа")
    text = RichTextField(verbose_name="Домашняя работа")
    lesson = models.ManyToManyField(Lesson, verbose_name="Урок")
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.tema)


class Comment(models.Model):
    class Meta:
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарии"
        # ordering = ['pub_date']

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    text = RichTextField(verbose_name="Текст")
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.student)


class Attendence(models.Model):
    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемость"

    CHOICES = (
        ('Непришел', '-'),
        ('Пришел', '+')

    )
    studentGroup = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name="Студент группа")
    check_student = models.CharField(max_length=300, choices=CHOICES, verbose_name="Отметка")
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.studentGroup)


class HomeWorkResult(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    home_work = models.ForeignKey(HomeWork, on_delete=models.CASCADE, verbose_name="Д/З")
    create_home_work = RichTextField(verbose_name="Домашняя работа")
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.student)
    class Meta:
        verbose_name = "Домашняя работа студента"
        verbose_name_plural = "Домашняя работа студента"
        unique_together = ('student','home_work')


class HomeWorkEvaluation(models.Model):
    class Meta:
        verbose_name = "Оценка домашнего задания"
        verbose_name_plural = "Оценка домашнего задания"

    student = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, verbose_name="Студент")
    home_work = models.ForeignKey(HomeWork, on_delete=models.CASCADE, verbose_name="Д/З")
    ball = models.PositiveIntegerField(verbose_name="Бал 10", blank=True, null=True)
    create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.student)


# class Dayball(models.Model):
#     class Meta:
#         verbose_name = "Оценка группы"
#         verbose_name_plural = "Оценка группы"

#     group = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name="Группа")
#     ball = models.PositiveIntegerField(verbose_name="Бал", blank=True, null=True)
#     create_data = models.DateField(auto_now=True, verbose_name="Дата создания")

#     def __str__(self):
#         return str(self.group)