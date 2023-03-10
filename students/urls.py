from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='home'),
    path('add/',views.add_student,name='add_student'),
    path('edit/<int:id>',views.edit_student,name='edit_student'),
    path('delete/<int:id>',views.del_student,name='del_student')
]