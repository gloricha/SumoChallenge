from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test

from .models import Question


def survey(request):
        
    if request.method == 'POST':
        #Get choice
        question = get_object_or_404(Question, pk=request.POST['question_id'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #Update choice
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('survey:thanks'))
    
    
    #request.method == 'GET'
    else: 
        question_pool = Question.objects.all()    
        #Get previous answered questions to avoid rendering them again.
        if request.COOKIES.has_key('prev_ques'):
            previous_questions_ids = request.COOKIES['prev_ques'].split(';')
            question_pool = question_pool.exclude(id__in=previous_questions_ids)
        else: previous_questions_ids = []
        #Try to get random question the haven't been presented yet to pass to 
        #the template, otherwise pass None
        try: 
            question = question_pool.order_by('?')[:1].get()
            previous_questions_ids.append( str(question.id) )
        except Exception: question = None
        
        response =  render(request, 'survey/survey.html', {'question': question})
        response.set_cookie('prev_ques', ';'.join(previous_questions_ids))
        
        return response




@user_passes_test(lambda u: u.is_superuser, 
                  login_url='http://localhost:8000/admin/login/?next=/survey/results')
def results(request):
    """
    Allow access only for admins
    """
    p = Question.objects.all() or None
    return render(request, 'survey/results.html', {'questions': p, } )
