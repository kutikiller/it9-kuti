from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from project.decorators import allowed_users
from project.servises import get_groups, get_students, get_studentgroup, get_students_attendence, study_year, \
    lessons_objects, daily_material_objects, get_home_work
from project.models import *
from project.forms import *

from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.views.generic.edit import FormView
from django.contrib import messages
from django.http import HttpResponse,HttpResponseNotAllowed
from django.template.loader import render_to_string

def updatAdmin(request,id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(data=(request.POST or None),files=(request.FILES or None),instance = teacher)
    if form.is_valid():
        form.save()
        return redirect('admin_page')
    context = {
        'form':form,
        'teacher': teacher,
    }
    return render(request, 'admin/form_admin/update/updat.html', context)


def create_group_form(request):
    form = GroupsForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "admin/group/group-form.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    user = request.user
    teacher = Teacher.objects.get(user=user)    
    
    group = Groups.objects.all()
 
    if request.method == "POST":
        form = GroupsForm(request.POST,)
        if form.is_valid():
            groups_instance = form.save(commit=False)
            groups_instance.teacher_id = teacher.id
            groups_instance.save()
            return redirect("detail-group", pk=groups_instance.id)
        else:
            return render(request, "admin/group/group-form.html", context={
                "form": form
            })
    else:
        form = GroupsForm()
    context = {
        "form": form,
        "group": group,
        "navbar": "groups",
        'teacher':teacher,
    }
    return render(request,'admin/admin_page.html',context)

def group_detail(request, pk):
    try:
        group = Groups.objects.get(id=pk)
    except Groups.DoesNotExist:
        raise Http404

    context = {
        "group": group
    }
    return render(request, "admin/group/group-detail.html", context)

def update_group(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    form = GroupsForm(request.POST or None , instance=group)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-group", pk=group.id)

    context = {
        "form": form,
        "group": group,
    }

    return render(request, "admin/group/group-form.html", context)

def delete_group(request, pk):
    group = get_object_or_404(Groups, pk=pk)
 
    if request.method == "POST":
        group.delete()
        return HttpResponse("")
 
    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )



def create_studentgroup_form(request):
    form1 = StudentGroupForm(request.POST or None)
    context = {
        "form1": form1
    }
    return render(request, "admin/group/studentgroup-form.html", context)

def studentgroup_detail(request, pk):
    try:
        studentgroup = StudentGroup.objects.get(id=pk)
    except StudentGroup.DoesNotExist:
        raise Http404
    context = {
        "studentgroup": studentgroup
    }
    return render(request, "admin/group/studentgroup-datail.html", context)

def studentgroup_delete(request, pk):
    studentgroup = get_object_or_404(StudentGroup, pk=pk)
 
    if request.method == "POST":
        studentgroup.delete()
        return HttpResponse("")
 
    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

def update_studentgroup(request, pk):
    studentgroup = get_object_or_404(StudentGroup, pk=pk)
    form1 = StudentGroupForm(request.POST or None , instance=studentgroup)

    if request.method == "POST":
        if form1.is_valid():
            form1.save()
            return redirect("detail-studentgroup", pk=studentgroup.id)

    context = {
        "form1": form1,
        "studentgroup": studentgroup,
    }

    return render(request, "admin/group/studentgroup-form.html", context)

def detailGroup(request,id):
    user = request.user
    teacher = Teacher.objects.get(user=user)
    group = Groups.objects.get(id=id)
    studentgroup = StudentGroup.objects.filter(group=group)
    lesson = Lesson.objects.filter(group=group)

    if request.method=='POST' and 'lesson':
        form2 = LessonForm(request.POST)
        if form2.is_valid():
            lesson_form = form2.save(commit=False)
            lesson_form.group_id = group.id
            lesson_form.save()
            return redirect("detail-lesson", pk=lesson_form.id)
        else:
            return render(request, "admin/group/lesson-form.html", context={
                "form2": form2
            })
    else:
        form2 = LessonForm()

    if request.method=='POST' and 'studentgroup':
        form1 = StudentGroupForm(request.POST)
        if form1.is_valid():
            studentgroup = form1.save(commit=False)
            studentgroup.group_id = group.id
            studentgroup.save()
            return redirect("detail-studentgroup", pk=studentgroup.id)
        else:
            return render(request, "admin/group/studentgroup-form.html", context={
                "form1": form1
            })
    else:
        form1 = StudentGroupForm()


    context = {
        "form1": form1,
        "form2": form2,
        "studentgroup": studentgroup,
        "lesson":lesson,
        'group':group,
        'teacher': teacher,
    }
    return render(request, 'admin/dateil/dateil_group.html', context)

def create_lesson_form(request):
    form2 = LessonForm(request.POST or None)
    context = {
        "form2": form2
    }
    return render(request, "admin/group/lesson-form.html", context)

def lesson_detail(request, pk):
    try:
        lesson = Lesson.objects.get(id=pk)
    except lesson.DoesNotExist:
        raise Http404
    context = {
        "lesson": lesson
    }
    return render(request, "admin/group/lesson-datail.html", context)

def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
 
    if request.method == "POST":
        lesson.delete()
        return HttpResponse("")
 
    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )

def update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    form2 = LessonForm(request.POST or None , instance=lesson)

    if request.method == "POST":
        if form2.is_valid():
            form2.save()
            return redirect("detail-lesson", pk=lesson.id)

    context = {
        "form2": form2,
        "lesson": lesson,
    }

    return render(request, "admin/group/lesson-form.html", context)

def createHomework(request,id):
    user = request.user
    teacher = Teacher.objects.get(user=user)
    form = HomeWorkForm(request.POST )
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("create_homework", id)

    context = {
        "form": form,
        "teacher": teacher,
        "id":id,
    }

    return render(request, "admin/form_admin/create/create.html", context)
