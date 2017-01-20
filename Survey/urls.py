from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # ex: /survey/
    url(r'^$', views.survey, name='survey'),
    # ex: /survey/thanks/
    url(r'^thanks/$', TemplateView.as_view(template_name='survey/thanks.html'), 
        name='thanks'),
    # ex: /survey/results/
    url(r'^results/$', views.results, name='results'),
]