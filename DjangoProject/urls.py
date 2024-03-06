from django.urls import path, re_path, include
from hello import views



products_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]

product_patterns = [
    path("", views.product),
    path("comments", views.comments),
    path("questions", views.questions),
]


# Очередность маршрутов важна!
urlpatterns = [
    re_path(r"^about", views.about, kwargs={"name": "Nikita", "age": 23}),
    re_path(r"^contact", views.contact),
    path("", views.index),
    path("products/<int:p_id>/", include(product_patterns)),
    path("products/", include(products_patterns)),
]
