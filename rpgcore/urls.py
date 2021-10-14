from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns.extend(views.ItemEffectViews().get_paths())
urlpatterns.extend(views.ItemEffectTypeViews().get_paths())
urlpatterns.extend(views.ItemInstanceViews().get_paths())
urlpatterns.extend(views.ItemPropertyViews().get_paths())
urlpatterns.extend(views.ItemSpecialPropertyViews().get_paths())
urlpatterns.extend(views.ItemTypeViews().get_paths())
urlpatterns.extend(views.ItemViews().get_paths())
