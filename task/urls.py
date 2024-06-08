from django.urls import path

from .views import *
urlpatterns = [
    # path('get_products/', GetProductsView.as_view()),
    # path('create_product/', CreateProductView.as_view()),
    # path('get_product/<int:pk>',GetProductView.as_view())
    path('get_tasks',get_tasks),
    path('create_task', create_task),
    path('get_task/<int:id>', get_task),
    path('update_task/<int:id>', update_task)
]
