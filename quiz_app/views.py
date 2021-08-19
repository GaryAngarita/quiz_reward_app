from django.core.checks import messages
from django.shortcuts import redirect, render
import bcrypt
from django.contrib import messages
from .models import *



def cover(request):
    return render(request, "cover.html")

def logreg(request):
    return render(request, 'register.html')

def register(request):
    errors = User.objects.reg_val(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/logreg')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user = User.objects.create(first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = pw_hash,)
        messages.success(request, "Registration successful!")
        request.session['id'] = user.id
        request.session['score'] = 0
        request.session['wrong'] = 0
        request.session['correct'] = 0
        request.session['total'] = 0
        request.session['percent'] = 0
    return redirect(f'start_lite/{user.id}')

def kid_login(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.log_val(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/logreg')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['id'] = user.id
        return redirect(f'start_lite/{user.id}')

def start_lite(request, user_id):
    context = {
        'user': User.objects.get(id = user_id),
        'querys': Query.objects.all()
    }
    return render(request, "quizlite.html", context)

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

def adult_login(request):
    pass

def process_quiz(request):
    if request.method == 'POST':
        querys = Query.objects.all()
        score = request.session['score']
        wrong = request.session['wrong']
        correct = request.session['correct']
        total = request.session['total']
        percent = request.session['percent']
        for q in querys:
            total+=1
            print(request.POST.get(q.query))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score / (total * 10) * 100
        request.session['percent'] = percent
        request.session['total'] = total
        request.session['correct'] = correct
        request.session['wrong'] = wrong
        request.session['score'] = score
        return redirect('/results')
    else:
        querys = Query.objects.all()
        context = {
            'questions': querys
        }
        return render(request, 'quizlite.html', context)

def results(request):
    context = {
        'user': User.objects.get(id = request.session['id']),
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
