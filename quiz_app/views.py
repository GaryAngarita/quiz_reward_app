from django.shortcuts import redirect, render
from .models import *



def cover(request):
    return render(request, "cover.html")

def addQuestion(request):
    if request.user.is_staff:
        if request.method == 'POST':
            question = request.POST['question']
            op1 = request.POST['op1']
            op2 = request.POST['op1']
            op3 = request.POST['op1']
            op4 = request.POST['op1']
            ans = request.POST['op1']
    pass

def register(request):
    pass

def kid_login(request):
    pass

def adult_login(request):
    pass

def quiz_lite(request):
    if request.method == 'POST':
        querys = Query.objects.all()
        request.session['score'] = 0
        request.session['wrong'] = 0
        request.session['correct'] = 0
        request.session['total'] = 0
        for q in querys:
            request.session['total']+=1
            print(request.POST.get(q.query))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                request.session['score']+=10
                request.session['correct']+=1
            else:
                request.session['wrong']+=1
        request.session['percent'] = request.session['score'] / (request.session['total'] * 10) * 100
        return redirect('/results')
    else:
        querys = Query.objects.all()
        context = {
            'questions': querys
        }
        return render(request, 'quizlite.html', context)
    pass

def results(request):
    context = {
            'score': request.session['score'],
            'time': request.POST.get('timer'),
            'correct': request.session['correct'],
            'wrong': request.session['wrong'],
            'percent': request.session['percent'],
            'total': request.session['total']
        }
    return render(request, 'result.html', context)



def logout(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
