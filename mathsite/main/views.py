from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import RankingTo10, RankingTo50
from random import randint

def mainpage(response):
    return render(response, "main/mainpage.html")

def rankingi(request):
    return render(request, "main/rankingi.html")

def ranking10(request):
    sort_by = request.POST.get("sort_by", "-Score")
    rk = RankingTo10.objects.all().order_by(sort_by)
    
    filter_by = request.POST.get('filter_by', '')

    if filter_by:
        rk = RankingTo10.objects.filter(PlayerName=request.user).order_by(sort_by)
    else:
        rk = RankingTo10.objects.all().order_by(sort_by)
    return render(request, "main/ranking.html", {"rk":rk})

def ranking50(request):
    sort_by = request.POST.get("sort_by", "-Score")
    rk = RankingTo50.objects.all().order_by(sort_by)
    
    filter_by = request.POST.get('filter_by', '')

    if filter_by:
        rk = RankingTo50.objects.filter(PlayerName=request.user).order_by(sort_by)
    else:
        rk = RankingTo50.objects.all().order_by(sort_by)
    return render(request, "main/ranking.html", {"rk":rk})

def SelOfMult(request):
    return render(request, "main/mnozenie.html")

def Multiplication(request, nr_of_questions):
    if (request.method == 'POST') and (request.session.get('nr', 0) < nr_of_questions):
        request.session['nr'] = request.session.get('nr', 0) + 1

        # pobieramy aktualną odpowiedź z formularza
        if request.POST['current_answer']:
                current_answer = int(request.POST['current_answer'])
        else:
            current_answer = "101"

        #sprawdzanie czy takie same 
        is_answer_correct = (request.session['question'][0]*request.session['question'][1]) == current_answer
        if is_answer_correct:
            request.session['correct_answers'] = request.session.get('correct_answers', 0) + 1

        # pobieramy kolejne pytanie
        request.session['question'] = [randint(1, 10), randint(1, 10)]

        return render(request, 'main/mnozenie10.html', {'question': request.session['question'], 'correct_answers': request.session['correct_answers'], 'nr_question': request.session['nr']})
    
    elif request.session.get('nr', 0) == nr_of_questions:
        if nr_of_questions == 50:
            if request.user.is_authenticated:
                m = RankingTo50(PlayerName=request.user, Score=request.session['correct_answers'])
                m.save()
            else:
                m = RankingTo50(PlayerName=None, Score=request.session['correct_answers'])
                m.save()

        elif nr_of_questions == 10:
            if request.user.is_authenticated:
                m = RankingTo10(PlayerName=request.user, Score=request.session['correct_answers'])
                m.save()
            else:
                m = RankingTo10(PlayerName=None, Score=request.session['correct_answers'])
                m.save()
        number_of_correct_a = request.session['correct_answers']
        if (request.session['correct_answers']*2)>=request.session['nr']:
            gz = True
        else:
            gz = False
        request.session['nr'] = 0
        request.session['correct_answers'] = 0
        return render(request, "main/congratulations.html", {'correct_answers': number_of_correct_a, 'nr_question': nr_of_questions, "gz":gz})
    else:
        request.session['nr'] = 0
        request.session['correct_answers'] = 0
        request.session['question'] = [randint(1, 10), randint(1, 10)]
        return render(request, 'main/mnozenie10.html', {'question': request.session['question'], 'correct_answers': request.session['correct_answers'], 'nr_question': request.session['nr']})

class profile(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/profile.html', {'user': request.user})

class deleteAccount(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'main/deleteAcc.html'
    success_url = reverse_lazy('mainpage')

    def get_object(self):
        username = self.kwargs.get("username")
        return User.objects.get(username=username)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        RankingTo10.objects.filter(PlayerName=user).delete()
        return super().delete(request, *args, **kwargs)
        



