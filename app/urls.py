
from django.urls import path
from . import views

urlpatterns=[
           path('', views.HomePageView.as_view(), name="home"),
           path(r'^ajax/specialDiv/', views.specialDiv, name='specialDiv'),
           path(r'^ajax/show_detail/', views.show_detail, name='show_detail'),
           path(r'^ajax/send_message/', views.send_message, name='send_message'),
           path('save-patient',views.save_patient, name="save-patient"),
           path('add-quicktext',views.add_quicktext, name="add-quicktext"),
    #path(r'^ajax/get_response/$', views.answer_me, name='get_response'),
    ]
