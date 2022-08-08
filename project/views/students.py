from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from project.decorators import allowed_users
from project.models import Student, StudentGroup, Groups, Lesson, HomeWork, Comment, HomeWorkEvaluation,HomeWorkResult
from project.forms import StudentForm, HomeWorkResultkForm, CommentForm
from django.contrib import messages
from django.http import HttpResponse
from django.conf.urls import handler404, handler500


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentPage(request):
    user = request.user
    student = Student.objects.get(user=user)
    student_groups = StudentGroup.objects.filter(student=student).select_related("group")
    context = {
        'student': student,
        'student_groups': student_groups
     }
    return render(request, 'student/student_page.html', context)

def studentBall(request,id):
    user = request.user
    student = Student.objects.get(user=user)
    ball = HomeWorkEvaluation.objects.filter(student=id)
    context = {
        "ball":ball,
        "student":student,
    }
    return render(request, 'student/ball/student_ball.html', context)


def detailGroup(request,id):
    user = request.user
    student = Student.objects.get(user=user)
    group = Groups.objects.get(id=id)
    lesson = Lesson.objects.filter(group=id)
    students = StudentGroup.objects.filter(group=id)
    context = {
        'group':group,
        'lesson':lesson,
        'students':students,
        'student': student,
    }
    return render(request, 'student/detail/detail_group.html', context)

def detailLesson(request,id):
    user = request.user
    student = Student.objects.get(user=user)
    lesson = Lesson.objects.get(id=id)
    home_work = HomeWork.objects.filter(lesson=lesson)
    # home_work = HomeWorkResult.objects.filter(home_work=home_work)
    home_work_student = HomeWorkResult.objects.filter(student=student,).select_related('home_work')
    comment = Comment.objects.filter(lesson=lesson)
    context = {
        'lesson':lesson,
        'home_work':home_work,
        'comment':comment,
        'student': student,
        'home_work_student':home_work_student,
    }
    return render(request, 'student/detail/detail_lesson.html', context)
    

def createHomeWorkStudent(request,id_home_work,id_lesson):
    user = request.user
    student = Student.objects.get(user=user)
    lesson = Lesson.objects.get(id=id_lesson)
    if request.method == 'POST':
        form = HomeWorkResultkForm(request.POST)
        if form.is_valid():
            create_home_work = form.save(commit=False)
            create_home_work.student = student
            create_home_work.home_work_id = id_home_work
            create_home_work.save()

            # messages.success(request, 'you create')
            return redirect('detail_lesson',id_lesson)
        else:
            return render(request, 'general/500.html',)
    else:
        form = HomeWorkResultkForm()
    context = {
        "form":form,
        'student': student,
        'lesson':lesson,
    }
    return render(request, 'student/form_students/create/create.html', context)

def createComment(request,id):
    user = request.user
    student = Student.objects.get(user=user)
    lesson = Lesson.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            create_comment = form.save(commit=False)
            create_comment.student = student
            create_comment.lesson_id = id
            create_comment.save()
            return redirect('detail_lesson',id)
    else:
        form = CommentForm()
    context = {
        "form":form,
        'student': student,
        'lesson':lesson,
    }
    return render(request, 'student/form_students/create/create.html', context)


def updatStudent(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(data=(request.POST or None),files=(request.FILES or None),instance = student)
    if form.is_valid():
        form.save()
        return redirect('student_page')
    context = {
        'form':form,
        'student': student,
    }
    return render(request, 'student/form_students/update/updat.html', context)

def updateComment(request,id,id_lesson):
    user = request.user
    student = Student.objects.get(user=user)
    get_comment = Comment.objects.get(id=id)
    form = CommentForm(data=(request.POST or None),files=(request.FILES or None),instance = get_comment)
    if form.is_valid():
        form.save()
        return redirect('detail_lesson',id_lesson)
    context = {
        'form':form,
        'student': student,
    }
    return render(request, 'student/form_students/update/updat.html', context)

def deleteComment(request,id,id_lesson):
    get_comment = Comment.objects.get(id=id)
    get_comment.delete()
    return redirect('detail_lesson',id_lesson)
    