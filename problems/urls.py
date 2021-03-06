from django.urls import path

from . import views
app_name = 'problems'
urlpatterns = [
    path('', views.show_main, name="main_page"),
    path('problems', views.show_problems, name='problems'),
    path('new_problem', views.add_problem, name='new_problem'),
    path(r'problems/problem/<int:problem_id>', views.show_problem, name='problem'),
    path(r'problems/problem/<int:problem_id>/new_solution', views.add_solution, name="new_solution"),
    path(r'problems/problem/<int:problem_id>/solution/<int:solution_id>', views.show_solution, name="show_solution"),
    # path(r"problems/problem/<int:problem_id>/solution/<int:solution_id>/edit", views.edit_solution, name="edit_solution"),
    path(r"edit_solution/<int:solution_id>", views.edit_solution, name="edit_solution"),
    path(r"edit_problem/<int:problem_id>", views.edit_problem, name="edit_problem"),
    path(r"delete_problem/<int:problem_id>", views.delete_problem, name="delete_problem"),
    path(r"delete_solution/<int:solution_id>", views.delete_solution, name="delete_solution"),
]
