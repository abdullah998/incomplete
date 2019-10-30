from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts',views.BlogPostSet)

app_name='myapi'

urlpatterns=[
    path('',include(router.urls)),
    path('posts2',views.ApiFunc.as_view()),
    path('posts3',views.ApiFunc2.as_view()),
]
