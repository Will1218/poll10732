from django.urls import path
from .views import *

urlpatterns = [
  # path('poll/',views.poll_list),
   path('poll2/', PollList.as_view()),
   path('poll/<int:pk>/', PollDetail.as_view()),
   path('option/<int:oid>',Pollvote.as_view()),
]