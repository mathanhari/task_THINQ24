# importing django routing libraries
# import accounts
from . import views
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
	# home page
	path('', views.postslist.as_view(), name='posts'),
	# route for posts
	path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
	# path('<slug:slug>/', views.post_detail, name='post_detail')
]
