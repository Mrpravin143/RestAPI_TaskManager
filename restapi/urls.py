from django.urls import path
from restapi.views import *

urlpatterns = [
    path("api/index",index,name='index'),
    path("api/create_records",create_records,name='create_records'),
    path("api/fetchdata",fetchdata,name='fetchdata'),
    path("api/deleteRecords/<id>/",deleteRecords,name='deleteRecords'),
    path("api/update/<id>/",update,name='update'),    

    # Practice API Create by me

    path('api/Pcreate', Pcreate , name='Pcreate'),
    path('api/Pget', Pget , name='Pget'),
    path('api/Pdelete/<id>/', Pdelete , name='Pdelete'),
    path('api/Pupdate/<id>/', Pupdate , name='Pupdate'),
    path('api/Statusget', Statusget , name='Statusget'),


    # Serializer -> (Model Serializers)

    path('api/GetData',get_data),
    path('api/generateRecords',generateRecords),
    path('api/update_data',update_data),
    path('api/delete_data',delete_data),

    # Serializer -> (Normal Serializers)

    path('api/data_create',data_create),
    path('api/get_data_of_normal',get_data_of_normal),
    path('api/update_student',update_student),
    path('api/delete_student/<pk>/',delete_student),

    # api views routs

    path('api/mixins/apiview' , StudentAPIView.as_view() , name='StudentAPIView'),

    # mixins

    path('api/drf/mixins/student_mixin_api/', StudentMixins.as_view()),
    path('api/drf/mixins/student_mixin_api/<int:pk>/', StudentMixins.as_view()),
    
]
