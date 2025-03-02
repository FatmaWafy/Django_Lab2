from django.urls import path
from .views import school_list, school_create, school_update, school_delete, classroom_list, classroom_create

urlpatterns = [

    path('schools/', school_list, name='school_list'),
    path('schools/create/', school_create, name='school_create'),
    path('schools/update/<int:pk>/', school_update, name='school_update'),
    path('schools/delete/<int:pk>/', school_delete, name='school_delete'),


    path('classrooms/', classroom_list, name='classroom_list'),
    path('classrooms/create/', classroom_create, name='classroom_create'),
]
