from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, ExerciseForm
from .models import Comment, Exercise


def home(request):
    search_exercise = request.GET.get("searchExercise")

    if search_exercise:
        search_exercise = Exercise.objects.filter(
            Q(title__icontains=search_exercise)
            | Q(body__icontains=search_exercise)
            | Q(soccer_skills__icontains=search_exercise)  # Correct field name
        ).order_by("-average_rating")
    else:
        search_exercise = Exercise.objects.all().order_by("-average_rating")

    paginator = Paginator(search_exercise, 6)

    page = request.GET.get("page")
    try:
        exercises = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exercises = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exercises = paginator.page(paginator.num_pages)

    return render(
        request,
        "home.html",
        {"searchExercise": search_exercise, "exercises": exercises},
    )


def exercise_list(request):
    exercises = Exercise.objects.all().order_by("created_on")
    return render(
        request,
        "exercise_list.html",
        {"page_title": "Trainingsübungen", "exercises": exercises},
    )


def detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    comments = Comment.objects.filter(exercise=exercise)
    return render(request, "detail.html", {"exercise": exercise, "comments": comments})


@login_required
def create_comment(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == "GET":
        return render(
            request,
            "create_comment.html",
            {"form": CommentForm(), "exercise": exercise},
        )
    else:
        try:
            form = CommentForm(request.POST)
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.exercise = exercise
            new_comment.save()
            return redirect("detail", new_comment.exercise.id)
        except ValueError:
            return render(
                request,
                "create_comment.html",
                {"form": CommentForm(), "error": "bad data passed in"},
            )


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_authenticated)
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # , user = request.user
    if request.method == "GET":
        form = CommentForm(instance=comment)
        return render(
            request, "update_comment.html", {"comment": comment, "form": form}
        )
    else:
        try:
            form = CommentForm(request.POST, instance=comment)
            form.save()
            return redirect("detail", comment.exercise.id)
        except ValueError:
            return render(
                request,
                "update_comment.html",
                {"review": comment, "form": form, "error": "Bad data in form"},
            )


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_authenticated)
def update_exercise(request, exercise_id):
    update_exercise_html = "update_exercise.html"
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == "GET":
        form = ExerciseForm(instance=exercise)
        return render(
            request, update_exercise_html, {"exercise": exercise, "form": form}
        )
    else:
        try:
            form = ExerciseForm(request.POST, request.FILES, instance=exercise)
            if form.is_valid():
                form.save()
                return redirect("detail", exercise.id)
            else:
                return render(
                    request,
                    update_exercise_html,
                    {"exercise": exercise, "form": form, "error": "Invalid form data"},
                )
        except ValueError:
            return render(
                request,
                update_exercise_html,
                {"exercise": exercise, "form": form, "error": "Bad data in form"},
            )


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_authenticated)
def delete_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)

    if request.method == "POST":
        exercise.delete()
        return redirect("home")  # Redirect to the home page after deletion

    return render(request, "delete_exercise.html", {"exercise": exercise})


@login_required
@user_passes_test(lambda u: u.is_staff or u.is_authenticated)
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect("detail", comment.exercise.id)


@login_required
def create_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.creator = request.user
            exercise.save()
            return redirect("detail", exercise.id)
    else:
        form = ExerciseForm()

    return render(request, "create_exercise.html", {"form": form})


def about():
    return HttpResponse("<h1>About")
