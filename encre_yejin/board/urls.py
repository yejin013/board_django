from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    # path('signout/', views.signout, name='signout'),
    # path('', views.list, name='list'),
    # path('<int:pk>/', views.detail, name='detail'),
    path('', views.PostList.as_view(), name='list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail')
]