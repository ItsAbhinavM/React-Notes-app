from django.urls import path
from .views import*
from . import views

urlpatterns = [
    path('djangonotes/', NoteListView.as_view()),
    path('djangonotes/<int:pk>/', views.saveNote,name="saving note"),
    path('delete/<int:pk>/',views.deleteNote,name="delete note")
]

'''urlpatterns = [
    path('notes/', NoteListCreateView.as_view(),name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-retrieve-update-destroy'),
]'''