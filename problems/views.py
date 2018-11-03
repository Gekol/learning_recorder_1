from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from .models import Problem, Solution
from .forms import NewProblem, NewSolution
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_main(request):
    return render(request, "base.html", {})

@login_required
def show_problems(request):
    problems = Problem.objects.all().filter(owner=request.user).order_by("-date_added")
    return render(request, "problems.html", {"problems": problems})

@login_required
def add_problem(request):
    if request.method == "GET":
        form = NewProblem()
        return render(request, "new_problem.html", {"form": form})
    else:
        form = NewProblem(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.owner = request.user
            problem.save()
        return HttpResponseRedirect(reverse("problems:problems"))

@login_required
def show_problem(request, problem_id):
    problem = Problem.objects.all().get(id=problem_id)
    solutions = Solution.objects.filter(problem=problem).order_by("-date_added")
    for i in range(len(solutions)):
        solutions[i].algorythm = solutions[i].algorythm[:50] + " ..."
        solutions[i].code = solutions[i].code[:50] + " ..."
    context = {"problem": problem, "solutions": solutions}
    return render(request, "problem.html", context)

@login_required
def add_solution(request, problem_id):
    problem = Problem.objects.all().get(id=problem_id)
    if request.method == "GET":
        form = NewSolution()
    else:
        form = NewSolution(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.problem = problem
            solution.owner = request.user
            solution.save()
        return HttpResponseRedirect(reverse("problems:problem", args=[problem_id]))
    context = {"form": form}
    return render(request, "new_solution.html", context)

@login_required
def show_solution(request, problem_id, solution_id):
    solution = Solution.objects.get(id=solution_id)
    problem = Problem.objects.get(id=problem_id)
    return render(request, "solution.html", {"solution": solution, "problem": problem})

@login_required
def edit_solution(request, solution_id):
    solution = Solution.objects.get(id=solution_id)
    form = NewSolution(instance=solution)
    if request.method == "GET":
        return render(request, "edit_solution.html", {"form": form})
    else:
        form = NewSolution(request.POST, instance=solution)
        if form.is_valid():
            solution = form.save()
            solution.save()
        return HttpResponseRedirect(reverse("problems:show_solution", args=[solution.problem.id, solution.id]))

@login_required
def edit_problem(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    form = NewProblem(instance=problem)
    if request.method == "GET":
        return render(request, "edit_problem.html", {"form": form})
    else:
        form = NewProblem(request.POST, instance=problem)
        if form.is_valid():
            problem = form.save()
            problem.save()
        return HttpResponseRedirect(reverse("problems:problem", args=[problem_id]))

def delete_problem(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    problem.delete()
    return HttpResponseRedirect(reverse("problems:problems"))

def delete_solution(request, solution_id):
    solution = Solution.objects.get(id=solution_id)
    problem_id = solution.problem.id
    solution.delete()
    return HttpResponseRedirect(reverse("problems:problem", args=[problem_id]))