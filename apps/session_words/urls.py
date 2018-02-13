from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^session_words/clear$', views.clear),
  url(r'^session_words/process$', views.process),
  url(r'^session_words/$', views.index)     # This line has changed!
]
