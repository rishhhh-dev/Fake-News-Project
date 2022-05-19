



from django.urls import path
from fn_app import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('article/',views.ArticleView,name='article'),
    path('valid/',views.Validate,name='valid')
]