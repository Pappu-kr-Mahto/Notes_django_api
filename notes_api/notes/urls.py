from django.urls import path,include
from . import views

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('',views.home,name="home"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/login/',views.login,name="login"),
    path('api/signup/',views.signup,name="signup"),

    path('api/notes/',views.allNotes,name="allNotes"),
    
    path('api/notes/create/',views.crateNote,name="crateNote"),

    path('api/notes/<id>',views.notesById,name="notesById"),

    path('api/notes/share/',views.shareNotes,name="shareNotes"),
    
    path('api/notes/version-history/<id>',views.notesVersion,name="notesVersion"),
    
]
