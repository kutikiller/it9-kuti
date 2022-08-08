from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from project.views import general
from project.views import admins
from project.views import students



urlpatterns = [
    path('', general.loginPage, name='login'),
    path('register/', general.registerPage, name='register'),
    path('logout/', general.logoutUser, name='logout'),

    path('student_page/', students.studentPage, name='student_page'),
    path('admin_page/', admins.adminPage, name='admin_page'),
    
    path('student_ball/<id>', students.studentBall, name='student_ball'),

    path('detail_group/<id>', students.detailGroup, name='detail_group'),
    path('detail_lesson/<id>', students.detailLesson, name='detail_lesson'),
    path('detail_group_admin/<id>', admins.detailGroup, name='detail_group_admin'),

    path('create_comment/<id>', students.createComment, name='create_comment'),
    path('create_home_work_student/<id_home_work>/<id_lesson>', students.createHomeWorkStudent, name='create_home_work_student'),
    path('create_homework/<id>', admins.createHomework, name='create_homework'),

    path('updat_student/<id>', students.updatStudent, name='updat_student'),
    path('update_comment/<id>/<id_lesson>', students.updateComment, name='update_comment'),
    path('updat_admin/<id>', admins.updatAdmin, name='updat_admin'),
    
    path('delete_comment/<id>/<id_lesson>', students.deleteComment, name='delete_comment'),

    path('group/hajj-form/', admins.create_group_form, name="group-hajj"),
    path('group/path/<int:pk>/detail/', admins.group_detail, name="detail-group"),
    path('group/path/<int:pk>/delete/', admins.delete_group, name="delete-group"),
    path('group/path/<int:pk>/update/', admins.update_group, name="update-group"),

    path('studentgroup/hajj-form/', admins.create_studentgroup_form, name='studentgroup-hajj'),
    path('studentgroup/path/<int:pk>/detail/', admins.studentgroup_detail, name="detail-studentgroup"),
    path('studentgroup/path/<int:pk>/delete/', admins.studentgroup_delete, name="delete-studentgroup"),
    path('studentgroup/path/<int:pk>/update/', admins.update_studentgroup, name="update-studentgroup"),

    path('lesson/hajj-form/', admins.create_lesson_form, name='lesson-hajj'),
    path('lesson/path/<int:pk>/detail/', admins.lesson_detail, name="detail-lesson"),
    path('lesson/path/<int:pk>/delete/', admins.lesson_delete, name="delete-lesson"),
    path('lesson/path/<int:pk>/update/', admins.update_lesson, name="update-lesson"),
    
    # path('homework/hajj-form/', admins.create_homework_form, name='homework-hajj'),
    # path('homework/path/<int:pk>/detail/', admins.homework_detail, name="detail-homework"),
    # path('homework/path/<int:pk>/delete/', admins.homework_delete, name="delete-homework"),
    # path('homework/path/<int:pk>/update/', admins.update_homework, name="update-homework"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)