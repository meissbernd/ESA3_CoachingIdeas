from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import CommentForm
from .models import Exercise, Comment


# Create your views here.
def home(request):
    search_exercise = request.GET.get("searchExercise")
    if search_exercise:
        exercises = Exercise.objects.filter(title__icontains=search_exercise)
    else:
        exercises = Exercise.objects.all()

    return render(request, "home.html",
                  {"searchExercise": search_exercise,
                   "exercises": exercises})


def exercise_list(request):
    exercises = Exercise.objects.all().order_by("created_on")
    return render(request,
                  "exercise_list.html",
                  {"page_title": "Trainingsübungen",
                   "exercises": exercises})


def detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    comments = Comment.objects.filter(exercise=exercise)
    return render(request, 'detail.html',
                  {'exercise': exercise,
                   "comments": comments})


def create_comment(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == 'GET':
        return render(request, 'create_comment.html',
                      {'form': CommentForm(), 'exercise': exercise})
    else:
        try:
            form = CommentForm(request.POST)
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.exercise = exercise
            new_comment.save()
            return redirect('detail',
                            new_comment.exercise.id)
        except ValueError:
            return render(request,
                          'create_comment.html',
                          {'form': CommentForm(), 'error': 'bad data passed in'})


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == 'GET':
        form = CommentForm(instance=comment)
        return render(request, 'update_comment.html',
                      {'comment': comment, 'form': form})
    else:
        try:
            form = CommentForm(request.POST, instance=comment)
            form.save()
            return redirect('detail', comment.exercise.id)
        except ValueError:
            return render(request,
                          'update_comment.html',
                          {'review': comment, 'form': form,
                           'error': 'Bad data in form'})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    comment.delete()
    return redirect('detail', comment.exercise.id)


def about(request):
    return HttpResponse("<h1>About")
