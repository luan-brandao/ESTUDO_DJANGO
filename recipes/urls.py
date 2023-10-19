from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="recipes-home"),
    path(
        "recipes/categoty/<int:category_id>/", views.category, name="recipes-category"
    ),
    path("recipes/<int:id>/", views.recipe, name="recipes-recipe"),
]
