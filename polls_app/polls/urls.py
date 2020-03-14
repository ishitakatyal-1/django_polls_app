from django.urls import path
from .views import index, detail, results, vote

appname = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:ques_id>/', detail, name='detail'),
    path('results/<int:ques_id>/', results, name='results'),
    path('vote/<int:ques_id>/', vote, name='vote')
]