from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .models import RankingTo10, RankingTo50
from random import randint
from ast import literal_eval

def mainpage(response):
    return render(response, "main/mainpage.html")

def rankingi(request):
    return render(request, "main/rankingi.html")

def ranking10(request):
    sort_by = request.POST.get("sort_by", "-Score")
    rk = RankingTo10.objects.all().order_by(sort_by)
    
    filter_by = request.POST.get('filter_by', '')

    if filter_by:
        rk = RankingTo10.objects.filter(PlayerName=request.user.username).order_by(sort_by)
    else:
        rk = RankingTo10.objects.all().order_by(sort_by)
    return render(request, "main/ranking.html", {"rk":rk})

def ranking50(request):
    sort_by = request.POST.get("sort_by", "-Score")
    rk = RankingTo50.objects.all().order_by(sort_by)
    
    filter_by = request.POST.get('filter_by', '')

    if filter_by:
        rk = RankingTo50.objects.filter(PlayerName=request.user.username).order_by(sort_by)
    else:
        rk = RankingTo50.objects.all().order_by(sort_by)
    return render(request, "main/ranking.html", {"rk":rk})

def mnozenie(request):
    return render(request, "main/mnozenie.html")

def mnozenie10(request):
    if (request.method == 'POST') and (request.session.get('nr', 0) < 10):
        request.session['nr'] = request.session.get('nr', 0) + 1
        # print(request.POST['current_answer'])
        # print(request.POST['current_question'])
        # pobieramy aktualne pytanie i odpowiedź z formularza
        current_question = literal_eval(request.POST['current_question'])
        if request.POST['current_answer']:
            current_answer = int(request.POST['current_answer'])
        else:
            current_answer = "101"
        #sprawdzanie czy takie same 
        is_answer_correct = (current_question[0]*current_question[1]) == current_answer
        if is_answer_correct:
            request.session['correct_answers'] = request.session.get('correct_answers', 0) + 1
        
        # pobieramy kolejne pytanie
        next_question = [randint(1, 10), randint(1, 10)]
        
        return render(request, 'main/mnozenie10.html', {'question': next_question, 'correct_answers': request.session['correct_answers'], 'nr_question': request.session['nr']})
    elif request.session.get('nr', 0) == 10:
        #dodanie do bazy
        if request.user.is_authenticated:
            m = RankingTo10(PlayerName = request.user.username, Score = request.session['correct_answers'])
            m.save()
        else:
            m = RankingTo10(PlayerName = "Anonim", Score = request.session['correct_answers'])
            m.save()
        number_of_q = request.session['nr']
        number_of_correct_a = request.session['correct_answers']
        if (request.session['correct_answers']*2)>=request.session['nr']:
            gz = True
        else:
            gz = False
        request.session['nr'] = 0
        request.session['correct_answers'] = 0
        return render(request, "main/congratulations.html", {'correct_answers': number_of_correct_a, 'nr_question': number_of_q, "gz":gz})
    else:
        request.session['nr'] = 0
        request.session['correct_answers'] = 0
        first_question = [randint(1, 10), randint(1, 10)]
        return render(request, 'main/mnozenie10.html', {'question': first_question, 'correct_answers': request.session['correct_answers'], 'nr_question': request.session['nr']})
    
def mnozenie50(request):
    if (request.method == 'POST') and (request.session.get('nr', 0) < 50):
        request.session['nr'] = request.session.get('nr', 0) + 1
        # pobieramy aktualne pytanie i odpowiedź z formularza
        current_question = literal_eval(request.POST['current_question'])
        if request.POST['current_answer']:
            current_answer = int(request.POST['current_answer'])
        else:
            current_answer = "101"
        #sprawdzanie czy takie same 
        is_answer_correct = (current_question[0]*current_question[1]) == current_answer
        if is_answer_correct:
            request.session['correct_answers'] = request.session.get('correct_answers', 0) + 1
        
        # pobieramy kolejne pytanie
        next_question = [randint(1, 10), randint(1, 10)]
        
        return render(request, 'main/mnozenie10.html', {'question': next_question, 'correct_answers': request.session['correct_answers'], 'nr_question': request.session['nr']})
    elif request.session.get('nr', 0) == 50:
        #dodanie do bazy
        if request.user.is_authenticated:
            m = RankingTo50(PlayerName = request.user.username, Score = request.session['correct_answers'])
            m.save()
        else:
            m = RankingTo50(PlayerName = "Anonim", Score = request.session['correct_answers'])
            m.save()
        number_of_q = request.session['nr']
        number_of_correct_a = request.session['correct_answers']
        if (request.session['correct_answers']*2)>=request.session['nr']:
            gz = True
        else:
            gz = False
        request.session['nr'] = 0
        request.session['correct_answers'] = 0
        return render(request, "main/congratulations.html", {'correct_answers': number_of_correct_a, 'nr_question': number_of_q, "gz":gz})
    else:
        request.session['nr'] = 0
        request.session['correct_answers'] = 0
        first_question = [randint(1, 10), randint(1, 10)]
        return render(request, 'main/mnozenie10.html', {'question': first_question, 'correct_answers': request.session['correct_answers'], 'nr_question': request.session['nr']})
    



